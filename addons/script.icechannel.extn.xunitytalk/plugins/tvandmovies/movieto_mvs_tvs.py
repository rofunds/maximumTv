'''
    Istream
    Scenelog.org
    Copyright (C) 2013 Coolwave, Jas0npc, the-one, voinage

    version 0.2

'''


from entertainment.plugnplay import Plugin
from entertainment import common
from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
import os




class movieto(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
	
    #unique name of the source
    name = "movie.to"
    source_enabled_by_default = 'true'
    #display name of the source
    display_name = "MovieTo"
    
    #base url of the source website
    base_url = 'http://movietv.to/'
    cookie_file = os.path.join(common.cookies_path, 'movietvto.cookie')

    
    def GetFileHosts(self, url, list, lock, message_queue,ref):

            self.AddFileHost(list, '720P', url+'|'+ref,host='MOVIE.TO')



    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):

        import urllib2
        import re,time
        from entertainment.net import Net

        net = Net(cached=False,user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36')
        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)


        wait=False
        new_url='http://movietv.to/index/loadmovies'
        if type == 'tv_episodes':
            types='tv'
            r='href="/series/(.+?)".+?movie-title">(.+?)</h2>'
            NEW='http://movietv.to/series/'
        else:
            types='movie'
            r='href="/movies/(.+?)".+?movie-title">(.+?)</h2>'
            NEW='http://movietv.to/movies/'
           
            
        gettoken=net.http_GET('http://movietv.to/movies').content
        print 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'

        net.save_cookies(self.cookie_file)

        aa=open(self.cookie_file).read()
        cfduid=re.compile('Set-Cookie3: __cfduid=(.+?); path="/"; domain=".movietv.to"').findall(aa)[0]

        token=re.compile('token_key="(.+?)"').findall(gettoken)[0]

        TIME = time.time()
  
        TIME= str(TIME).split('.')[0]

        data={'loadmovies':'showData','page':'1','abc':'All','genres':'','sortby':'Popularity','quality':'All','type':types,'q':name,'token':token}
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
                 'Referer':NEW,
                 'Origin': 'http://movietv.to',
                 'Connection': 'keep-alive',
                 'Pragma':'no-cache',
                 'Cache-Control': 'no-cache',
                 'Accept': '*/*',
                 'X-Requested-With': 'XMLHttpRequest',
                 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.8'}
        
        net.set_cookies(self.cookie_file)
        content=net.http_POST(new_url,data,headers=headers).content
        
       
        match=re.compile(r,re.DOTALL).findall (content)

        for URL , TITLE in match:

                if name.lower() in TITLE.lower():
                    if type == 'tv_episodes':
                        id=URL.split('-')[0]
                                 
                        LINKURL='http://movietv.to/series/getLink?id=5028&s=5&e=7&token=%s&_=%s' % (token,TIME)
                        contents=net.http_GET(LINKURL,headers).content
                        import json
                        match=json.loads(contents)['url']
                        

                    else:
                        
                        contents=net.http_GET(NEW+URL,headers).content
                        
                        match=re.compile('<source src="(.+?)" type=\'video/mp4\'>').findall(contents)[0]
                    
                    self.GetFileHosts(match, list, lock, message_queue,URL)

                    

    def Resolve(self, url):
        import re
        import urllib
        
        ref=url.split('|')[1]
        url=url.split('|')[0].replace('310','999')
        #url=url.split('&end')[0]

        HOST=url.split('//')[1]
        HOST=HOST.split('/')[0]
        
        #cookie = match=re.compile('__cfduid=(.+?);').findall(open(self.cookie_file).read())[0]
        
        url += "|Referer=http://movietv.to/movies/"+ref+"&Host="+HOST+"&Connection=keep-alive"
        return url.replace('\\','')
                                
