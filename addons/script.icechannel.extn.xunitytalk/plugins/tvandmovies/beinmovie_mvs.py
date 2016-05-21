'''
    Cartoon HD    
    Copyright (C) 2013 Mikey1234
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment import common
import os

class beinmovie(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "BeinMovie"
    display_name = "BeinMovie"
    base_url = 'https://beinmovie.com/'
   
    source_enabled_by_default = 'true'
    cookie_file = os.path.join(common.cookies_path, 'beinmovie.cookie')  
            
    
    def GetFileHosts(self, url, list, lock, message_queue):

        import re
        from entertainment.net import Net
        net = Net(cached=False,user_agent='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5')
     
     
        headers   ={'Host':'beinmovie.com',
                    'Referer':'https://beinmovie.com/'}

        net.set_cookies(self.cookie_file)
        
        content = net.http_GET(url,headers=headers).content
        #print content

        
        match=re.compile('movie-player/(.+?)"').findall(content)



        for URL  in match:
            net.set_cookies(self.cookie_file)
            getcontent = net.http_GET('https://beinmovie.com/movie-player.php?'+URL,headers=headers).content
            #print getcontent
            try:
                 FINAL_URL=re.compile('src="(.+?)"').findall(getcontent)[0]
            except:
                 FINAL_URL=re.compile("src='(.+?)'").findall(getcontent)[0]
       
            if len(FINAL_URL)< 8:
                grabsecond =  re.compile('movie-player/(.+?)"').findall(getcontent)[1]
                net.set_cookies(self.cookie_file)
                getcontent = net.http_GET('https://beinmovie.com/movie-player.php?'+grabsecond).content
                try: 
                    FINAL_URL=re.compile(' src="(.+?)"').findall(getcontent)[0]
                except: 
                    FINAL_URL=re.compile(" src='(.+?)'").findall(getcontent)[0]                
            if 'movie_lang=fr' in URL:
                language= 'French'
            elif 'movie_lang=en' in URL:
                language= 'English'
            else:language=''    
            self.AddFileHost(list, '1080P', FINAL_URL,host='GOOGLEVIDEO - '+language)
        
        
        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
        
        from entertainment.net import Net
        import re
        net = Net(cached=False,user_agent='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5')
        name = self.CleanTextForSearch(name)

        
        content=net.http_GET('https://beinmovie.com').content

        net.save_cookies(self.cookie_file)
        main_url='https://beinmovie.com/movies-list.php?b=search&v=' + name.replace(' ','+')
        
        headers   ={'Host':'beinmovie.com',
                    'Referer':'https://beinmovie.com/'}

        net.set_cookies(self.cookie_file)
        content=net.http_GET(main_url,headers=headers).content
        
        match=re.compile('#!movie-detail/id=(.+?)/').findall (content)
        for id in match: 
            item_url='https://beinmovie.com/movie-detail.php?id='+id
            self.GetFileHosts(item_url, list, lock, message_queue)
              

    def GrabMailRu(self,url,list):
        print 'RESOLVING VIDEO.MAIL.RU VIDEO API LINK'
        
        
        from entertainment.net import Net
        net = Net(cached=False)

        
        import json,re
        items = []

        data = net.http_GET(url).content
        cookie = net.get_cookies()
        
        for x in cookie:
             if '.my.mail.ru' in x: 
                 for y in cookie[x]:
                      for z in cookie[x][y]:
                           l= (cookie[x][y][z])
                       
        r = '"key":"(.+?)","url":"(.+?)"'
        match = re.compile(r,re.DOTALL).findall(data)
        for quality,stream in match:
            test = str(l)
            test = test.replace('<Cookie ','')
            matcher =re.compile('for (.+?)>').findall(test)[0]
            test = test.replace(' for '+matcher+'>','')
            url=stream +'|Cookie='+test
            Q=quality.upper()
            if Q == '1080P':
                Q ='1080P'
            elif Q == '720P':
                Q ='720P'                
            elif Q == '480P':
                Q ='HD'
            else:
                Q ='SD'     
            self.AddFileHost(list, Q, url,host='MAIL.RU')  

             

    def Resolve(self, url):                 
        print '############################' +url
        if 'mail.ru' in url:
            resolved = url
        if 'googleusercontent.com' in url:
            import urllib
            page = urllib.urlopen(url)
            resolved=page.geturl()
            
        elif 'googlevideo.com' in url:
            resolved =url
        else:
        
            from entertainment import istream
            resolved =istream.ResolveUrl(url)
        return resolved    









            
