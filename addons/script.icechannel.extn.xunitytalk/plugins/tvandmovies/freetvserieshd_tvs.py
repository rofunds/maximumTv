'''
    Istream
    Oneclickwatch
    Copyright (C) 2013 Coolwave

    version 0.1

'''


from entertainment.plugnplay import Plugin
from entertainment import common

from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.xgoogle.search import GoogleSearch


class freetvserieshd(TVShowSource):
    implements = [TVShowSource]
	
    #unique name of the source
    name = "seriestv"
    source_enabled_by_default = 'true'
    #display name of the source
    display_name = "FreeTvSeriesHD"
    
    #base url of the source website
    base_url = 'http://seriestv.us/'
    
    def GetFileHosts(self, url, list, lock, message_queue):
        import re

        from entertainment.net import Net
        net = Net(cached=False)

        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

        content = net.http_GET(url,headers=headers).content        
        data=re.compile('link:"(.+?)"',re.DOTALL).findall(content)[0]
        data={'link':data}

        if '720p' in content.lower():
                res='720P'
        elif '1080p' in content.lower():
                res='1080P'
        else:
                res='HD'                 
                
        content = net.http_POST('http://seriestv.us/plugins/gkpluginsphp.php',data,headers=headers).content
        import json
        data= json.loads(content)
                          
        self.AddFileHost(list, res, data['link'])



    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):

        import urllib2
        import re
        from entertainment.net import Net

        from entertainment import bing
        net = Net(cached=False)
        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)


        search_term ='%s Season %s Episode %s' %(name,season,episode)

        try:GOOGLED = self.GoogleSearch('seriestv.us', search_term)
        except:GOOGLED = bing.Search('seriestv.us', search_term)
        
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']
            if movie_url not in uniques:
                uniques.append(movie_url)
                if search_term.lower() in TITLE.lower():      
  
            
                    self.GetFileHosts(movie_url, list, lock, message_queue)
                   

    def Resolve(self, url):
        
        url=url.split('|')[0]
        if 'redirector.googlevideo' in url:
            import urllib
            url=urllib.urlopen(url).geturl()
            
        return url
