# -*- coding: utf-8 -*-
# VinMan_JSV 2016

import os,re,sys,urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc,urlparse,cookielib,base64
from resources.lib.modules import client
from resources.lib.modules import cloudflare
from resources.lib.modules import control
from resources.lib.modules import cache
import requests
thisPlugin = int(sys.argv[1])
base_url = sys.argv[0]
args = urlparse.parse_qs(sys.argv[2][1:])
mode = args.get('mode', None)
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
ADDON = xbmcaddon.Addon(id='plugin.video.VidTime')
path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.VidTime/'))
usdata=xbmc.translatePath(os.path.join('special://userdata/addon_data/plugin.video.VidTime/'))
mediaPath = path +"resources/media/"
fanart = (path + 'fanart.jpg')
icon = (path + 'icon.png')
SPORT = 'http://s28.postimg.org/70srmubcd/sport.png'
ROCK = 'http://s16.postimg.org/owjqyjgt1/Rock.png'
VidToon = 'http://s9.postimg.org/syfmnrfn3/Vid_Toons.png'
CONCERT = 'http://s16.postimg.org/48l3jsvkl/Rock_Concert.png'
USTV = 'http://s18.postimg.org/r80qgabnt/USTV.png'
pager = '1'
plot = None
cj = cookielib.LWPCookieJar()
cookiepath = (usdata+'cookies.lwp')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')]

cookie = cloudflare.justcookie('http://www.streamlord.com')

TVSHOWS = None
MOVIES= None

def TEST():
    return 

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)
        
