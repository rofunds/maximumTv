'''
    Istream
    trakt by Coolwave
    Copyright (C) 2013 

    version 0.1

'''


from entertainment.plugnplay import Plugin
from entertainment import common
from entertainment.plugnplay.interfaces import MovieIndexer
from entertainment.plugnplay.interfaces import CustomSettings
from entertainment.plugnplay.interfaces import TVShowIndexer
from entertainment.xgoogle.search import GoogleSearch

import re

class trakt(MovieIndexer,TVShowIndexer,CustomSettings):
    implements = [MovieIndexer,TVShowIndexer,CustomSettings]

    name = "trakt"
    default_indexer_enabled = 'false'
    display_name = "[COLOR royalblue]T[/COLOR][COLOR white]rakt[/COLOR]"
    img='https://raw.githubusercontent.com/Coolwavexunitytalk/images/master/trakt.png'
    
    #base url of the source website
    base_url = 'http://www.movie25.hk/'
    base_url_api = 'http://services.tvrage.com/myfeeds/'
    base_url_tv = 'http://www.tvrage.com/'
    api = 'ag6txjP0RH4m0c8sZk2j'
    trakt_api_url = 'http://api.trakt.tv/'
    traki_url = 'https://trakt.tv/'
    traki_api = '18a6532a12a81d0f18bc25a158e5e4e9'
    base_url_tvrage_48hours = 'http://services.tvrage.com/feeds/last_updates.php?hours=48'

    def __init__(self):
        xml = '<settings>\n'
        xml += '<category label="Account">\n'
        xml += '<setting id="enable_trakt" type="bool" label="Enable Trakt Watchlist:" default="false" />\n'
        xml += '<setting id="username" type="text" label="Trakt Username:" default="Enter your trakt username" enable="eq(-1,true)" />\n'
        xml += '</category>\n' 
        xml += '</settings>\n'
        self.CreateSettings(self.name, self.display_name, xml)    
    
    def ExtractContentAndAddtoList(self, indexer, section, url, type, list, page='', total_pages='', sort_by='', sort_order=''):
        
        if section == 'popular':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/popular?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'popular', '', type, str(page), total_pages)
        
            match=re.compile('data-type="movie" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<div class="titles"><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)


        elif section == 'boxoffice':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/boxoffice?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '1'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'boxoffice', '', type, str(page), total_pages)
        
            match=re.compile('data-type="movie" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)

        elif section == 'populartv':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/popular?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'populartv', '', type, str(page), total_pages)
        
            match=re.compile('data-type="show" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<div class="titles"><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_Content, name+ '[COLOR royalblue] (' + year +')[/COLOR]', '', 'tv_seasons', url=url, name=name, year=year)

        elif section == 'populareps':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://thewatchseries.to/new/'+page
                
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            html = net.http_GET(new_url).content
            total_pages = '9'
            
            self.AddInfo(list, indexer, 'populareps', '', type, str(page), total_pages)
            
            match=re.compile('<li><a href="(.+?)">(.+?) Seas. (.+?) Ep. (.+?) .+?<').findall(html)
            for url, name, Sea_num, eps_num in match:
                
                name = self.CleanTextForSearch(name)
                #url = self.tv_calender_url
                season_pull = "0%s"%Sea_num if len(Sea_num)<2 else Sea_num
                episode_pull = "0%s"%eps_num if len(eps_num)<2 else eps_num
                sea_eps = 'S'+season_pull+'E'+episode_pull
                year= '0'

                item_id = common.CreateIdFromString(name + '_' + year + '_season_' + Sea_num + '_episode_' + eps_num)

                self.AddContent(list, indexer, common.mode_File_Hosts, name +'[COLOR royalblue] ('+sea_eps+')[/COLOR]', item_id, 'tv_episodes', url=url, name=name, year=year, season=Sea_num, episode=eps_num)

        elif section == 'latesttv':
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://thewatchseries.to/latest/'+page
                
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            html = net.http_GET(new_url).content
            total_pages = '9'
            
            self.AddInfo(list, indexer, 'latesttv', '', type, str(page), total_pages)
            
            match=re.compile('<li><a href="(.+?)">(.+?) Seas. (.+?) Ep. (.+?) .+?<').findall(html)
            for url, name, Sea_num, eps_num in match:
                
                name = self.CleanTextForSearch(name)
                #url = self.tv_calender_url
                season_pull = "0%s"%Sea_num if len(Sea_num)<2 else Sea_num
                episode_pull = "0%s"%eps_num if len(eps_num)<2 else eps_num
                sea_eps = 'S'+season_pull+'E'+episode_pull
                year= '0'

                item_id = common.CreateIdFromString(name + '_' + year + '_season_' + Sea_num + '_episode_' + eps_num)

                self.AddContent(list, indexer, common.mode_File_Hosts, name +'[COLOR royalblue] ('+sea_eps+')[/COLOR]', item_id, 'tv_episodes', url=url, name=name, year=year, season=Sea_num, episode=eps_num)

        elif section == 'trending':
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/trending?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'trending', '', type, str(page), total_pages)
        
            match=re.compile('data-type="movie" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<div class="titles"><h4>.+?</h4><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)

        elif section == 'trendingtv':
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/trending?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'trendingtv ', '', type, str(page), total_pages)
        
            match=re.compile('data-type="show" data-url="(.+?)"><a href=".+?">.+?<div class="titles"><h4>.+?</h4><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url = 'http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_Content, name+ '[COLOR royalblue] (' + year +')[/COLOR]', '', 'tv_seasons', url=url, name=name, year=year)

        elif section == 'anticipated':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/anticipated?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '400'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'anticipated', '', type, str(page), total_pages)
        
            match=re.compile('data-type="movie" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)

        elif section == 'watched':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/watched/weekly?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'watched', '', type, str(page), total_pages)
        
            match=re.compile('data-type="movie" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<div class="titles"><h4>.+?</h4><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)

        elif section == 'watchedtv':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/watched/weekly?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'watchedtv ', '', type, str(page), total_pages)
        
            match=re.compile('data-type="show" data-url="(.+?)"><a href=".+?">.+?<div class="titles"><h4>.+?</h4><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url = 'http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_Content, name+ '[COLOR royalblue] (' + year +')[/COLOR]', '', 'tv_seasons', url=url, name=name, year=year)

        elif section == 'watchedeps':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/watchers/daily/'+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            
            self.AddInfo(list, indexer, 'watchedeps', '', type, str(page), total_pages)
        
            match=re.compile('<div class="title-overflow"></div>.+?<a href=".+?">(.+?)</a>.+?<div class="title-overflow"></div>.+?<a href="(.+?)">.+?<span>(.+?)x(.+?)</span>',re.DOTALL).findall(html)
            for name, url, Sea_num, eps_num in match:
                name = self.CleanTextForSearch(name)
                url = 'http://services.tvrage.com/myfeeds/search.php?key=ag6txjP0RH4m0c8sZk2j&show='+name
                season_pull = "0%s"%Sea_num if len(Sea_num)<2 else Sea_num
                episode_pull = "0%s"%eps_num if len(eps_num)<2 else eps_num
                sea_eps = 'S'+season_pull+'E'+episode_pull
                year= '0'

                item_id = common.CreateIdFromString(name + '_' + year + '_season_' + Sea_num + '_episode_' + eps_num)

                self.AddContent(list, indexer, common.mode_File_Hosts, name +'[COLOR royalblue] ('+sea_eps+')[/COLOR]', item_id, 'tv_episodes', url=url, name=name, year=year, season=Sea_num, episode=eps_num)


        elif section == 'played':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/played?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'played', '', type, str(page), total_pages)
        
            match=re.compile('data-type="movie" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)

        elif section == 'playedtv':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/played/weekly'+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'playedtv ', '', type, str(page), total_pages)
        
            match=re.compile('data-type="show" data-url="(.+?)"><a href=".+?">.+?<div class="titles"><h4>.+?</h4><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url = 'http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_Content, name+ '[COLOR royalblue] (' + year +')[/COLOR]', '', 'tv_seasons', url=url, name=name, year=year)

        elif section == 'collectedtv':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/collected/weekly'+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'collectedtv ', '', type, str(page), total_pages)
        
            match=re.compile('data-type="show" data-url="(.+?)"><a href=".+?">.+?<div class="titles"><h4>.+?</h4><h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url = 'http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_Content, name+ '[COLOR royalblue] (' + year +')[/COLOR]', '', 'tv_seasons', url=url, name=name, year=year)
                
        elif section == 'playedeps':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/episodes/plays/daily/'+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            
            self.AddInfo(list, indexer, 'playedeps', '', type, str(page), total_pages)
        
            match=re.compile('<div class="title-overflow"></div>.+?<a href=".+?">(.+?)</a>.+?<div class="title-overflow"></div>.+?<a href="(.+?)">.+?<span>(.+?)x(.+?)</span>',re.DOTALL).findall(html)
            for name, url, Sea_num, eps_num in match:
                name = self.CleanTextForSearch(name)
                url = 'http://services.tvrage.com/myfeeds/search.php?key=ag6txjP0RH4m0c8sZk2j&show='+name
                season_pull = "0%s"%Sea_num if len(Sea_num)<2 else Sea_num
                episode_pull = "0%s"%eps_num if len(eps_num)<2 else eps_num
                sea_eps = 'S'+season_pull+'E'+episode_pull
                year= '0'

                item_id = common.CreateIdFromString(name + '_' + year + '_season_' + Sea_num + '_episode_' + eps_num)

                self.AddContent(list, indexer, common.mode_File_Hosts, name +'[COLOR royalblue] ('+sea_eps+')[/COLOR]', item_id, 'tv_episodes', url=url, name=name, year=year, season=Sea_num, episode=eps_num)



        elif section == 'release':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/released/'+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            
            self.AddInfo(list, indexer, 'release', '', type, str(page), total_pages)
        
            match=re.compile('<a class="title" href="(.+?)">(.+?) \((.+?)\)</a>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name)
                name = name.replace('$','s')
                url = 'http://services.tvrage.com/myfeeds/search.php?key=ag6txjP0RH4m0c8sZk2j&show='+name
                self.AddContent(list, indexer, common.mode_File_Hosts, name + ' (' + year +')', '', type, '', name, year)

        elif section == 'trakt_title':
            
            new_url = url
                                        
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            match=re.compile('<img class="poster-art" alt="(.+?) \((.+?)\)"').findall(html)
            if 'No items in this list yet!' in html:
                    self.AddContent(list, indexer, common.mode_File_Hosts, 'No items in this list yet!', '', type, '', '', '')            
            
            ''' Pagination Code Start '''
            num_items_on_a_page = 25
            if page == '':                
                page = '1'
                total_items = len(match)
                total_pages = str ( ( total_items / num_items_on_a_page ) + ( 1 if total_items % num_items_on_a_page >= 1 else 0) )
                
            self.AddInfo(list, indexer, section, url, type, page, total_pages, sort_by, sort_order)
            
            start_index = ( int(page) - 1 ) * num_items_on_a_page
            match = match[ start_index : start_index + num_items_on_a_page  ]
            ''' Pagination Code End '''
        
            
            for name, year in match:
                name = self.CleanTextForSearch(name)
                name = name.replace('$','s')
                url = 'http://services.tvrage.com/myfeeds/search.php?key=ag6txjP0RH4m0c8sZk2j&show='+name
                self.AddContent(list, indexer, common.mode_File_Hosts, name + ' (' + year +')', '', type, '', name, year)

        elif section == 'trakt_official':
            
            new_url = url

            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            match=re.compile('data-title="(.+?) \((.+?)\)"').findall(html)
                      
            
            ''' Pagination Code Start '''
            num_items_on_a_page = 25
            if page == '':                
                page = '1'
                total_items = len(match)
                total_pages = str ( ( total_items / num_items_on_a_page ) + ( 1 if total_items % num_items_on_a_page >= 1 else 0) )
                
            self.AddInfo(list, indexer, section, url, type, page, total_pages, sort_by, sort_order)
            
            start_index = ( int(page) - 1 ) * num_items_on_a_page
            match = match[ start_index : start_index + num_items_on_a_page  ]
            ''' Pagination Code End '''
        
            
            for name, year in match:
                name = self.CleanTextForSearch(name)
                name = name.replace('$','s')
                url = 'http://trakt.tv'
                self.AddContent(list, indexer, common.mode_File_Hosts, name + ' (' + year +')', '', type, '', name, year)

        elif section == 'trakt_personal':
            
            new_url = url
                                        
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            match=re.compile('<a class="title" href="(.+?)">(.+?) \((.+?)\)</a>').findall(html)
                      
            
            ''' Pagination Code Start '''
            num_items_on_a_page = 25
            if page == '':                
                page = '1'
                total_items = len(match)
                total_pages = str ( ( total_items / num_items_on_a_page ) + ( 1 if total_items % num_items_on_a_page >= 1 else 0) )
                
            self.AddInfo(list, indexer, section, url, type, page, total_pages, sort_by, sort_order)
            
            start_index = ( int(page) - 1 ) * num_items_on_a_page
            match = match[ start_index : start_index + num_items_on_a_page  ]
            ''' Pagination Code End '''
        
            
            for url2,name, year in match:
                name = self.CleanTextForSearch(name)
                name = name.replace('$','s')
                url = 'http://trakt.tv'+url2
                self.AddContent(list, indexer, common.mode_File_Hosts, name + ' (' + year +')', '', type, '', name, year)

        elif section == 'collected':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/collected/weekly?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '400'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'collected', '', type, str(page), total_pages)
        
            match=re.compile('data-type="movie" data-url="(.+?)"><a href=".+?"><div class="fanart">.+?<h3>(.+?) <span class="year">(.+?)</span></h3>').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)

        elif section == 'populartvgenre':
            section = url.replace('http://trakt.tv/shows/popular/','')
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/shows/popular/'+section+'/'+ page
                                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'populartvgenre', url, type, str(page), total_pages)
        
            match=re.compile('data-url="(.+?)">.+?class="titles"><h3>(.+?)<').findall(html)
            for url, name in match:
                name = self.CleanTextForSearch(name)
                name = name.replace('$','s')
                url = 'http://services.tvrage.com/myfeeds/search.php?key=ag6txjP0RH4m0c8sZk2j&show='+name
                self.AddContent(list, indexer, common.mode_Content, name, '', 'tv_seasons', url=url, name=name)

        elif section == 'trakt_watchlisttv':
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            import json
            response = net.http_GET(url).content
            match = json.loads(response)
            
            ''' Pagination Code Start '''
            num_items_on_a_page = 25
            if page == '':                
                page = '1'
                total_items = len(match)
                total_pages = str ( ( total_items / num_items_on_a_page ) + ( 1 if total_items % num_items_on_a_page >= 1 else 0) )
                
            self.AddInfo(list, indexer, section, url, type, page, total_pages, sort_by, sort_order)
            
            start_index = ( int(page) - 1 ) * num_items_on_a_page
            match = match[ start_index : start_index + num_items_on_a_page  ]
            ''' Pagination Code End '''
            
            for shows in match:
                name = shows['title']
                if name:
                    name = name.encode('utf8')
                    year = str(shows['year'])
                    name = self.CleanTextForSearch(name)
                    name = name.replace('$','s')
                    url = 'http://services.tvrage.com/myfeeds/search.php?key=ag6txjP0RH4m0c8sZk2j&show='+name
                    self.AddContent(list, indexer, common.mode_Content, name, '', 'tv_seasons', url=url, name=name, year=year)

        elif section == 'calendar':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/calendars/shows/'+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            print html.encode('utf-8')
            total_pages = '446'
            
            self.AddInfo(list, indexer, 'calendar', '', type, str(page), total_pages)
        
            match=re.compile('data-url=".+?"><a href="(.+?)">.+?<div class="titles"><h4> (.+?) am on (.+?)</h4><h3><span class=\'main-title-sxe\'>(.+?)x(.+?)</span>(.+?)</h3>',re.DOTALL).findall(html)
            for url,time, network, Sea_num, eps_num, title in match:
                name = url.split('/shows/')[1]
                name = name.split('/season/')[0]
                name = name.replace('-',' ')
                name = name.title()
                name = self.CleanTextForSearch(name)
                url = 'http://services.tvrage.com/myfeeds/search.php?key=ag6txjP0RH4m0c8sZk2j&show='+name
                season_pull = "0%s"%Sea_num if len(Sea_num)<2 else Sea_num
                episode_pull = "0%s"%eps_num if len(eps_num)<2 else eps_num
                sea_eps = 'S'+season_pull+'E'+episode_pull
                year= '0'

                item_id = common.CreateIdFromString(name + '_' + year + '_season_' + Sea_num + '_episode_' + eps_num)

                self.AddContent(list, indexer, common.mode_File_Hosts, name +'[COLOR royalblue] ('+sea_eps+')[/COLOR] Time: [COLOR red]'+time+'[/COLOR] On [COLOR red]'+network+'[/COLOR]', item_id, 'tv_episodes', url=url, name=name, year=year, season=Sea_num, episode=eps_num)

        elif section == 'network_title':
            import re
            #url = url.replace(' ','+')
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = new_url + '/page'+page+'/'
            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            url = urllib.unquote_plus(url)
            new_url = url.rpartition('/')[0]
            new_url = new_url+'/'
            html = net.http_GET(new_url+'page'+str(page)+'/').content

            if total_pages == '':
                #lastlist = url
                r= '>([0-9]*)</a>\s*<a href=".+?" class="next">' #% lastlist
                total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'network_title', url, type, str(page), total_pages)
            
            match=re.compile('<div class="mask"><a href=".+?"><img src=".+?" alt="(.+?)"/></a></div>.+?<div class="_clear"></div>\s*<div class="airtime">(.+?)</div>',re.DOTALL).findall(html)
            for name, netw in match:
                name = self.CleanTextForSearch(name)
                name2 = name.replace(' ','-').replace('\'','-').replace('.','-').replace(':','').replace('&-','')
                url = 'http://trakt.tv/shows/'+name2
                netw = netw.split('<')[0]
                netw = '[COLOR red]'+netw+'[/COLOR]'
                self.AddContent(list, indexer, common.mode_Content, name+ ' (' + netw.replace('(','').replace(')','') +')', '', 'tv_seasons', url=url, name=name)

        elif section == 'decade_title':
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = new_url + '/page'+page+'/'
            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            new_url = url.rpartition('/')[0]
            new_url = new_url+'/'
            html = net.http_GET(new_url+'page'+str(page)+'/').content

            if total_pages == '':
                #lastlist = url
                r= '>([0-9]*)</a>\s*<a href=".+?" class="next">' #% lastlist
                total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'decade_title', url, type, str(page), total_pages)
            
            match=re.compile('<div class="mask"><a href=".+?"><img src=".+?" alt="(.+?)"/></a></div>.+?<div class="_clear"></div>\s*<div class="airtime">(.+?)</div>',re.DOTALL).findall(html)
            for name, netw in match:
                name = self.CleanTextForSearch(name)
                name2 = name.replace(' ','-').replace('\'','-').replace('.','-').replace(':','').replace('&-','')
                url = 'http://trakt.tv/shows/'+name2
                netw = netw.split('<')[0]
                netw = '[COLOR red]'+netw+'[/COLOR]'
                self.AddContent(list, indexer, common.mode_Content, name+ ' (' + netw.replace('(','').replace(')','') +')', '', 'tv_seasons', url=url, name=name)

        elif section == 'genres_title':
            import re
            #url = url.replace(' ','+')
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = new_url + '/page'+page+'/'
            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            url = urllib.unquote_plus(url)
            new_url = url.rpartition('/')[0]
            new_url = new_url+'/'
            html = net.http_GET(new_url+'page'+str(page)+'/').content

            if total_pages == '':
                #lastlist = url
                r= '>([0-9]*)</a>\s*<a href=".+?" class="next">' #% lastlist
                total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'genres_title', url, type, str(page), total_pages)
            
            match=re.compile('<div class="mask"><a href=".+?"><img src=".+?" alt="(.+?)"/></a></div>.+?<div class="_clear"></div>\s*<div class="airtime">(.+?)</div>',re.DOTALL).findall(html)
            for name, netw in match:
                name = self.CleanTextForSearch(name)
                name2 = name.replace(' ','-').replace('\'','-').replace('.','-').replace(':','').replace('&-','')
                url = 'http://trakt.tv/shows/'+name2
                netw = netw.split('<')[0]
                netw = '[COLOR red]'+netw+'[/COLOR]'
                self.AddContent(list, indexer, common.mode_Content, name+ ' (' + netw.replace('(','').replace(')','') +')', '', 'tv_seasons', url=url, name=name)

        elif section == 'genres1':
            
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://trakt.tv/movies/played?page='+ page
                            
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            html = net.http_GET(new_url).content
            total_pages = '446'
            #print html.encode('utf-8')
            #if total_pages == '':
                #r= '</a><a href="/movies/.+?" >(.+?)</a>	</div>'
                #total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'played', '', type, str(page), total_pages)
        
            match=re.compile('<td class="image">.+?<a href="(.+?)" title="(.+?) \((.+?)\)"><img src=').findall(html)
            for url, name, year in match:
                name = self.CleanTextForSearch(name.strip())
                name = name.replace('$','s')
                url='http://trakt.tv'+url
                self.AddContent(list, indexer, common.mode_File_Hosts, name + '[COLOR royalblue] (' + year +')[/COLOR]', '', type, '', name, year)

        elif section == 'web':
            new_url = url
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = 'http://www.tv.com/' + section + '/page'+page+'/'
            #http://www.tv.com/web/page2/
                
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            url = urllib.unquote_plus(url)
            
            new_url = 'http://www.tv.com/' + section+'/'
            
            html = net.http_GET(new_url+'page'+str(page)+'/').content

            if total_pages == '':
                #lastlist = url
                r= '>([0-9]*)</a>\s*<a href=".+?" class="next">' #% lastlist
                total_pages = re.compile(r).findall(html)[0]
            self.AddInfo(list, indexer, 'web', url, type, str(page), total_pages)
            
            match=re.compile('<div class="mask"><a href=".+?"><img src=".+?" alt="(.+?)"/></a></div>.+?<div class="_clear"></div>\s*<div class="airtime">(.+?)</div>',re.DOTALL).findall(html)
            for name, netw in match:
                name = self.CleanTextForSearch(name)
                name2 = name.replace(' ','-').replace('\'','-').replace('.','-').replace(':','').replace('&-','')
                url = 'http://trakt.tv/shows/'+name2
                netw = netw.split('<')[0]
                netw = '[COLOR red]'+netw+'[/COLOR]'
                self.AddContent(list, indexer, common.mode_Content, name+ ' (' + netw.replace('(','').replace(')','') +')', '', 'tv_seasons', url=url, name=name)

        elif section == 'listings':
            import re
            #url = url.replace(' ','+')
            new_url = url
                        
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            url = urllib.unquote_plus(url)
            html = net.http_GET(new_url).content
            
            
            r= '<td colspan="3" class="pop"><div align="center"><a href=".+?"><img src=".+?" border="0"></a>&nbsp;&nbsp;<a href="(.+?)">'
            next_pages = re.compile(r).findall(html)[0]
            url = 'http://www.thefutoncritic.com' + next_pages
            #next_pages = next_pages.replace('/listings/','')
            #next_pages = next_pages[:-1]
            #next_pages = next_pages.replace('/','-')
            #self.AddSection(list, indexer,'listings','[COLOR royalblue]<<--'+next_pages+'[/COLOR]',url,indexer)#(list, indexer, 'listings', url, type, '', total_pages)
            
            r2= '<td colspan="3" class="pop"><div align="center"><a href=".+?"><img src=".+?" border="0"></a>&nbsp;&nbsp;<a href=".+?"><img src="/.+?" border="0"></a>&nbsp;&nbsp;.+?&nbsp;&nbsp;<a href="(.+?)"'
            r3= 'border="0"></a>&nbsp;&nbsp;\[.+?, (.+?)\]&'
            todays_date = re.compile(r3).findall(html)[0]
            next_pages2 = re.compile(r2,re.DOTALL).findall(html)[0]
            url = 'http://www.thefutoncritic.com' + next_pages2
            next_pages2 = next_pages2.replace('/listings/','')
            next_pages2 = next_pages2[:-1]
            next_pages2 = next_pages2.replace('/','-')
            todays_date = todays_date.title()
            self.AddSection(list, indexer,'listings','[COLOR white]Today Date: '+'[COLOR red]'+todays_date+' [/COLOR]'+'[COLOR white]Click to go to:[/COLOR] '+'[COLOR royalblue]'+next_pages2+'-->>[/COLOR]',url,indexer)#(list, indexer, 'listings', url, type, '', total_pages)               
            
            match=re.compile('<td width="15%">(.+?)</td>\s*<td width="15%">(.+?)</td>\s*<td width="70%"><a href="(.+?)">(.+?)</a').findall(html)
            date_idem = re.search(r'border="0"></a>&nbsp;&nbsp;[.+?, (.+?)]', html)# february 25, 2014
            for time, netw, url, name in match:
                name = name.split(':')[0]
                name = self.CleanTextForSearch(name)
                url = 'http://www.thefutoncritic.com' + url
                name = re.sub('(.+?), the', 'the \g<1>', name)
                name = name.title()
                name = name.replace('Nhl Special','NHL').replace('$','').replace('Abc Special','ABC Special').replace('Nba Special','NBA').replace('Wwe Main Event','WWE Main Event').replace('Pbs Special','PBS Special').replace('Wwe Raw','WWE Raw').replace('Bet Special','BET Special').replace('Hbo Special','HBO Special').replace('Nbc Sports Special','NBC Sports Special').replace('#','')
                time=time.replace('&nbsp;','')
                netw = '[COLOR red]'+netw+'[/COLOR]'
                self.AddContent(list, indexer, common.mode_Content, name+ ' (' + netw + ')'+' '+'[COLOR royalblue]'+time+'[/COLOR]', '', 'tv_seasons', url=url, name=name)

            r= '<td colspan="3" class="pop"><div align="center"><a href=".+?"><img src=".+?" border="0"></a>&nbsp;&nbsp;<a href="(.+?)">'
            next_pages = re.compile(r).findall(html)[0]
            url = 'http://www.thefutoncritic.com' + next_pages
            next_pages = next_pages.replace('/listings/','')
            next_pages = next_pages[:-1]
            next_pages = next_pages.replace('/','-')
            self.AddSection(list, indexer,'listings','[COLOR royalblue]<<--[/COLOR]'+'[COLOR white]Click to go to: [/COLOR]'+'[COLOR royalblue]'+next_pages+'[/COLOR]',url,indexer)
            #self.AddSection(list, indexer,'listings','[COLOR royalblue]<<--'+next_pages+'[/COLOR]',url,indexer)

        elif section == 'calendar2':
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            import json
            html = net.http_GET(url).content
            match=re.compile('"show":{"title":"(.+?)","year":(.+?),.+?"network":"(.+?)".+?"episode":{"season":(.+?),"number":(.+?),"title":"(.+?)","overview":"","url":"(.+?)".+?"first_aired_iso":"(.+?)T.+?-(.+?)"',re.DOTALL).findall(html)
            
            ''' Pagination Code Start '''
            num_items_on_a_page = 25
            if page == '':                
                page = '1'
                total_items = len(match)
                total_pages = str ( ( total_items / num_items_on_a_page ) + ( 1 if total_items % num_items_on_a_page >= 1 else 0) )
                
            self.AddInfo(list, indexer, section, url, type, page, total_pages, sort_by, sort_order)
            
            start_index = ( int(page) - 1 ) * num_items_on_a_page
            match = match[ start_index : start_index + num_items_on_a_page  ]
            ''' Pagination Code End '''
            
            for name,year,network,Sea_num,eps_num,title,url,date,time in match:
                name = self.CleanTextForSearch(name)
                season_pull = "0%s"%Sea_num if len(Sea_num)<2 else Sea_num
                episode_pull = "0%s"%eps_num if len(eps_num)<2 else eps_num
                sea_eps = 'S'+season_pull+'E'+episode_pull
                network=network.replace('",','')

                item_id = common.CreateIdFromString(name + '_' + year + '_season_' + Sea_num + '_episode_' + eps_num)

                self.AddContent(list, indexer, common.mode_File_Hosts, name +'[COLOR royalblue] ('+sea_eps+')[/COLOR] [COLOR red]'+network+'[/COLOR] Date: [COLOR red]'+date+'[/COLOR]', item_id, 'tv_episodes', url=url, name=name, year=year, season=Sea_num, episode=eps_num)

        elif section == 'featured' or 'new-release' or 'latest-added' or 'latest-hd' or 'genres2':
            import re
            new_url = url.replace('.so/','.la/')
            if page == '':
                page = '1'
            else:
                page = str( int(page) )
                new_url = new_url + page

            
            from entertainment.net import Net
            
            net = Net(cached=False)
            import urllib
            url = urllib.unquote_plus(url)
            new_url = self.base_url+section+'/'
            
            html = net.http_GET(new_url+str(page)).content
            if total_pages == '':
                lastlist = '/'+section+'/'
                r= ">Next</a>&nbsp;&nbsp;&nbsp;<a href='%s(.+?)'>Last</a>" % lastlist
                total_pages = re.compile(r).findall(html)[0]
                
            self.AddInfo(list, indexer, section, '', type, str(page), total_pages)

            
            match=re.compile('<div class="movie_pic"><a href="(.+?)"  target="_self" title="(.+?) \((.+?)\)">').findall(html)
            for url,name,year in match:
                name = self.CleanTextForSearch(name)
                self.AddContent(list,indexer,common.mode_File_Hosts,name + '[COLOR royalblue] (' + year +')[/COLOR]' ,'',type, url=url, name=name, year=year)

        else:
            from entertainment.net import Net
            net = Net(cached=False)
            import urllib
            import re
            import json
            response = net.http_GET(url).content
            match = json.loads(response)
            
            ''' Pagination Code Start '''
            num_items_on_a_page = 25
            if page == '':                
                page = '1'
                total_items = len(match)
                total_pages = str ( ( total_items / num_items_on_a_page ) + ( 1 if total_items % num_items_on_a_page >= 1 else 0) )
                
            self.AddInfo(list, indexer, section, url, type, page, total_pages, sort_by, sort_order)
            
            start_index = ( int(page) - 1 ) * num_items_on_a_page
            match = match[ start_index : start_index + num_items_on_a_page  ]
            ''' Pagination Code End '''
            
            for movies in match:
                name = movies['title']
                if name:
                    name = name.encode('utf8')
                    year = str(movies['year'])
                    self.AddContent(list, indexer, common.mode_File_Hosts, name + ' (' + year +')', '', type, '', name, year)
              
       
    def GetContent(self, indexer, url, title, name, year, season, episode, type, list):
        import urllib
        url = urllib.unquote_plus(url)
        title = urllib.unquote_plus(title)
        name = urllib.unquote_plus(name)
        
        from entertainment.net import Net
        net = Net(cached=False)
        import re
        
        '''show_url = self.GoogleSearchByTitleReturnFirstResultOnlyIfValid('tvrage.com', name, 'shows', item_count=2, title_extrctr=['(.+?) tv show', '(.+?) \- tvrage'], exact_match=True)
        if show_url == '' :
            tv_url= 'http://www.tvrage.com/search.php?search=%s&searchin=2&button=Go' %(name.lower().replace(' ','+'))
            html = net.http_GET(tv_url).content
            r = re.search(r'<h2><a href="(.+?)">(.+?)</a> <img src=\'.+?\' /> </h2>\s*</dt>\s*<dd class="img"> <a href="/(.+?)">', html)
            show_url = 'http://www.tvrage.com' + r.group(1)
        
        item_url = show_url + '/episode_list'
        '''
                    
        import datetime
        todays_date = datetime.date.today()
        content = net.http_GET(url).content
        
        if type == 'tv_seasons':
            match=re.compile('<a class="titles-link" href="(.+?)"><div class="titles"><h3>Season (.+?)</h3>').findall(content)
            for url,seasonnumber in match:                
                item_url = 'http://trakt.tv'+url
                item_title = 'Season ' + seasonnumber
                item_id = common.CreateIdFromString(title + ' ' + item_title)               
                self.AddContent(list, indexer, common.mode_Content, item_title, item_id, 'tv_episodes', url=item_url, name=name, season=seasonnumber)

        elif type == 'tv_episodes':
            new_url = url
            print new_url
            print "####################################################################################################################################"
            content2 = net.http_GET(new_url).content
            match=re.compile('<h3><a href="(.+?)"><span class=\'main-title-sxe\'>.+?x(.+?)</span> (.+?)</a></h3><h4><span class="convert-date" data-date="(.+?)T.+?" data-timezone').findall(content2)
            
            for item_url,item_v_id_2,item_title,item_date in match:
                item_v_id_2 = str(int(item_v_id_2))
                
                item_fmtd_air_date = self.get_formated_date( item_date )
                if item_fmtd_air_date.date() > todays_date: break
                
                item_id = common.CreateIdFromString(name + '_season_' + season + '_episode_' + item_v_id_2)
                self.AddContent(list, indexer, common.mode_File_Hosts, item_title, item_id, type, url=item_url, name=name, season=season, episode=item_v_id_2)
                   
    def get_formated_date(self, date_str):
        
        import re
        import datetime

        if '00' in date_str:
            date_str = '01/Aug/2000'
        #date_str = date_str.replace('00/([0-9]{2})/([0-9]{4})','01/Aug/2000')
        date_str = date_str.replace('00/00/0000','01/Aug/2000')
        #date_str = re.sub(pattern, replace, date_str)
        
                
        item_air_date = common.unescape(date_str).replace('      ', '')
        item_fmtd_air_date = ""
        if 'Jan' in item_air_date: item_fmtd_air_date = '01-'
        elif 'Feb' in item_air_date: item_fmtd_air_date = '02-'
        elif 'Mar' in item_air_date: item_fmtd_air_date = '03-'
        elif 'Apr' in item_air_date: item_fmtd_air_date = '04-'
        elif 'May' in item_air_date: item_fmtd_air_date = '05-'
        elif 'Jun' in item_air_date: item_fmtd_air_date = '06-'
        elif 'Jul' in item_air_date: item_fmtd_air_date = '07-'
        elif 'Aug' in item_air_date: item_fmtd_air_date = '08-'
        elif 'Sep' in item_air_date: item_fmtd_air_date = '09-'
        elif 'Oct' in item_air_date: item_fmtd_air_date = '10-'
        elif 'Nov' in item_air_date: item_fmtd_air_date = '11-'
        elif 'Dec' in item_air_date: item_fmtd_air_date = '12-'
        else: item_fmtd_air_date = '12-'
        date = re.search('([0-9]{1,2})', item_air_date)
        if date: 
            date = date.group(1)
            item_fmtd_air_date += "%02d-" % int(date)
        else:
            item_fmtd_air_date += "01-"
        year = re.search('([0-9]{4})', item_air_date)
        if year: 
            year = year.group(1)
            item_fmtd_air_date += year
        else:
            item_fmtd_air_date += "0001"
            
        try:
            item_fmtd_air_date = datetime.datetime.strptime(item_fmtd_air_date, "%m-%d-%Y")
        except TypeError:
            import time
            item_fmtd_air_date = datetime.datetime(*(time.strptime(item_fmtd_air_date, "%m-%d-%Y")[0:6]))
            
        return item_fmtd_air_date
            
    def GetSection(self, indexer, section, url, type, list, page='', total_pages='', sort_by='', sort_order=''):
        
        from entertainment.net import Net
        
        net = Net(cached=False)
        url_type = ''
        content_type = ''
        

        if indexer == common.indxr_Movies:
            if section == 'main':
                self.AddSection(list, indexer,'trending','Trending','http://trakt.tv/movies/trending',indexer)
                self.AddSection(list, indexer,'boxoffice','Box Office','http://trakt.tv/movies/boxoffice',indexer)
                self.AddSection(list, indexer,'featured','Featured',self.base_url +'featured/',indexer)
                self.AddSection(list, indexer,'new-release','New Releases',self.base_url +'new-release/',indexer)
                self.AddSection(list, indexer,'latest-added','Latest Added',self.base_url +'latest-added/',indexer)
                self.AddSection(list, indexer,'latest-hd','Latest HD',self.base_url +'latest-hd/',indexer)
                self.AddSection(list, indexer,'popular','Popular','http://trakt.tv/movies/popular',indexer)
                self.AddSection(list, indexer,'watched','Watched','http://trakt.tv/movies/watched',indexer)
                self.AddSection(list, indexer,'played','Played','http://trakt.tv/movies/played/weekly',indexer)
                self.AddSection(list, indexer,'collected','Collected','http://trakt.tv/movies/collected/weekly',indexer)
                self.AddSection(list, indexer,'anticipated','Anticipated','http://trakt.tv/movies/anticipated',indexer)
                self.AddSection(list, indexer,'genres2','Genres',self.base_url,indexer)
                #self.AddSection(list, indexer,'year','By Year','http://www.thefutoncritic.com/listings/',indexer)
                #self.AddSection(list, indexer,'movieset','Movie Sets','http://trakt.tv/lists/movie-sets/popular',indexer)
                #self.AddSection(list, indexer,'personal','Personal List','http://trakt.tv/lists/personal/popular',indexer)
                #if self.Settings().get_setting('enable_trakt')=='true':
                #    self.AddSection(list, indexer,'trakt_watchlist','Trakt Watchlist','http://api.trakt.tv/user/watchlist/movies.json/18a6532a12a81d0f18bc25a158e5e4e9/' + self.Settings().get_setting('username'),indexer)
                #    self.AddSection(list, indexer,'trakt_lists','Trakt Lists','http://trakt.tv/user/%s/lists/' % self.Settings().get_setting('username'),indexer)
                    

            elif section == 'year':
                import re
                r = re.findall(r'<a   href="/shows/decade/.+?/">(.+?)</a>', net.http_GET(url).content, re.I)
                for genres in r[0:]:

                    self.AddSection(list, indexer, 'decade_title', genres, self.base_url_tv_com+'shows/decade/'+genres+'/', indexer)

            elif section == 'trakt_lists':
                import re
                r = re.findall(r'<h3>\s*<div class="title-overflow"></div>\s*<a href="/user/(.+?)/lists/(.+?)">(.+?)</a>\s*</h3>', net.http_GET(url).content, re.I)
                for username,url,title in r[0:]:
                    url='http://trakt.tv/user/'+username+'/lists/'+url
                    
                    self.AddSection(list, indexer, 'trakt_title', title, url, indexer)

            elif section == 'official':
                import re
                
                r = re.findall(r'<h3>\s*<div class="title-overflow"></div>\s*<a href="(.+?)">(.+?)</a>\s*</h3>', net.http_GET(url).content, re.I)
                print r
                print '##################################################'
                for url,title in r[0:]:
                    url='http://trakt.tv'+url
                    if 'Television' in title:
                        self.AddSection(list, indexer, 'trakt_tv', title, url, indexer)
                    else:
                        self.AddSection(list, indexer, 'trakt_official', title, url, indexer)

            elif section == 'personal':
                new_url = url
                if page == '':
                    page = '1'
                else:
                    page = str( int(page) )
                    new_url = 'http://trakt.tv/lists/personal/popular/weekly/'+ page
                                
                from entertainment.net import Net
                net = Net(cached=False)
                import urllib
                import re
                url = urllib.unquote_plus(url)
                
                html = net.http_GET(new_url).content
                total_pages = '20'
                self.AddInfo(list, indexer, 'personal', '', type, str(page), total_pages)
                r = re.findall(r'<h3>\s*<div class="title-overflow"></div>\s*<a href="(.+?)">(.+?)</a>\s*</h3>', net.http_GET(new_url).content, re.I)
                for url,title in r[0:]:
                    url='http://trakt.tv'+url
                    if 'Television' in title:
                        self.AddSection(list, indexer, 'trakt_tv', title, url, indexer)
                    else:
                        self.AddSection(list, indexer, 'trakt_personal', title, url, indexer)

            elif section == 'movieset':
                
                new_url = url
                if page == '':
                    page = '1'
                else:
                    page = str( int(page) )
                    new_url = 'http://trakt.tv/lists/movie-sets/popular/weekly/'+ page
                                
                from entertainment.net import Net
                net = Net(cached=False)
                import urllib
                import re
                url = urllib.unquote_plus(url)
                
                html = net.http_GET(new_url).content
                total_pages = '20'
                self.AddInfo(list, indexer, 'movieset', '', type, str(page), total_pages)
                r = re.findall(r'<h3>\s*<div class="title-overflow"></div>\s*<a href="(.+?)">(.+?)</a>\s*</h3>', net.http_GET(new_url).content, re.I)
                for url,title in r[0:]:
                    url='http://trakt.tv'+url
                    if 'Television' in title:
                        self.AddSection(list, indexer, 'trakt_tv', title, url, indexer)
                    else:
                        self.AddSection(list, indexer, 'trakt_personal', title, url, indexer)
                

                        
            elif section == 'genres2':
                self.AddSection(list, indexer,'action','Action',self.base_url +'action/',indexer)
                self.AddSection(list, indexer,'adventure','Adventure',self.base_url +'adventure/',indexer)
                self.AddSection(list, indexer,'animation','Animation',self.base_url +'animation/',indexer)
                self.AddSection(list, indexer,'biography','Biography',self.base_url +'biography/',indexer)
                self.AddSection(list, indexer,'comedy','Comedy',self.base_url +'comedy/',indexer)
                self.AddSection(list, indexer,'crime','Crime',self.base_url +'crime/',indexer)
                self.AddSection(list, indexer,'documentary','Documentary',self.base_url +'documentary/',indexer)
                self.AddSection(list, indexer,'drama','Drama',self.base_url +'drama/',indexer)
                self.AddSection(list, indexer,'family','Family',self.base_url +'family/',indexer)
                self.AddSection(list, indexer,'fantasy','Fantasy',self.base_url +'fantasy/',indexer)
                self.AddSection(list, indexer,'history','History',self.base_url +'history/',indexer)
                self.AddSection(list, indexer,'horror','Horror',self.base_url +'horror/',indexer)
                self.AddSection(list, indexer,'music','Music',self.base_url +'music/',indexer)
                self.AddSection(list, indexer,'musical','Musical',self.base_url +'musical/',indexer)
                self.AddSection(list, indexer,'mystery','Mystery',self.base_url +'mystery/',indexer)
                self.AddSection(list, indexer,'romance','Romance',self.base_url +'romance/',indexer)
                self.AddSection(list, indexer,'sci-fi','Sci-Fi',self.base_url +'sci-fi/',indexer)
                self.AddSection(list, indexer,'short','Short',self.base_url +'short/',indexer)
                self.AddSection(list, indexer,'thriller','Thriller',self.base_url +'thriller/',indexer)
                self.AddSection(list, indexer,'war','War',self.base_url +'war/',indexer)
                self.AddSection(list, indexer,'western','Western',self.base_url +'western/',indexer)       
                
            else:
                self.ExtractContentAndAddtoList(indexer, section, url, type, list, page, total_pages, sort_by, sort_order)

        elif indexer == common.indxr_TV_Shows:
            if section == 'main':
                self.AddSection(list, indexer,'latesttv','Date Added','http://thewatchseries.to/latest',indexer)
                self.AddSection(list, indexer,'populareps','Popular Episodes Added This Week','http://thewatchseries.to/new',indexer)
                self.AddSection(list, indexer,'trendingtv','Trending','http://trakt.tv/shows/trending',indexer)
                self.AddSection(list, indexer,'populartv','Popular','http://trakt.tv/shows/popular',indexer)
                self.AddSection(list, indexer,'watchedtv','Watched','http://trakt.tv/shows/watched/weekly',indexer)
                self.AddSection(list, indexer,'playedtv','Played','http://trakt.tv/shows/played/weekly',indexer)
                self.AddSection(list, indexer,'collectedtv','Collected','http://trakt.tv/shows/collected/weekly',indexer)
                self.AddSection(list, indexer,'anticipated','Anticipated','http://trakt.tv/shows/anticipated',indexer)
                self.AddSection(list, indexer,'network','By Network','http://www.tv.com/shows/',indexer)
                self.AddSection(list, indexer,'decade','By Decade','http://www.tv.com/shows/',indexer)
                self.AddSection(list, indexer,'web','Web Series','http://www.tv.com/web/',indexer)
                self.AddSection(list, indexer,'genres_tv','Genres','http://www.tv.com/shows/',indexer)
                self.AddSection(list, indexer,'listings','TV Show Schedule','http://www.thefutoncritic.com/listings/',indexer)
                #self.AddSection(list, indexer,'calendardate','Calendar','http://api.trakt.tv/calendar/shows.json/18a6532a12a81d0f18bc25a158e5e4e9',indexer)
                #http://api.trakt.tv/calendar/shows.json/18a6532a12a81d0f18bc25a158e5e4e9/20140803/1
                #self.AddSection(list, indexer,'genrestv','Genres','http://trakt.tv/shows/popular/',indexer)
                #if self.Settings().get_setting('enable_trakt')=='true':#show/episode
                #    self.AddSection(list, indexer,'trakt_watchlisttv','Trakt Show Watchlist','http://api.trakt.tv/user/watchlist/shows.json/18a6532a12a81d0f18bc25a158e5e4e9/' + self.Settings().get_setting('username'),indexer)
                    #self.AddSection(list, indexer,'trakt_watchlist','Trakt Episode Watchlist','http://api.trakt.tv/user/watchlist/show/episode.json/18a6532a12a81d0f18bc25a158e5e4e9/' + self.Settings().get_setting('username'),indexer)
                    #self.AddSection(list, indexer,'trakt_lists','Trakt Lists','http://trakt.tv/user/%s/lists/' % self.Settings().get_setting('username'),indexer)

            elif section == 'calendardate':
                import re
                from datetime import date, timedelta


                for i in range(1,14):
                    days= i

                    date =date.today()-timedelta(days=days)
                    datestring = str(date).replace('-','')


                    self.AddSection(list, indexer,'calendar2',str(date),'http://api.trakt.tv/calendar/shows.json/18a6532a12a81d0f18bc25a158e5e4e9/'+str(datestring)+'/1',indexer)

            elif section == 'network':
                import re
                r = re.findall(r'<a   href="/shows/network/(.+?)/">.+?</a>', net.http_GET(url).content, re.I)
                for network in r[0:]:

                    network_title = network.replace('-',' ')
                    network_title = network_title.replace('and','&')
                    network_title = network_title.upper()
                    self.AddSection(list, indexer, 'network_title', network_title, 'http://www.tv.com/shows/network/'+network+'/', indexer)
                    

            elif section == 'decade':
                import re
                r = re.findall(r'<a   href="/shows/decade/.+?/">(.+?)</a>', net.http_GET(url).content, re.I)
                for genres in r[0:]:

                    self.AddSection(list, indexer, 'decade_title', genres, 'http://www.tv.com/shows/decade/'+genres+'/', indexer)
                    

            elif section == 'genres_tv':
                import re
                r = re.findall(r'<a   href="/shows/category/(.+?)/">.+?</a>', net.http_GET(url).content, re.I)
                for genres in r[0:]:
                    genres_title = genres.replace('-',' ')
                    genres_title = genres_title.replace('and','&')
                    genres_title = genres_title.upper()
                    self.AddSection(list, indexer, 'genres_title', genres_title, 'http://www.tv.com/shows/category/'+genres+'/', indexer)

            elif section == 'genrestv':
                self.AddSection(list, indexer,'populartvgenre','Action','http://trakt.tv/shows/popular/action',indexer)
                self.AddSection(list, indexer,'populartvgenre','Adventure','http://trakt.tv/shows/popular/Adventure',indexer)
                self.AddSection(list, indexer,'populartvgenre','Animation','http://trakt.tv/shows/popular/animation',indexer)
                self.AddSection(list, indexer,'populartvgenre','Comedy','http://trakt.tv/shows/popular/comedy',indexer)
                self.AddSection(list, indexer,'populartvgenre','Documentary','http://trakt.tv/shows/popular/documentary',indexer)
                self.AddSection(list, indexer,'populartvgenre','Drama','http://trakt.tv/shows/popular/drama',indexer)
                self.AddSection(list, indexer,'populartvgenre','Fantasy','http://trakt.tv/shows/popular/fantasy',indexer)
                self.AddSection(list, indexer,'populartvgenre','Game Show','http://trakt.tv/shows/popular/game-show',indexer)
                self.AddSection(list, indexer,'populartvgenre','Home and Garden','http://trakt.tv/shows/popular/home-and-garden',indexer)
                self.AddSection(list, indexer,'populartvgenre','Mini Series','http://trakt.tv/shows/popular/mini-series',indexer)
                self.AddSection(list, indexer,'populartvgenre','News','http://trakt.tv/shows/popular/news',indexer)
                self.AddSection(list, indexer,'populartvgenre','No Genre','http://trakt.tv/shows/popular/none',indexer)
                self.AddSection(list, indexer,'populartvgenre','Reality','http://trakt.tv/shows/popular/reality',indexer)
                self.AddSection(list, indexer,'populartvgenre','Science Fiction','http://trakt.tv/shows/popular/science-fiction',indexer)
                self.AddSection(list, indexer,'populartvgenre','Soap','http://trakt.tv/shows/popular/soap',indexer)
                self.AddSection(list, indexer,'populartvgenre','Fantasy','http://trakt.tv/shows/popular/special-interest',indexer)
                self.AddSection(list, indexer,'populartvgenre','Sport','http://trakt.tv/shows/popular/sport',indexer)
                self.AddSection(list, indexer,'populartvgenre','Talk Show','http://trakt.tv/shows/popular/talk-show',indexer)
                self.AddSection(list, indexer,'populartvgenre','Western','http://trakt.tv/shows/popular/western',indexer)
                
            else:
                self.ExtractContentAndAddtoList(indexer, section, url, type, list, page, total_pages, sort_by, sort_order)
            

    
