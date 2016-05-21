'''
    Ice Channel
    buzzfilms.co
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment.xgoogle.search import GoogleSearch

class xmovies(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "XMovies8"
    display_name = "XMovies8"
    base_url = 'http://xmovies8.tv'
    
    source_enabled_by_default = 'true'

    
    def GetFileHosts(self, url, list, lock, message_queue, season, episode,type,year):

        from entertainment.net import Net
        import re,json
        net = Net(cached=False)

        #print url



        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        
        ##print html.encode('ascii','ignore')
        if type == 'tv_episodes':
 
            URL = url.split('xmovies8.tv/movie/')[1]
            URL = URL.split('/')[0]
            data={'mx':URL,
                  'isseries':'1',
                  'part':'0'}

            
            html = net.http_POST('http://xmovies8.tv/lib/picasa.php',data,headers=headers).content
            match=re.compile('part_id=(.+?)">(.+?)</a>').findall(html)
            if not match:
     
                
                URL = url.split('xmovies8.tv/movie/')[1]
                URL = 'watch-'+URL.split('/')[0]
                data={'mx':URL,
                      'isseries':'1',
                      'part':'0'}
                
                html = net.http_POST('http://xmovies8.tv/lib/picasa.php',data,headers=headers).content          
                match=re.compile('part_id=(.+?)">(.+?)</a>').findall(html)
            
            for partid , ep in match:
                if episode ==ep:
                                            
                    data={'mx':URL,
                          'isseries':'1',
                          'part':partid}
                    #print data
                    HTML = net.http_POST('http://xmovies8.tv/lib/picasa.php',data,headers=headers).content
                    #print HTML.encode('ascii','ignore')
                    try:
                        URL = re.compile('docid=(.+?)&').findall(HTML)[0]
                        html = net.http_GET('https://docs.google.com/file/d/%s/preview'%URL,headers=headers).content
                        result = re.compile('"fmt_stream_map",(".+?")').findall(html)[0]
                        
                        result = json.loads(result)
                        result = [i.split('|')[-1] for i in result.split(',')]
                        result = sum([self.googletag(i) for i in result], [])
                        
                        for a in result:
                            FINAL_URL = a['url']
                            host=FINAL_URL.split('//')[1]
                            HOST=host.split('/')[0]                    
                            res = a['quality']
                            self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())                       
                    except:    
                        FINAL_URL = re.compile('webkitallowfullscreen=".+?" src="(.+?)"').findall(HTML)[0]
                        #print FINAL_URL
                        host=FINAL_URL.split('//')[1]
                        HOST=host.split('/')[0]
                        res='720P'
                         
                        self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())  
        else:
            
            html = net.http_GET(url,headers=headers).content            
            
            try:
                URL = re.compile('docid=(.+?)&').findall(html)[0]
                html = net.http_GET('https://docs.google.com/file/d/%s/preview'%URL,headers=headers).content
                result = re.compile('"fmt_stream_map",(".+?")').findall(html)[0]
                
                result = json.loads(result)
                result = [i.split('|')[-1] for i in result.split(',')]
                result = sum([self.googletag(i) for i in result], [])
                
                for a in result:
                    FINAL_URL = a['url']
                    host=FINAL_URL.split('//')[1]
                    HOST=host.split('/')[0]                    
                    res = a['quality']
                    self.AddFileHost(list, res, FINAL_URL,host=HOST.upper()) 
            
            except:    
                FINAL_URL = re.compile('webkitallowfullscreen=".+?" src="(.+?)"').findall(html)[0]
                #print FINAL_URL
                host=FINAL_URL.split('//')[1]
                HOST=host.split('/')[0]
                res='720P'
                 
                self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())                    

                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net
        from entertainment import bing


        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)
        ##print ':::::::::::::::::::::::::::::::::'

        if type == 'tv_episodes':
            search_term ='%s Season %s' %(name,season)
            try:GOOGLED = self.GoogleSearch('xmovies8.tv', search_term)
            except:GOOGLED = bing.Search('xmovies8.tv', search_term)        
           
        else:
            search_term = name + ' '+year
            RESULT_TERM = name.lower()           
            try:GOOGLED = self.GoogleSearch('xmovies8.tv', search_term)
            except:GOOGLED = bing.Search('xmovies8.tv', search_term)            
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']

            if type == 'tv_episodes':
                if 'xmovies8.tv' in movie_url.lower():
                    if name.lower() in TITLE.lower():
                        if 'season '+season in TITLE.lower():
                            if movie_url not in uniques:
                                uniques.append(movie_url)               
                                self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                                break
            else:
                if 'xmovies8.tv' in movie_url.lower():
                    if name.lower() in TITLE.lower():
                       
                        if year in TITLE.lower():
                            if movie_url not in uniques:
                                uniques.append(movie_url)
                 
                                self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                                break

    def googletag(self,url):
        import re
        quality = re.compile('itag=(\d*)').findall(url)
        quality += re.compile('=m(\d*)$').findall(url)
        try: quality = quality[0]
        except: return []

        if quality in ['37', '137', '299', '96', '248', '303', '46']:
            return [{'quality': '1080P', 'url': url}]
        elif quality in ['22', '84', '136', '298', '120', '95', '247', '302', '45', '102']:
            return [{'quality': '720P', 'url': url}]
        elif quality in ['35', '44', '135', '244', '94']:
            return [{'quality': 'SD', 'url': url}]
        elif quality in ['18', '34', '43', '82', '100', '101', '134', '243', '93']:
            return [{'quality': 'SD', 'url': url}]
        elif quality in ['5', '6', '36', '83', '133', '242', '92', '132']:
            return [{'quality': 'SD', 'url': url}]
        else:
            return []

    
    def Resolve(self, url):
        if 'http' in url:
            from entertainment import istream
            url =istream.ResolveUrl(url)
        else:

            
            return url
            
                
                