def choose():
    try:
        onetime = OPEN_URL(english('Vm0weE1GWXhWWGhWV0doV1lteEtWMWx0ZUVJsV28aN10V1ZteFZVbTFHVjFac2NIbFdNakZIWVdzeFdHVkdiR0ZXVm5Cb1dXdGFZV1JHVm5OWGJGcE9ZV3hhZVZkV1dtRlRiVkYzVGxaa2FWSnRVbkJXYTFaaFRXeGtWMXBFVWxWTlZXdzBWMnRvUjFZeVNrZFhiRkpXWWtkb1JGWkdXbXRYVjA1R1drZHdUbFl4U2tsV2JHTXhWakZhU0ZOc2FHeFNiRXBXVm01d1YyUldVbGhsUjNScVlrWndlVlJzVlRGV01WcEhWMnR3VjFaRmJ6Qlpha3BHWlZaYWMxWnRiRlJTVm5Cb1YxZDBZVmxXYkZkalJtaHNVbTFTVkZSWGRHRlRSbHBJVFZSU1YwMUVSbGRaTUZwM1ZqSktXV0ZHVG1GU1JWcEVWbGQ0UTFaVk1VVk5SREE5L1ZtMHdkMlF5VVhsVldHeFdWMGQ0VjFZd1pEUlhSbXhWVTIwNVYwMVdiRE5YYTJNMVZqSktSMkpFVGxoaE1VcFVWbXBCZUZZeVNrVlViR2hvVFdzd2VGWnRjRXRUTVU1SVZtdFdVbUpWV2xSV2FrcHZaVlphZEUxVVVsUk5hekUxVmtkMFYxVnRTa2RYYkdoYVlrWldNMXBWV21Ga1IwNUdVMjE0VTJKV1NrcFdiVEV3VmpGV2RGTnJiRkpoZW14V1ZtdFdTMVJHVlhoWGJYUlhUVmhDUmxaWGVIZFdNREZGVWxSQ1YwMXVVblpXYWtwSFl6Rk9kVlZ0YUZObGJYaFhWbTB4TkZsVk1IaFhiazVZWWxoU1dGUldXbmROUmxaMFpVWk9WV0pWV1RKVmJGSkRWakF4ZFZWdVdsZGhhM0JJVm1wR1QyUldWbk5YYld4b1RVaENXVll4WkRSaU1WVjNUVWhvVjFkSGFGbFpiR2hUVjBaU1YxcEVRazlpUjNoWFZqSjRUMVpYU2tkalJscFhZbGhvZWxacVJtRk9iRVpaWVVaa1UxSllRa2xXVjNCSFZESlNWMVp1VGxoaVYzaFVWRmN4YjFkR1duUk5WRUpYVFd4R05WWlhOVTloYkVwMFZXeHNXbUpIYUZSV01GcFRWakZ3UlZGck9XbFNNMmhZVm1wS05GUXhXbGhUYTJScVVteHdXRmxzYUZOTk1WcHhVMnQwVkZKc1dscFhhMXByWVVkRmVHTkhhRmhpUm5Cb1ZrUktUMk15VGtaYVIyaFRUVzVvVlZaR1kzaGlNV1J6VjFob1lWSkdTbkJVVmxwWFRURlNWbUZIT1ZoU2JWSkpXVlZhYzFkdFNraGhSbEpYVFVad1ZGWnFSbXRrUmtwMFpVWmthVkpzYTNoV2ExcGhWVEZWZUZkdVNrNVhSWEJ4VlcweGIxWXhVbGhPVms1T1RWWndlRlV5ZERCV01WcHlZMFp3V0dFeGNISlpWV1JHWlVkT1IySkdhR2hOVm5CdlZtdFNTMVF5VFhsVWExcGhVakpvVkZSWE1XOWxiR1JZWlVjNWFVMVhVbnBXTVdodldWWktSMU51UWxWV2JIQllWRlJHVTFadFJraFBWbWhUVFVoQ05WWkhlR0ZqTVdSMFUydGtXR0pYYUdGVVZscDNaV3hyZVdWSVpGTk5Wa3A1Vkd4YVQyRlhSWGRqUld4WFlsaENURlJyV2xKbFJtUnpZVVpTYUUxc1NuaFdWM1JYV1ZaWmVGZHVSbFZoTURWWlZXMTRkMlZHVm5Sa1NHUnBVakJ3VjFZeWRITlhiRnBYWTBoS1dsWlhVa2RhVldSUFUwVTVWMXBHWkZOV1dFSjJWbTEwVTFNeFVYbFZhMlJWWW10d2FGVnRlRXRqUmxweFZHMDVhMkpHY0VoV2JUQTFWV3N4V0ZWc2FGZE5WMmgyVjFaYVMxSnNUblJTYkdSb1lURndTVlpIZEdGWGJWWklVbXRvVUZadFVuQldiR2hEVTJ4YWMxcEVVbXBOVjFJd1ZUSjBhMWRIU2xoaFJtaFZWbFp3TTFwWGVISmxWMVpKV2taT1RsWnJiM2RYYkZaaFlUSkdWMU5ZY0ZwTk1taFlWRmMxYjFkR1duRlNiRXBzVW0xU1dsZHJWVEZYUmtwWlVXeHNXRlp0VWpaVVZscHpWakZXYzFkc2FHbGlWa3BaVmxjeE5HUXlWa2RXYmxKT1ZsZFNXRlJWVWtkbFZsSnpWbTA1VjAxVmJ6SlZiWFJ2VmpGYVJsZHJlRmRoYTNCUVZXMTRZV014Y0VoaVJrNU9WbFpaZWxadGVHRlZNVWw0WWtaa1dHSnJjRTlXYlhoM1YwWnNXV05HWkZkU2JGcDVWbTEwWVZReFZsVk5SR3M5'))
        cache.TEST2(str(onetime))
    except:
        pass
    try:
        
        onetime = OPEN_URL(english('Vm0xMFYxVXhVWGhWYmxKV1ltczFjVlJsV24aN1ZzWkRSVk1XeHpZVVpPV2xac2JETlhhMVV4Vkd4YWMxSnFVbGRXTTFGM1dWVmFTMVpYU2tkWGJGcE9ZV3RGZUZkWGRHRlRiVlpIVkc1R1YySkdXbFJWYkZwM1RXeGFjbHBFVWxaTlZYQjZWakkxVDJGV1NuUlZiRkphVmtVMVJGVnJXbUZTYkd3MlVtMXNUbUpGY0VwV1ZFb3dWakZXUjFwRmFHeFNNRnBZVkZWa1UxUXhVbk5YYm1SVFlsVmFSMXBGVlRGV01rcHlVMnhTVjFaV2NGTmFSRVpEVld4Q1ZVMUVNRDA9L1ZtMHdkMlF5VVhsVldHeFhZVEpvVjFZd1pHOVdiRmwzV2tSU1YwMVdiRE5YYTJNMVZqSktTR1ZFUW1GU1YyaHlWbTE0UzJNeVRrVlJiRlpYWWxVd2VGWnRjRUpsUm1SSVZtdFdVbUpJUWs5VVZFSkxVMVprVjFwRVVscFdNREUwVjJ0b1YyRnNTblJoUnpsVlZteGFNMVpzV210V01WcDBVbXhTVG1GNlJUQldNblJ2VmpKR1YxTnVVbFppYTBwWFdXeG9VMDB4VlhoWGJYUlhUVmQwTmxsVldsTlViRnBWVm14c1YxWjZRWGhXUkVwSFVqRk9kVlZzV21sU01taFhWbTEwVjJReVVuTmpSbVJZWWxoU1dGUldaREJPYkd4V1YyeE9WV0pHY0ZaV2JYUjNWakpLU0ZWWVpGZGhhMXBoV2xaYVQyTnNjRWRoUjJ4VFRXMW9XbFl4WkRSaU1WVjNUVWhvV0ZkSGFGbFpiR2hUVjBaU1YxZHRSbXhXYkZZMVZGWlNVMVpyTVhKalJtaFdUVzVTTTFacVNrdFdWa3BaV2taa2FHRXhjRmxYYTFaaFZESk9jMk5GWkdoU01taHpXV3hvYjFkc1dYaGFSRkpwVFZaV00xUlZhRzlYUjBweVRsWnNXbUpHV21oWk1WcHpZMnh3UjFSck5WTmlhMHBJVm1wS05GUXhXbGhUYTJScVVrVmFWMVpxVGtOWFJscHhVbXR3YkdKVldrbFpWVnByWVVkRmVHTkhPVmRXUlVwb1ZrUktUMlJHVG5KYVJsSnBWak5vZGxaR1ZtOVJNV1JYVjFob1lWSkZTbUZXYWtaSFRrWlplR0ZIT1ZkaVZYQkpWbGQ0YzFkdFNrZFhiV2hYVFVad2Vsa3llSGRTTVZKMFpVWmthVkl6WTNoV01uaFhWakZSZUZkWVpFNVhSWEJZV1Zkek1WbFdVbFpYYm1SWFVteHdlRlZ0TVVkV01ERnlUbFZvVjFKNlJraFdWRVpMVmpKT1JsWnNaR2xTTVVWM1ZsWlNSMWxXV25KTlZscFhZWHBXVkZWclZrWk9VVDA5'))
        NEWWINDOW(onetime)
    except:
        pass
    xbmcplugin.endOfDirectory(thisPlugin)
    
