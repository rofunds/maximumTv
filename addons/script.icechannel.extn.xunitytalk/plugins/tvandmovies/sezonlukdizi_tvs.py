'''
    http://afdah.com/    
    Copyright (C) 2013 Mikey1234
'''


from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment import common

import os


class sezonlukdizi(TVShowSource):
    implements = [TVShowSource]
    
    name = "sezonlukdizi"
    display_name = "Sezonlukdizi"
    search_url = 'http://sezonlukdizi.com/service/search?q=%s&_=%s'
    videourl='http://sezonlukdizi.com/service/get_video_part'
    cookie_file = os.path.join(common.cookies_path, 'sezon.cookie')
    source_enabled_by_default = 'false'
    icon = common.notify_icon
    
        
    def GetFileHosts(self, url, list, lock, message_queue,season,episode,showname):

        import re
        from entertainment.net import Net
        
        net = Net(cached=False)
                  
        new_url = url

        r='%s-sezon-%s' % (season,episode)
        #print new_url
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
                 'X-Requested-With': 'XMLHttpRequest',
                 'Host': 'sezonlukdizi.com'}
        
        content= net.http_GET(new_url,headers=headers).content
        match=re.compile('img alt="(.+?)".+?class="seep" href="(.+?)"',re.DOTALL).findall(content)
        for title , url in match:
       

            if showname.lower() in title.lower():
                
                if r in url:
                    page = net.http_GET(url,headers=headers).content
                    video_id = re.compile('var video_id.+?"(.+?)"').findall(page)[0]
                    part_name = re.compile('var part_name.+?"(.+?)"').findall(page)[0]
                    videourl='http://sezonlukdizi.com/service/get_video_part'

                    data = {'video_id': video_id, 'part_name': part_name,'page':'0'}
                    html=  net.http_POST(videourl,data,headers=headers).content
                    net.save_cookies(self.cookie_file)
                    import json

                    link= json.loads(html)
          
                    scriptpage=re.compile('src="(.+?)"').findall(str(link))[0]
                    contents= net.http_GET(scriptpage,headers=headers).content
                    contented=contents.split('{')
                    for p in contented:
                        try:
                            source =re.compile('file.+?"(.+?)"').findall(p)[0]
                            res =re.compile('label.+?"(.+?)"').findall(p)[0]
                            if res.endswith('p'):
                                self.AddFileHost(list, res.upper(), source+'|'+scriptpage,host='GOOGLEVIDEO.COM')
                        except:pass       
                        
            
        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
        
        from entertainment.net import Net
        import re,time,json

        net = Net(cached=False)
        name = self.CleanTextForSearch(name)

        search_term = name.lower()
        helper_term = ''
        ttl_extrctr = ''
        new_url=self.search_url % (search_term.replace(' ','+'),(str(int(time.time() * 1000))))
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
                 'X-Requested-With': 'XMLHttpRequest',
                 'Host': 'sezonlukdizi.com'}
        content= net.http_GET(new_url,headers=headers).content
        link = json.loads(content)
        for field in link:
            TITLE = field['name']
            URL = field['url']
            #print URL
            if name.lower() in TITLE.lower():
                    self.GetFileHosts(URL, list, lock, message_queue,season,episode,TITLE.lower())



    def Resolve(self, url):

        from entertainment.net import Net
        
        net = Net(cached=False)
        
        import re,urllib,requests


        ref=url.split('|')[1]
        url=url.split('|')[0]

        
        net.set_cookies(self.cookie_file)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
                 'X-Requested-With': 'XMLHttpRequest',
                 'Host': 'sezonlukdizi.com',
                 'Cookie':'ASPSESSIONIDCQSQCQDC=LHCFJCEDOMAAFLCBAEHCIHKE',
                 'Referer':str(ref)}

        r=requests.get(url, headers=headers,allow_redirects=False)

   

        return r.headers['location']+'|User-Agent=Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'+'&Referer=%s' % (urllib.quote(ref))    

