'''
    Cartoon HD    
    Copyright (C) 2013 Mikey1234
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay import Plugin


class flixbreak(MovieSource):
    implements = [MovieSource]
    
    name = "FlixBreak"
    display_name = "FlixBreak"

   
    source_enabled_by_default = 'true'
           
    
    def GetFileHosts(self, url, list, lock, message_queue,type):

        import re
        from entertainment.net import Net
        net = Net(cached=False)
     


        link = net.http_GET(url).content
  
   
        FINAL_URL=re.compile('<iframe src="(.+?)"').findall(link)[0]
        host=FINAL_URL.split('://')[1]
        HOST=host.split('/')[0]
        self.AddFileHost(list, '720P', FINAL_URL,host=HOST.upper())
        
        
        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
        

      name=name.lower()

      item_url = 'http://flixbreak.com/watch-%s-full-movie' % (name.replace(' ','-'))
        
      self.GetFileHosts(item_url, list, lock, message_queue,type)


             

    def Resolve(self, url):                 
         

        from entertainment import istream
        resolved =istream.ResolveUrl(url)
        return resolved    









            