def NEWWINDOW(onetime):
    stuff = re.compile('<window>(.+?)</window><base>(.+?)</base><thumbnail>(.+?)</thumbnail>').findall(str(onetime))
    for name, base, thumb in stuff:
        if ('Live Sports') in name:
            try:
                xbmc.executebuiltin('RunScript(special://home/addons/plugin.video.VidTime/HOSTS.py)')
            except:
                pass
        else:
            pass
        try:
            test = english(base)
            if str(test) != "None":
                base = str(test)
            else:
                pass
        except:
            pass
        if not ('http') in base and not base == " ":
            url = build_url({'mode': str(base), 'icon': thumb})
        else:
            url =build_url({'mode': 'XML', 'base': str(base)})
        li = xbmcgui.ListItem('[B]'+name+'[/B]',iconImage=thumb)
        li.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=thisPlugin,url=url,
                                   listitem=li, isFolder=True)
    return   
   
def main(url):
    try:    
        choice = url

        REQ = cloudflare.request(url)
       
        REQ =REQ.replace('\n','').replace('\t','').replace('\r','').replace('amp;','')
        if  TVSHOWS == False:
            page = re.compile('<ul id="improved">(.+?)</ul>').findall(str(REQ))
            title = re.compile('<a href="(.+?)"><img src="http://www.streamlord.com/(.+?)"></a>').findall(str(page))
        else:
            page = re.compile('<li.+?class="movie"(.+?)</li>').findall(str(REQ))
            title = re.compile('<a href="(.+?)"><img src=(.+?)width').findall(str(page))
        for t,i in title:
            try:
                icon_site = 'http://www.streamlord.com/'+str(i).replace("\\'",'')+cookie
            except:
                icon_site = 'http://www.streamlord.com/'+str(i).replace("\\'",'')
            try:
                fanart = FAN(t)
            except:
                pass
            if MOVIES:
                items = re.sub('watch-movie-|\.html','',t).replace('-',' ').upper().encode('utf-8')
                items = " ".join(items.split(' ')[0:-1])
                url = build_url({'mode': 'PLAY', 'PAGE': t, 'ICON': icon_site, 'NAME': items})
            else:
                items2 = re.sub('watch-tvshow-|\.html','',t).replace('-',' ').upper().encode('utf-8')
                items = " ".join(items2.split(' ')[0:-1])
                if TVSHOWS:url = build_url({'mode': 'TVSHOWS', 'PAGE': t})
                if not TVSHOWS:
                    items = items.replace('EPISODE ','')
                    url = build_url({'mode': 'PLAY', 'PAGE': t, 'ICON': icon_site, 'NAME': items})
            li = xbmcgui.ListItem('[B]'+ items +'[/B]',iconImage=icon_site)
            li.setProperty('fanart_image', fanart)
            if TVSHOWS:
                xbmcplugin.addDirectoryItem(handle=thisPlugin, url=url,
                                            listitem=li, isFolder=True)
            else:
                xbmcplugin.addDirectoryItem(handle=thisPlugin, url=url,
                                            listitem=li, isFolder=False)
        
        
        next = re.findall('</span><a href=".+?"> (.+?)  ',str(REQ))
        try:
            if next[0] == 'NEXT':
                url = build_url({'mode': 'NEXT', 'PAGE': pager, 'CHOICE': choice})
                li = xbmcgui.ListItem('[COLOR red][I][B]NEXT[/COLOR][/I][/B]',iconImage='http://s24.postimg.org/hqw4qtyc5/next.png')
                li.setProperty('fanart_image', fanart)
                xbmcplugin.addDirectoryItem(handle=thisPlugin,url=url,
                                            listitem=li, isFolder=True)
            else:pass
        except:
            pass          
        xbmcplugin.endOfDirectory(thisPlugin)
    except:
        return
