'''
    9movies
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment.xgoogle.search import GoogleSearch

class onetwothree(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "9Movies"
    display_name = "9movies.to"
    base_url = 'http://fmovies.to/'
    
    source_enabled_by_default = 'true'

    
    def GetFileHosts(self, url, list, lock, message_queue, season, episode,type,year):

        from entertainment.net import Net
        import re
        net = Net(cached=False,user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')

        REF=url

        #print REF
        
        LINK=net.http_GET(url).content
        try:
            res=re.compile('class="quality">(.+?)<').findall(LINK)[0].strip().lower()
     
        except:
            res='HD'
      
        
        LINK=LINK.split('<ul class="episodes">')

        for p in LINK:
                   

            if type == 'tv_episodes':
                try:
                    if len(episode)<2:
                        episode = "0%s"%episode
                        
                    match = re.compile('data-id="(.+?)" href=".+?">(.+?)<',re.DOTALL).findall(p)
                    #print match
                    for id , episodes in match:
                        
                        if episode in episodes:
             

                            self.GRABLINKS(list,id,REF)                            
                except:pass
                
            else:
                try:
                    id = re.compile('data-id="(.+?)"').findall(p)[0]
                    res=res.replace('hd ','').replace('rip','HD')
                    res=res.upper().replace('HDHD','HD')
                    if not id in REF:
                        self.AddFileHost(list, res, id+'|'+REF,host='9MOVIES')
                except:pass                                        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net

        from entertainment import bing
        import re

        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)
        ##print ':::::::::::::::::::::::::::::::::'

        if type == 'tv_episodes':
            search_term ='%s %s' %(name,season)
            RESULT_TERM = '%s %s' %(name.lower(),season.lower())
            try:GOOGLED = self.GoogleSearch('fmovies.to', search_term)
            except:GOOGLED = bing.Search('fmovies.to', search_term)
            RETURN = 'watch %s' % RESULT_TERM.lower()
                      
           
        else:
            search_term = name + ' '+year
            RESULT_TERM = name.lower()           
            try:GOOGLED = self.GoogleSearch('fmovies.to', search_term)
            except:GOOGLED = bing.Search('fmovies.to', search_term)
                
            RETURN = 'watch %s' % RESULT_TERM.lower()
                      
        #print GOOGLED    
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']
       
            if '?' in movie_url:
                movie_url=movie_url.split('?')[0]
                
            #if not '/watching.html' in movie_url:
                #movie_url = movie_url + '/watching.html'
                #movie_url =movie_url.replace('//watching.html','/watching.html')

  
            if RETURN.lower() in TITLE.lower():
                if movie_url not in uniques:
                    if '/film/' in movie_url:
                        
                        
                        uniques.append(movie_url)
                        #match=re.compile('/film/(.+?)/(.+?)/').findall(movie_url)
                        #if match:
                        if not type == 'tv_episodes':
                            if year in TITLE:

                                self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                        else:
                                self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)




    def GRABLINKS(self,list, url,REF):

          
            from entertainment.net import Net
            import time,json,urllib,re

            net = Net(cached=False,user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')

        
            headers = {'X-Requested-With': 'XMLHttpRequest','Referer':REF+'/'+url}

            query = {'id': url, 'update': '0'}
            hello=self.__get_token(query)
            

            url = 'http://fmovies.to/ajax/episode/info?_token=%s&id=%s&update=0' % (hello,url)

            result = net.http_GET(url, headers=headers).content
            result = json.loads(result)
            #print result
            theparams = result['params']
            theparams['mobile'] = '1'
            TOKEN=self.__get_token(theparams)
            

            grabber='%s?_token=%s&token=%s&options=%s&mobile=1' % (result['grabber'],TOKEN,urllib.quote(theparams['token']),urllib.quote(theparams['options']))
            #print grabber
            headers = {'X-Requested-With': 'XMLHttpRequest','Referer':url}
            result = net.http_GET(grabber, headers=headers).content
            result = json.loads(result)
            #print result
            URL=[]
            STREAM=[]
            try:
                for i in result['data']:
                    res=i['label'].upper()
                    id=i['file']
                    final=id.split('//')[1]
                    HOST=final.split('/')[0].upper()
                    
                    self.AddFileHost(list, res, id,host=HOST)
            except:       
                    id=result['target']
                    FINAL=id.split('//')[1]
                    HOST=FINAL.split('/')[0]
                    
                    self.AddFileHost(list, '720p', id,host=HOST.upper())              


    def __get_token(self, data):
        n = 0
        for key in data:
            if not key.startswith('_'):
                for i, c in enumerate(data[key]):
                    n += ord(c) * (i + 1990)
        return hex(n)[2:]


            
    def Resolve(self, url):
            #print url
            import urllib
            
            if '|' in url:
                REF=url.split('|')[1]
                url=url.split('|')[0]
                
                from entertainment.net import Net
                import time,json,re

                net = Net(cached=False,user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')    
                
                headers = {'X-Requested-With': 'XMLHttpRequest','Referer':REF+'/'+url}

                query = {'id': url, 'update': '0'}
                hello=self.__get_token(query)
                
                #url = 'http://fmovies.to/ajax/film/episode?hash_id=%s&f=&p=%s' % (url, now.tm_hour + now.tm_min)
                url = 'http://fmovies.to/ajax/episode/info?_token=%s&id=%s&update=0' % (hello,url)
                #print url
                result = net.http_GET(url, headers=headers).content
                result = json.loads(result)
                #print result

                if 'error' in result:
                    return ''
               
                try:
                    theparams = result['params']
                    theparams['mobile'] = '1'
                    TOKEN=__get_token(theparams)

                    grabber='%s?_token=%s&token=%s&options=%s&mobile=1' % (result['grabber'],TOKEN,urllib.quote(theparams['token']),urllib.quote(theparams['options']))

                    headers = {'X-Requested-With': 'XMLHttpRequest','Referer':url}
                    result = net.http_GET(grabber, headers=headers).content
                    result = json.loads(result)
                    #print result
                    URL=[]
                    STREAM=[]
                    for i in result:
                        URL.append(i['label'].replace('p',''))

                  

                    r=max(URL)

                    for i in result:
                        if r in i['label']:
                            
                            STREAM.append(i['file'])

                    url=STREAM[0]

                    
                    if 'redirector' in url:

                          url = urllib.urlopen(url).geturl()

                          
                        
                    if 'requiressl=yes' in url: url = url.replace('http://', 'https://')
                    else: url = url.replace('https://', 'http://')
                except:
                    from entertainment import istream
                    url =result['target']
                    if url:
                        url = istream.ResolveUrl(url)
                    else:
                        url=''

            else:
                from entertainment import istream
                url = istream.ResolveUrl(url)                     
                                            
            return url
            
                
                
