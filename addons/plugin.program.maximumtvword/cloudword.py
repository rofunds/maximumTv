import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

import downloaderold
import extract
import socket, fcntl, struct

ADDON = xbmcaddon.Addon(id='plugin.program.UpdateSports')

def CLOUDINSTALL():
        dialog = xbmcgui.Dialog()      
        dp = xbmcgui.DialogProgress()
        dp.create("Cloudword","Cloud Download",'', 'In Progress...')
        keyword      =  SEARCH()
        url ='http://www.maximumtv.info/form.php?keyword=sports6'+'&m1='+getHwAddr('eth0')
        path         =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
        lib          =  os.path.join(path, keyword+'.zip')
        addonfolder  =  xbmc.translatePath(os.path.join('special://home',''))
        
        downloaderold.download(url,lib)
        dp = xbmcgui.DialogProgress()
        dp.create("Cloudword","Cloud Install",'', 'In Progress...')
        dp.update(0,"", "SETUP NOW")
        extract.all(lib,addonfolder,dp)
        xbmc.executebuiltin('UpdateLocalAddons')
        xbmc.executebuiltin( 'UpdateAddonRepos' )
        dialog.ok("CLOUDWORD", "Cloud Setup Complete","", "[COLOR red]All Done Press Ok[/COLOR]")
	        
def SEARCH():
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Enter CLOUDWORD')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered =  keyboard.getText() .replace(' ','%20')
            if search_entered == None:
                return False          
        return search_entered    

def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
        pass
    except IOError:
        # do this
        return ''
        pass
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]        
    
url=None
name=None
mode=None
iconimage=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        CLOUDINSTALL()