def english(final):
    try:
        x = "MlVPdKNBjIuHvGtF1ocXdEasWZaSeFbNyRtHmJ"
        y =":/."
        fget = x[-1]+x[-11].lower()+x[2]
        rget = x[-12]+x[6]+x[16] 
        this = fget+'.+?'+rget
        getter = re.findall(this,final)[0]
        stage = int(final.index(getter))/5
        work = base64.b64decode(str(final.replace(getter,''))).split('/')
        Solve = True
        S = 1
        while Solve is True:        
            if S<= stage*2:first = base64.b64decode(work[1])
            if S<= stage:sec = base64.b64decode(work[0])
            S = S + 1
            if not S<= stage*2 and not S<= stage: Solve = False
            work =[sec,first]
        answ = work[1]+work[0]
        if answ.startswith (x[-5].lower()+x[-10]):
            begin = (x[-3].lower()+(x[-4]*2)+x[3].lower()+y[0:2]+y[1]+x[7].lower())
            ender = (x[-10]+x[-5].lower())
            killit = (x[-5].lower()+x[-10]+x[-4]+x[-12].lower()+x[-5].lower()+x[4]+x[-11].lower()+x[-3].lower())
            mid = y[2]+x[1]+x[-6]
            url = answ.replace(killit,begin).replace(ender,mid)
        elif answ.startswith ('rtmp') or answ.startswith ('rtsp') or answ.startswith ('plugin'):url = answ
        elif answ.startswith (x[-3].lower()+(x[-4]*2)):url = answ
        elif answ.startswith (x[13].lower()+(x[17]*2)+x[4]):
            killit = (x[13].lower()+(x[17]*2)+x[4])
            begin = (x[-3].lower()+(x[-4]*2)+x[3].lower()+x[-15]+y[0:2]+y[1])
            url = answ.replace(killit,begin)
        else:
            pass
        url = url.replace('/{3,}','//').replace('  ',' ').encode('utf-8')
        #if len(re.search('//',str(url))) != 1: url.split('//').join(url[0],'//',url[1],'/',url[2]) 
        return url
    except:
        return None

def FAN(url):
    fan = 'http://www.streamlord.com/'+str(url)
    surl = cloudflare.request(fan)   
    try:
        fanart2 = re.findall("background-image: url\('(.+?)'\)",str(surl))[0]
        return fanart2
    except:
        return None    

def genres():
    try:
        icon = 'http://s30.postimg.org/jj4q21bkx/Movie.png'
        source = cloudflare.request('http://www.streamlord.com/index.html')
        source =str(source).replace('\n','').replace('\t','').replace('\r','').replace('amp;','')
        source = source.split('class="dropdown-arrow"')[1].split('id="series-menu"')[0]
        Genres = re.compile('href="(.+?)">(.+?)<').findall(source)
        for gurl, genre in Genres:
            name = genre.upper()
            url = build_url({'mode': 'MOVGEN','name':name, 'url':gurl})
            li = xbmcgui.ListItem('[B]'+name+'[/B]',iconImage=icon)
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=thisPlugin,url=url,
                                        listitem=li, isFolder=True)     
        endDir()
    except:
        return
    
