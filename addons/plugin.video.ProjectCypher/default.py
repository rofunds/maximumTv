import urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, base64


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = '[B]          Welcome to The Future of TV[/B]'
line2 = '[B]Plexus[/B] addon is required for P2P sports channels'
line3 = '         Project Cypher Streaming since 2012'

 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)

plugin_handle = int(sys.argv[1])

_id = 'plugin.video.ProjectCypher'
_icondir = "special://home/addons/" + _id + "/icons/"
_resources = "special://home/addons/" + _id + "/resources/"

fanart = "special://home/addons/" + _id + '/fanart.jpg'
icon = xbmc.translatePath(os.path.join('special://home/addons/' + _id, 'icon.png'))

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)
	
def add_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'False')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=True)


# hdsdtv

add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/ProjectCypherTV.m3u',{ 'title': 'Project Cypher Live TV'}, '%s/procyp.png'% _icondir)

# sport tv

add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/sport.m3u',{ 'title': 'Project Cypher Sports TV'}, '%s/sport.png'% _icondir)

# Wsport tv

add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/worldsport.m3u',{ 'title': 'Live World Sports Channels'}, '%s/wsport.png' % _icondir)

# adult

add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/ProjectCypherAdult.m3u',{ 'title': 'Project Cypher Adult'}, '%s/adult.png'% _icondir)

# cams

add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/WorldCams.m3u',{ 'title': 'Project Cypher World Cams'}, '%s/earthcam.png'% _icondir)

# sports

add_video_item('http://bigten247.cdnak.bigtenhd.neulion.com/nlds/btn2go/btnnetwork/as/live/btnnetwork_hd_3000.m3u8',{ 'title': 'Big Ten Network 720p HD'}, '%s/big10.png' % _icondir)
add_video_item('http://tvenbcsn-i.Akamaihd.net/hls/live/218235/nbcsnx/2596k/prog.m3u8|X-Forwarded-For=209.239.112.104',{ 'title': 'NBCSN 720p HD'}, '%s/nbcsn.png' % _icondir)
add_video_item('http://nflsvglagame1-i.akamaihd.net/hls/live/223206/NFL_Mobile/2015Mobile_NFLN_5000k.m3u8',{ 'title': 'NFL 720p HD'}, '%s/NFL.png' % _icondir)
add_video_item('http://nflioslivesvg2-i.akamaihd.net/hls/live/221521/nflioslive/2015HackerNow_w99d9.m3u8',{ 'title': 'NFL Now 720p HD'}, '%s/nfl-now.png' % _icondir)

# nasa

add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/nasa.m3u',{ 'title': 'Project Cypher NASA'}, '%s/nasa.png'% _icondir)


#LFL

add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/ppvevents.m3u',{ 'title': 'PPV/SPORTS EVENTS LIVE'}, '%s/ppv.png'% _icondir)


add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/lflvod.m3u',{ 'title': 'Project Cypher LFL VOD'}, '%s/lfl.png'% _icondir)
add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/ufcvod.m3u',{ 'title': 'Project Cypher UFC VOD'}, '%s/ufc.png'% _icondir)
add_video_item('https://raw.githubusercontent.com/FutuHDware/streams/master/test.m3u',{ 'title': 'Project Cypher TEST AREA'}, '%s/Test.png'% _icondir)



xbmcplugin.endOfDirectory(int(sys.argv[1]))

xbmc.executebuiltin("Container.SetViewMode(500)")

