'''
    movieshd
    Copyright (C) 2014 Coolwave
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay import Plugin
from entertainment import common
import os

do_no_cache_keywords_list = ['Sorry for this interruption but we have detected an elevated amount of request from your IP']

class movieshd(MovieSource):
    implements = [MovieSource]
    
    name = "MoviesHD"
    display_name = "MoviesHD"
    cookie_file = os.path.join(common.cookies_path, 'MoviesHD')
    source_enabled_by_default = 'true'
    
    def GetFileHosts(self, url, list, lock, message_queue):
        import re
        from entertainment.net import Net
        net = Net(cached=False)
   
        content = net.http_GET(url).content

        r = '<video id="Google-(.+?)".+?<source src="(.+?)"'
        match  = re.compile(r).findall(content)
 
        for res,url in match:
            HOST=url.split('//')[1]
            HOST=HOST.split('/')[0]              
            res=res.upper()
            if '360' in res:
                res='HD'
            self.AddFileHost(list, res, url,host=HOST.upper())
            
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):
        import re
        from entertainment.net import Net
        
        net = Net(cached=False)


        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)

        content = net.http_GET('http://movieshd.tv/?s=%s'%name.replace(' ','+')).content
        
        match=re.compile('<a href="(.+?)" title="(.+?) \((.+?)\)">').findall(content)

        for url , _name , _year  in match:
            if name.lower() in _name.lower():
                if year in _year:
                    print 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'
                    self.GetFileHosts(url, list, lock, message_queue)
                    

    
    def Resolve(self, url):
      
        if 'redirector.googlevideo' in url:
            import urllib
            url=urllib.urlopen(url).geturl()
            
        return url