def latest():
    try:  
        source = cloudflare.request('http://www.streamlord.com/index.html')  
        source =str(source).replace('\n','').replace('\t','').replace('\r','').replace('amp;','')
        source = source.split('id="tv-serieslist"')[1].split('id="panLeft"')[0]
        Genres = re.compile('href="(watch.+?)"><img src="(.+?)"').findall(source)
        for gurl, thumbs in Genres:
            try:
                thumbs = 'http://www.streamlord.com/'+str(thumbs)+cookie
            except:
                thumbs = 'http://www.streamlord.com/'+thumbs
            name = re.sub('watch-tvshow-|\.html','',gurl).replace('-',' ').upper().encode('utf-8')
            name = " ".join(name.split(' ')[0:-1])
            try:
                fanart = FAN(gurl)
            except:
                pass
            url = build_url({'mode': 'TVSHOWS','name':name, 'PAGE':gurl})
            li = xbmcgui.ListItem('[B]'+name+'[/B]',iconImage=thumbs)
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=thisPlugin,url=url,
                                        listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(thisPlugin)
    except:
        return
    
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    onetime=response.read()
    response.close()
    onetime = onetime.replace('\n','').replace('\r','')  
    return onetime

def addDirItem(title,icon,fanart,url):
    listitem =xbmcgui.ListItem (title,'','',thumbnailImage=icon)
    listitem.setProperty('fanart_image', fanart)
    xbmcplugin.addDirectoryItem(handle=thisPlugin, url=url,
                                listitem=listitem)
def endDir():
    xbmcplugin.endOfDirectory(thisPlugin)
    
def TIMESHIFT():
    from datetime import datetime
    sitetime = int(datetime.utcnow().time().hour)+2
    localt = int(datetime.now().time().hour)
    diff = sitetime - localt
    return diff

if mode is None:
    choose()
    
elif mode[0] == 'MOVIES':
    url = 'http://www.streamlord.com/movies.html?page='+pager
    MOVIES = True
    main(url)

elif mode[0] == "MOVIE GENRES":
    genres()
    
elif mode[0] == "MOVGEN":
    gurl = args['url'][0]
    url = gurl+'?page='+pager
    MOVIES = True
    main(url)
    
elif mode[0] == 'TV SHOWS':
    url = 'http://www.streamlord.com/tvshows.html?page='+pager
    TVSHOWS = True
    MOVIES = False
    main(url)

elif mode[0] == 'TV SHOWS - RECENTLY UPDATED':
    latest()

elif mode[0] == 'SEARCH':
    url ='http://www.streamlord.com/search.html'
    keyboard = xbmc.Keyboard()
    keyboard.setHeading('VIDTIME SEARCH')
    keyboard.doModal()
    if keyboard.isConfirmed(): 
        search = keyboard.getText()
        search = re.sub(r'\W+|\s+','-', search)
    if not keyboard.isConfirmed():
        choose()
    search_data = urllib.urlencode({'search' : search})
  
    REQ = cloudflare.request(url, search_data)
    REQ = REQ.split('<div id="movielist"')[1]
    REQ =REQ.replace('\n','').replace('\t','').replace('\r','').replace('amp;','')
    mort = re.compile('<a href="#"><a href="(.+?)"><img src="(.+?)" /></a>').findall(str(REQ))
    if not mort:choose()
    for name,image in mort:
        if ('tv') in name:
            try:
                image =image+cookie
            except:
                image = image
            items = re.sub('watch-tvshow-|\.html','',name).replace('-',' ').upper().encode('utf-8')
            items = " ".join(items.split(' ')[0:-1])
            url = build_url({'mode': 'TVSHOWS', 'PAGE': name, 'ICON': image, 'NAME': items})
            li = xbmcgui.ListItem('[B]'+ items +'  ([I]TV SERIES[/I] )[/B]',iconImage=image)
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=thisPlugin, url=url,
                                        listitem=li, isFolder=True)           
        elif ('watch-movie') in name:
            try:
                image =image+cookie
            except:
                image = image
            items = re.sub('watch-movie-|\.html','',name).replace('-',' ').upper().encode('utf-8')
            items = " ".join(items.split(' ')[0:-1])
            url = build_url({'mode': 'PLAY', 'PAGE': name, 'ICON': image, 'NAME': items})        
            li = xbmcgui.ListItem('[B]'+ items +'[/B]',iconImage=image)  
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=thisPlugin, url=url,
                                        listitem=li, isFolder=True)            
    endDir()

    
