'''
    http://afdah.com/    
    Copyright (C) 2013 Mikey1234
'''


from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay import Plugin
from entertainment import common
from entertainment.xgoogle.search import GoogleSearch



class afdah(MovieSource):
    implements = [MovieSource]
    
    name = "afdah"
    display_name = "afdah"
    base_url = ['afdah.org', 'xmovies8.org', 'putlockerhd.co', 'genvideos.org']
    #img=''
    source_enabled_by_default = 'true'
    icon = common.notify_icon
    profile_path = common.profile_path
  
        
    def GetFileHosts(self, url, list, lock, message_queue,domain,s,ref):

        import re,urllib,requests
        from entertainment.net import Net
        
        net = Net(cached=False,user_agent='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5')


        loginurl = 'https://'+domain+'/video_info/iframe'
        
        v=url.split('v=')[1]
        data={'v': v}
        headers={'Host': domain,
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'https://'+domain,
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://'+url,
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.8'}

        first=s.post(loginurl,data=data, headers=headers ,allow_redirects=False, verify=False).content
        #first= net.http_POST(loginurl,data,headers).content

        import json

        link= json.loads(first)

        for j in link:
            if '360' in j:
                quality='SD'
            else:  quality=j
            
            THEURL = urllib.unquote(link[j])
            
            if 'url=' in THEURL:
                THEURL=THEURL.split('url=')[1]
                
            if not 'SD' in quality:
                quality=quality+'P'
                
            self.AddFileHost(list, quality, THEURL,host='GOOGLEVIDEO.COM')
        
        
        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
        
        from entertainment.net import Net
        import requests
        import re,random

        net = Net(cached=False)
        name = self.CleanTextForSearch(name)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        search_term = name.lower()
        helper_term = ''
        ttl_extrctr = ''

        s = requests.Session()
        
        domain=random.choice(self.base_url)
        new_url='https://'+domain+'/results?q='+name.replace(' ','+')
        content=s.get(new_url,headers=headers,allow_redirects=False, verify=False).content
        match=re.compile('title="(.+?)" href="(.+?)#').findall(content)
        for title , url in match:
            if name in title:
                if year in title:
                    movie_url = domain+url

                    self.GetFileHosts(movie_url, list, lock, message_queue,domain,s,new_url)



    def Resolve(self, url):

                   
        return url
