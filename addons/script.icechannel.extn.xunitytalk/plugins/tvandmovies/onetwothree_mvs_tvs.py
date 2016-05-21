'''
    Ice Channel
    buzzfilms.co
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment.xgoogle.search import GoogleSearch
from entertainment import common
import os

class onetwothree(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "123Movies"
    display_name = "123Movies"
    base_url = 'http://123movies.to/'

    UA ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    
    profile_path = common.profile_path
    cookie_file = os.path.join(profile_path, 'cookies', '%s.cookies') % name
    
    source_enabled_by_default = 'true'

    
    def GetFileHosts(self, url, list, lock, message_queue, season, episode,type,year):

        from entertainment.net import Net
        from entertainment import cloudflare
        import re
        net = Net(cached=False)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        try:
            LINK = net.http_GET(url,headers=headers).content
            net.save_cookies(self.cookie_file)
            print '##########################'
            print 'NET'             
        except:LINK = cloudflare.solve(url,self.cookie_file,self.UA,'8')
        
        try:movie_id = re.compile('movie-id="(.+?)"').findall(LINK)[0]
        except:movie_id = re.compile('updateMovieView\((.+?)\)').findall(LINK)[0]
        #token = re.compile('hash="(.+?)"').findall(LINK)[0]
        net.set_cookies(self.cookie_file)
        LOAD =net.http_GET('http://123movies.to/movie/loadepisodes/'+movie_id,headers=headers).content
        link=LOAD.split('<div id="server-')
        for p in link:
            #try:
                host= p.split('"')[0]
                res ='720P'
                if len(host)<2:
                    

                    if type == 'tv_episodes':

                            HTML=p.split('<a title="')
                            
                            for d in HTML:
                                try:                                
                                    if 'episode '+episode in d.lower() or 'episode '+episode+':' in d.lower():
                                        token = re.compile('hash="(.+?)"').findall(d)[0]
                                        SERVER=d.split('loadEpisode(')[1]
                                        server=SERVER.split(',')[0]
                                        episodeid=re.compile(',(.+?),').findall(SERVER)[0]
                                        URL='http://123movies.to/movie/load_episode/%s/%s' % (episodeid,token)
                                        net.set_cookies(self.cookie_file)
                                        HTML1=net.http_GET(URL,headers=headers).content
                                    
                                        
                                        
                                        try:
                                            match=re.compile('file="(.+?)".+?label="(.+?)"',re.DOTALL).findall(HTML1)
                                            for FINAL_URL , res in match:
                                                
                                                if 'google' in FINAL_URL or 'blogspot' in FINAL_URL or '123movies.to' in FINAL_URL:                             
                                                    if not '.srt' in FINAL_URL:
                                                        res=res.replace('p','')
                                                        if not res.isdigit():
                                                            res='720'
                                                        #print res
                                                        res=int(res)
                                                        #print res
                                                        if res < 400:
                                                            res='SD'
                                                        elif (res > 400) and (res< 500):
                                                            res='HD'
                                                        elif (res > 500) and (res< 721):
                                                            res='720P'                                            
                                                        else:res='1080P'

                                                        HOST=FINAL_URL.split('//')[1]
                                                        HOST=HOST.split('/')[0]  
                                                        

                                                        

                                                        self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())                              
                                        except:pass
                                except:pass                                    
                    else:
                            HTML=p.split('<a title="')
                            
                            for d in HTML:
                                try:                                
                                    YEAR=re.compile('Release:</strong>(.+?)<').findall(LINK)[0].strip()
                                    token = re.compile('hash="(.+?)"').findall(d)[0]
                                    SERVER=d.split('loadEpisode(')[1]
                                    server=SERVER.split(',')[0]
                                    episodeid=re.compile(',(.+?),').findall(SERVER)[0]
                    
                                    URL='http://123movies.to/movie/load_episode/%s/%s' % (episodeid,token)                            
                                    if year == YEAR:
                                        net.set_cookies(self.cookie_file)
                                        HTML=net.http_GET(URL,headers=headers).content
                                        try:  
                                            match=re.compile('file="(.+?)".+?label="(.+?)"',re.DOTALL).findall(HTML)
                                            for FINAL_URL , res in match:
                                                
                                                if 'google' in FINAL_URL or 'blogspot.com' in FINAL_URL or '123movies.to' in FINAL_URL:
                                                    
                                                    if not '.srt' in FINAL_URL:
                                                        res=res.replace('p','')
                                                        res=int(res)
                                                        #print res
                                                        if res < 400:
                                                            res='SD'
                                                        elif (res > 400) and (res< 500):
                                                            res='HD'
                                                        elif (res > 500) and (res< 720):
                                                            res='720P'                                            
                                                        else:res='1080P'
                                                        
                                                        HOST=FINAL_URL.split('//')[1]
                                                        HOST=HOST.split('/')[0]  

                                            
                                                        self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())
                                        except:pass
                                except:pass                                        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net

        from entertainment import bing

        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)
        #print ':::::::::::::::::::::::::::::::::'

        if type == 'tv_episodes':
            search_term ='%s Season %s' %(name,season)
            RESULT_TERM = '%s - season %s' %(name.lower(),season.lower())
            try:GOOGLED = self.GoogleSearch('123movies.to', search_term)
            except:GOOGLED = bing.Search('123movies.to', search_term)
            
                      
           
        else:
            search_term = name + ' '+year
            RESULT_TERM = name.lower()           
            try:GOOGLED = self.GoogleSearch('123movies.to', search_term)
            except:GOOGLED = bing.Search('123movies.to', search_term)
            
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']
       
            if '?' in movie_url:
                movie_url=movie_url.split('?')[0]
                
            if not '/watching.html' in movie_url:
                movie_url = movie_url + '/watching.html'
                movie_url =movie_url.replace('//watching.html','/watching.html')

                
    
                
            RETURN = 'watch %s for free on' % RESULT_TERM.lower()
            RETURN_TWO  = '%s - watch movies online free' % RESULT_TERM.lower()

            if RETURN.lower() in TITLE.lower() or RETURN_TWO in TITLE.lower():
                if movie_url not in uniques:
                    uniques.append(movie_url)
                    movie_url=movie_url.replace('/tags/','film/')
              
                    self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                    break
            
    def Resolve(self, url):
                
        if 'google' in url:
            return url
        elif 'blogspot' in url:    
            return url
        else:
            from entertainment import istream
            return istream.ResolveUrl(url)
            
                
                