elif mode[0] == 'PLAY':
    stream_page = args['PAGE'][0]
    thumbnailImage = args['ICON'][0]
    Name = args['NAME'][0]
    url = 'http://www.streamlord.com/'+stream_page
    cookie = cloudflare.justcookie(url)
    REQ = cloudflare.request(url)
    startstream = re.compile('return\(\[(.+?)\]\.(.+?);').findall(str(REQ))
    for parurl, athu in startstream:
        parurl = parurl.replace('\\','').replace('"','').replace(',','')
        athu = athu.split('+')
        first = athu[1].split('.')[0].replace(' ','')
        second = re.findall('\("(.+?)"\)',athu[2])[0]
        wms1 = re.findall('var '+str(first)+' = \[(.+?)\];',str(REQ))[0]
        wms1 = wms1.replace('"','').replace(',','')
        wms2 = re.findall('id='+str(second)+'\>(.+?)\<',str(REQ))[0]
    stream = str(parurl)+str(wms1)+str(wms2)
    #stream = re.sub(r'//.+?\.streamlord\.com','//163.172.17.55',stream).encode('utf-8')  

    listitem =xbmcgui.ListItem (Name,'','',thumbnailImage)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(stream,listitem)
   
elif mode[0] == 'TVSHOWS':
    url = args['PAGE'][0]
    url = 'http://www.streamlord.com/'+url
    TVSHOWS = False
    MOVIES = False
    main(url)
    
elif mode[0] == 'NEXT':
    pager = int(args['PAGE'][0]) + 1
    choice = args['CHOICE'][0]
    pager = str(pager)
    if '?genre' in choice:
        url = choice.split('page=')[0]+'page='+pager
    else:
        url = choice.split('=')[0]+'='+pager
    if re.search('tvshows',str(url),re.I):
        TVSHOWS=True    
    elif re.search('genre',str(url),re.I):
        try:
            sep = url.split('genre-')[1].split('.html?')
            url = 'http://www.streamlord.com/movies.html?genre='+sep[0]+'&'+sep[1]
        except:
            pass
        MOVIES=True
    elif re.search('movies',str(url),re.I):
        MOVIES=True
    else:
        pass
    main(url)

elif mode[0] == "XML":
    base = args['base'][0]
    onetime = OPEN_URL(base)
    try:
        fanart = re.findall('<fanart>(.+?)</fanart>',str(onetime))[0]
    except:
        pass
    if ('<window>') in str(onetime):NEWWINDOW(onetime)
    stuff = re.compile('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>').findall(str(onetime))
    
    for title, url, icon in stuff:
        
        if not ('http') in url and not ('plugin') in url and not ('rtmp') in url and not ('rstp') in url and not ('base64') in url and len(url) > 2:
            url = english(url)
        if ('base64') in url:
            url = base64.b64decode(url[8:-1])
        if ('sdw-net') in url:
            url = build_url({'mode': 'shadow', 'name':title, 'icon':icon, 'url':url})    
        if ('youtube') in url and not 'plugin' in url:
            url = build_url({'mode': 'YouTube', 'name':title, 'icon':icon, 'url':url})
        if ('sawlive') in url:
            url = build_url({'mode': 'sawlive', 'name':title, 'icon':icon, 'url':url})
        if ('p2pcast') in url:
            url = build_url({'mode': 'P2P', 'name':title, 'icon':icon, 'url':url})
        if ('t-tv.org') in url:
            url = build_url({'mode': 'acestream', 'name':title, 'icon':icon, 'url':url})
        if ('sublink') in url:
            links = re.findall('<sublink>(.+?)</sublink>',str(url))
            for item in links:
                url = item
                addDirItem(title,icon,fanart,url)        
        else:
            pass
        addDirItem(title,icon,fanart,url)    
    endDir()
    
elif mode[0] =="YouTube":
    url = args['url'][0]
    name = args['name'][0]
    thumbnailImage = args['icon'][0]
    try:
        try:
            url = 'plugin://plugin.video.youtube/play/?video_id=' + str(url.split('v=')[1])
        except:
            url = xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id='+ url.split('v=')[1]+')')
            pass
    except:
        pass
    listitem =xbmcgui.ListItem(name, '','',thumbnailImage)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(url, listitem)

