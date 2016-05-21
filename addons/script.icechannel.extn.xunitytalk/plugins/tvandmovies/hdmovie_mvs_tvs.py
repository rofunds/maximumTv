'''
    Ice Channel
    buzzfilms.co
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay import Plugin

class hdmovie(MovieSource):
    implements = [MovieSource]
    
    name = "usmovieshd"
    display_name = "USMOVIESHD"
    base_url = 'http://usmovieshd.com/'
    
    source_enabled_by_default = 'true'

    
    def GetFileHosts(self, url, list, lock, message_queue):

        from entertainment.net import Net
        import re
        net = Net(cached=False)


        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                 'Referer': url}
        
        
        html = net.http_GET(url,headers=headers).content


        match=re.compile('data-lazy-src="(.+?)"').findall(html)[0]
     
        html = net.http_GET(match,headers=headers).content
        match=re.compile('"file":"(.+?)".+?label":"(.+?)"',re.DOTALL).findall(html)

        for url , res in match:            
               
                res =res.upper().replace('hd','').replace('HD','')
                if not 'p' in res.lower():
                    res=res+'P'                
                if '480' in res:
                    res='HD'

                url=url+'|'+res
                            
                self.AddFileHost(list, res, url)
                  

                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net
        import re

 
        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)
        #print ':::::::::::::::::::::::::::::::::'

        new_url ='http://usmovieshd.com/?s='+name.replace(' ','+')

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                 'Referer': 'http://usmovieshd.com/'}
       

        html = net.http_GET(new_url,headers=headers).content            
        match=re.compile('title="(.+?)".+?<a href="(.+?)"',re.DOTALL).findall(html)

        for TITLE,movie_url in match:
            if name.lower() in TITLE.lower():
                if year in TITLE.lower():

                    self.GetFileHosts(movie_url, list, lock, message_queue)

                    
                                
    def Resolve(self, url):
        
        url=url.split('|')[0]
        if 'redirector.googlevideo' in url:
            import urllib
            url=urllib.urlopen(url).geturl()
            
        return url

                
                