elif mode[0] =="shadow":
    url = args['url'][0]
    Name = args['name'][0]
    thumbnailImage = args['icon'][0]
    from resources.lib.resolvers import shadownet
    setter = shadownet.resolve(url)
    listitem = xbmcgui.ListItem (Name,'','',thumbnailImage)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(str(setter),listitem)
    
elif mode[0] == "P2P":
    url = args['url'][0]
    Name = args['name'][0]
    thumbnailImage = args['icon'][0]
    from resources.lib.resolvers import p2pcast
    stream = p2pcast.resolve(url)
    listitem =xbmcgui.ListItem (Name,'','',thumbnailImage)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(stream,listitem)

elif mode[0] == "sawlive":
    url = args['url'][0]
    Name = args['name'][0]
    thumbnailImage = args['icon'][0]
    from resources.lib.resolvers import sawlive
    stream = sawlive.resolve(url)
    listitem =xbmcgui.ListItem (Name,'','',thumbnailImage)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(stream,listitem)

elif mode[0] == "VT SPORTS":
    fanart = 'http://s18.postimg.org/yehmbqqy1/d0i0w_desktop_2418840_1920x1080.jpg'
    icon = args['icon'][0]
    url = 'http://www.wiz1.net'
    a = requests.get(url+'/schedule/')
    ans = a.text
    page = re.findall('iframe src="(.+?)"',ans)[0]
    game_page = requests.get(url+page)
    a =game_page.text
    b = a.split('<hr>')
    sports = re.compile('<a href="(.+?)" target="(.+?)">(.+?)</a>').findall(b[0])

    for url, blank, name in sports:
        name = name
        url =  url.replace('wiz1.net/','www.wiz1.net/watch')
        url = build_url({'mode': 'wiz1', 'name':name, 'icon':icon, 'url':url})
        addDirItem(name,icon,fanart,url)
        
    burl = 'http://www.ibrod.tv/index.html'
    req = cloudflare.request(burl)
    heading = client.parseDOM(req, 'a', attrs={'title':'Watch UK TV Online'})[0]
    slist = req.split(str(heading))[1].split('a class')[0]
    title = re.findall('title="(.+?)"',str(slist))
    turl = re.findall('href="(.+?)"',str(slist))
    joint = zip(title,turl)
    for title,turl in joint:
        title = title.replace('Watch ','').replace('Online','').upper()
        turl = 'http://www.ibrod.tv/'+str(turl)
        url = build_url({'mode': 'UKSPORT', 'name':title, 'icon':icon, 'url':turl})
        addDirItem(title,icon,fanart,url)
        
    channels = re.compile('(\d+?:\d+? )<font color=".+?"><b>(.+?)</b></font>(.+?)<a href="(.+?)" target=".+?">(.+?)<').findall(a)   
    for time, sport, detail, url, chan in channels:
        times = time.split(':')
        if times[0][0]=='0':
            if 0 <= int(times[0][1]) <= 9:
                stimes = int(times[0][1])
                time = str(int(stimes)- TIMESHIFT())+':'+str(times[1])
        else:
            time = str(int(times[0])- TIMESHIFT())+':'+str(times[1])
        newday = int(times[0]) - TIMESHIFT()
        if int(newday) >= 24:time = str(int(newday)-24)+":"+str(times[1])
        if ('-') in str(time):time = str(int(str(time).split(':')[0])+24)+':'+str(times[1])
        name = str(time) +' '+sport+'-'+detail[1:]
        url = url.replace('wiz','www.wiz').replace('annel','')+'?referer'+str(url)
        url = build_url({'mode': 'wiz1', 'name':name, 'icon':icon, 'url':url})
        addDirItem(name,icon,fanart,url)                            
    endDir()   

elif mode[0] =="wiz1":
    url = args['url'][0]
    Name = args['name'][0]
    thumbnailImage = args['icon'][0]
    site_url = cloudflare.request(url)                      
    url = re.findall('src="(.+?sawlive.+?)"',str(site_url))[0]
    from resources.lib.resolvers import sawlive
    stream = sawlive.resolve(url)
    listitem =xbmcgui.ListItem (Name,'','',thumbnailImage)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(stream,listitem)
    
elif mode[0] =="UKSPORT":
    url = args['url'][0]
    Name = args['name'][0]
    thumbnailImage = args['icon'][0]
    req = cloudflare.request(str(url))
    murl = re.findall('iframe .+? src="(.+?)"',str(req))[0]
    req = cloudflare.request(str(murl))
    url = re.findall('src="(http://mipl.+?)"',str(req))[0]
    url =url.encode('utf-8')
    from resources.lib.resolvers import miplayer
    url = miplayer.resolve(url)
    listitem =xbmcgui.ListItem (Name,'','',thumbnailImage)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(str(url),listitem)

elif mode[0]=="ACETV":
    murl = 'http://t-tv.org'
    req = client.request(murl)
    chunk = client.parseDOM(str(req), 'div', attrs={'id':'channels'})
    chunk = re.findall('<a href=(.+?)</a>',str(chunk))
    for item in chunk:
        urls = re.findall('"(/\?channel.+?)".+?data-favid="(.+?)"', str(item))
        try:
            icon = re.findall('src="(.+?)"',str(item))[0]
            icon = str(murl)+str(icon)+'?raw=true'
        except:
            icon = 'https://cdn3.iconfinder.com/data/icons/abstract-1/512/no_image-512.png'
        url = str(murl)+str(urls[0][0])
        name = str(urls[0][1]).replace('-',' ').upper()
        url = build_url({'mode': 'acestream', 'name':name, 'icon':icon, 'url':url})
        addDirItem(name,icon,fanart,url)
    endDir()
    
elif mode[0]=="acestream":
    url = args['url'][0]
    name = args['name'][0].upper()
    thumbnailImage = args['icon'][0]
    req = client.request(url)
    url = re.findall("var id = '(acestream://.+?)'",str(req))[0]
    url = str(url)+'&name='+str(name).replace(' ','+').encode('utf-8')
    url = xbmc.executebuiltin('PlayMedia(plugin://program.plexus/?mode=1&url='+str(url)+')')
   
    
elif mode[0] =="USTV RIGHT NOW":
    from resources.lib.indexers import ustv
    ustv.RIGHT()
    
elif mode[0] =="VIDTOONS":
    from resources.lib.indexers import vidtoons
    vidtoons.VidToon()
    
elif mode[0] =="VCartoonCraze":
    try:
        image = args['image'][0]
    except:
        image = mediaPath+'VidToonsLogo.png'
    try:
        fanart = args['fanart'][0]
    except:
        fanart = mediaPath+'VidToons.png'
    from resources.lib.indexers import vidtoons
    vidtoons.VCartoonCraze(image,fanart)
    
elif mode[0] =="VAnime":
    try:
        image = args['image'][0]
    except:
        image = mediaPath+'AnimeLogo.png'
    try:
        fanart = args['fanart'][0]
    except:
        fanart = mediaPath+'Anime.png'
    from resources.lib.indexers import vidtoons
    vidtoons.VAnime(image,fanart)

elif mode[0] =="VAalpha": 
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons
    vidtoons.VAalpha(image,fanart)

elif mode[0]=="VCalpha":
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons
    vidtoons.VCalpha(image,fanart)

elif mode[0]=="VAgenres":
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons
    vidtoons.VAgenres(image,fanart)
    
elif mode[0]=="VCgenres":
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons    
    vidtoons.VCgenres(image,fanart)

elif mode[0]=="VCcat":
    url = args['url'][0]
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons
    vidtoons.VCcat(url, image, fanart)
    
elif mode[0]=="VAcat":
    url = args['url'][0]
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons    
    vidtoons.VAcat(url, image, fanart)

elif mode[0]=="VCpart":
    url = args['url'][0]
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons
    vidtoons.VCpart(url, image, fanart)
    
elif mode[0]=="VApart":
    url = args['url'][0]
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons    
    vidtoons.VApart(url, image, fanart)

elif mode[0]=="VCsearch":
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons
    vidtoons.VCsearch(image, fanart)
    
elif mode[0]=="VAsearch":
    image = args['image'][0]
    fanart = args['fanart'][0]
    from resources.lib.indexers import vidtoons    
    vidtoons.VAsearch(image, fanart)

elif mode[0]=="VAstream":
    url = args['url'][0]
    from resources.lib.indexers import vidtoons
    vidtoons.VAstream(url)
    
elif mode[0]=="VCstream":
    url = args['url'][0]
    from resources.lib.indexers import vidtoons    
    vidtoons.VCstream(url)

elif mode[0]=='TV SHOWS - WEEKLY UPDATE':
    from resources.lib.indexers import Dizilab
    Dizilab.CCTV(fanart)

elif mode[0]=='CCfind':
    url = args['url'][0]
    from resources.lib.indexers import Dizilab
    Dizilab.CCfind(url)
