# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import urllib , urllib2 , sys , re , os , unicodedata
import xbmc , xbmcgui , xbmcplugin , xbmcaddon , base64
import time
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = int ( sys . argv [ 1 ] )
oo = xbmcaddon . Addon ( id = 'plugin.video.dragon.sports' )
i1iII1IiiIiI1 = oo . getAddonInfo ( 'name' )
iIiiiI1IiI1I1 = oo . getAddonInfo ( 'profile' )
o0OoOoOO00 = oo . getAddonInfo ( 'path' )
if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
o0OOO = True
if 13 - 13: ooOo + Ooo0O
try :
 IiiIII111iI = xbmc . getInfoLabel ( 'Network.MacAddress' )
 IiII = 0
 while IiiIII111iI == 'Busy' and IiII < 10 :
  time . sleep ( 3 )
  IiiIII111iI = xbmc . getInfoLabel ( 'Network.MacAddress' )
  IiII = IiII + 1
  if 28 - 28: Ii11111i * iiI1i1
 if IiiIII111iI == 'Busy' and IiII == 10 :
  IiiIII111iI = ""
  o0OOO = False
except Exception , i1I1ii1II1iII :
 IiiIII111iI = ""
 o0OOO = False
 if 86 - 86: oO0o
IIII = xbmc . translatePath ( os . path . join ( o0OoOoOO00 , 'fanart.jpg' ) )
Oo0oO0oo0oO00 = xbmc . translatePath ( os . path . join ( o0OoOoOO00 , 'icon.png' ) )
i111I = 'http://dragonstr.com/new_ds/index.php?mac=' + IiiIII111iI + '&method='
if 16 - 16: Oo0oO0ooo % IiIiI11iIi - O0OOo . O0Oooo00 . oo00 * I11
if 98 - 98: i11iIiiIii * Oo % O0OOo * O0OOo * OOOo0
if 79 - 79: O0Oooo00
def oOo0oooo00o ( url ) :
 try :
  oO0o0o0ooO0oO = urllib2 . Request ( url )
  oO0o0o0ooO0oO . add_header ( 'User-Agent' , ( "User-Agent:Mozilla/5.0 (Windows NT 6.2; WOW64)"
 "AppleWebKit/537.17 (KHTML, like Gecko)"
 "Chrome/24.0.1312.56" ) )
  oO0o0o0ooO0oO . add_header ( 'Referer' , 'http://dragonstr.com' )
  oo0o0O00 = urllib2 . urlopen ( oO0o0o0ooO0oO , timeout = 10 )
  oO = oo0o0O00 . read ( )
  oo0o0O00 . close ( )
  return oO
 except urllib2 . URLError , i1I1ii1II1iII :
  if 34 - 34: Oo0oO0ooo * Oo
  iiiI11 = 1
  pass
  if 91 - 91: Ooo0O / OOOo0 . Ii11111i + oO0o
def iI11 ( method ) :
 global o0OOO
 list = [ ]
 iII111ii = i111I + method
 if 3 - 3: O0OOo + O0
 oO = oOo0oooo00o ( iII111ii )
 if 42 - 42: oO0o / i1IIi + i11iIiiIii - IiIiI11iIi
 if oO == '0' :
  o0OOO = False
  oo0Ooo0 = xbmcgui . Dialog ( )
  oo0Ooo0 . ok ( 'Access Denied!' , 'To gain access update your firmware through the OTA Updater. If access is still denied contact support.' )
 else :
  I1I11I1I1I = r'title=(.+?)mode=(.+?)url=(.+?)icon=(.+?)fanart=(.+?)\n'
  for OooO0OO in re . finditer ( I1I11I1I1I , oO , re . DOTALL | re . IGNORECASE ) :
   iiiIi , IiIIIiI1I1 , OoO000 , IIiiIiI1 , iiIiIIi = OooO0OO . groups ( )
   if 65 - 65: ooOo
   iiiIi = iiiIi . strip ( )
   IiIIIiI1I1 = IiIIIiI1I1 . strip ( )
   OoO000 = OoO000 . strip ( )
   IIiiIiI1 = IIiiIiI1 . strip ( )
   iiIiIIi = iiIiIIi . strip ( )
   if 6 - 6: Oo / Ooo00oOo00o % IiIiI11iIi
   if iiIiIIi == 'default' :
    iiIiIIi = IIII
   ooOO0O00 ( iiiIi , OoO000 , IiIIIiI1I1 , IIiiIiI1 , iiIiIIi )
   if 20 - 20: OoooooooOO
   if 13 - 13: i1IIi - IiIiI11iIi % iiI1i1 / iIii1I11I1II1 % O0OOo
def ooO0o0Oo ( s ) :
 return '' . join ( ( c for c in unicodedata . normalize ( 'NFD' , s . decode ( 'utf-8' ) ) if unicodedata . category ( c ) != 'Mn' ) )
 if 78 - 78: iIii1I11I1II1 - IiIiI11iIi * I1IiI + Ooo0O + O0OOo + O0OOo
 if 11 - 11: O0OOo - I1IiI % I11 % O0OOo / ooOo - I1IiI
def o0o0oOOOo0oo ( url ) :
 o0oo0o0O00OO = [ 'tombstone6.com' , 'streamup.com' ]
 if 80 - 80: i1IIi
 for oOOO0o0o in o0oo0o0O00OO :
  if url . find ( oOOO0o0o ) != - 1 :
   return True
   if 26 - 26: OoooooooOO
 return False
 if 12 - 12: OoooooooOO % ooOo / I11 % Ooo0O
 if 29 - 29: OoooooooOO
def iI ( url ) :
 if 28 - 28: oO0o - O0Oooo00 . O0Oooo00 + ooOo - OoooooooOO + O0
 if 95 - 95: I1IiI % iiI1i1 . O0
 I1i1I = ''
 if 80 - 80: ooOo - I1IiI
 OOO00 = oOo0oooo00o ( url )
 if 21 - 21: OoooooooOO - OoooooooOO
 if url . find ( 'tombstone6.com' ) != - 1 :
  if 8 - 8: ooOo
  I1I11I1I1I = r'\'file\': "(.+?)",'
  OooO0OO = re . search ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE )
  I1i1I = OooO0OO . group ( 1 )
  if 60 - 60: Oo0oO0ooo / Oo0oO0ooo
 elif url . find ( 'streamup.com' ) != - 1 :
  I1I11I1I1I = r' url: "(.+?)" \+ window.Room.+?HlsManifestUrl: "//" \+ response \+ "(.+?)",'
  OooO0OO = re . search ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE )
  I1II1III11iii = OooO0OO . group ( 1 )
  Oo000 = OooO0OO . group ( 2 )
  if 51 - 51: i11iIiiIii . Oo + OOOo0
  if 10 - 10: Ii11111i * I11 * OOOo0 % IiIiI11iIi . oO0o + oo00
  IIiIi11i1 = url [ url . find ( '.com/' ) + 5 : url . find ( '/embed' ) ]
  IIIii1II1II = oOo0oooo00o ( I1II1III11iii + IIiIi11i1 )
  if 42 - 42: IiIiI11iIi + iiI1i1
  I1i1I = 'http://' + IIIii1II1II + Oo000
  if 76 - 76: oo00 - I1IiI
 return I1i1I
 if 70 - 70: I11
 if 61 - 61: Ii11111i . Ii11111i
def IIi1I1Ii11iI ( list ) :
 for I11i1I1I in list :
  if I11i1I1I [ 'url' ] . find ( 'm3u8' ) == - 1 and I11i1I1I [ 'url' ] . find ( 'rtmp' ) == - 1 and I11i1I1I [ 'url' ] . find ( '.mp4' ) == - 1 and not o0o0oOOOo0oo ( I11i1I1I [ 'url' ] ) :
   ooOO0O00 ( I11i1I1I [ 'title' ] , I11i1I1I [ 'url' ] , I11i1I1I [ 'mode' ] , I11i1I1I [ 'icon' ] , I11i1I1I [ 'fanart' ] )
  else :
   oO0Oo ( I11i1I1I [ 'title' ] , I11i1I1I [ 'url' ] , 15 , I11i1I1I [ 'icon' ] , I11i1I1I [ 'fanart' ] )
   if 54 - 54: Ooo0O - Oo + OoooooooOO
   if 70 - 70: IiIiI11iIi / Oo0oO0ooo . O0OOo % Ooo00oOo00o
def OOoOO00OOO0OO ( url ) :
 if 16 - 16: Oo * iiI1i1 % O0Oooo00
 list = [ ]
 if 86 - 86: Oo + IiIiI11iIi % i11iIiiIii * iiI1i1 . I11 * Oo0oO0ooo
 OOO00 = oOo0oooo00o ( url )
 if 44 - 44: iiI1i1
 I1I11I1I1I = r'<title>(.+?)</title><image>(.+?)</image><url>(.+?)</url>'
 for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
  o0o0oOoOO0 , iIi1iIiii111 , url = OooO0OO . groups ( )
  if 16 - 16: Ii11111i + I1IiI - OOOo0
  list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 11 , 'fanart' : '' , 'icon' : iIi1iIiii111 , 'url' : url } )
  if 85 - 85: ooOo + i1IIi
 IIi1I1Ii11iI ( list )
 if 58 - 58: OOOo0 * oO0o * Ii11111i / oO0o
 if 75 - 75: iiI1i1
def I1III ( url ) :
 list = [ ]
 if 63 - 63: oO0o % iiI1i1 * iiI1i1 * I1IiI / Ii11111i
 OOO00 = oOo0oooo00o ( url )
 if 74 - 74: OOOo0
 I1I11I1I1I = r'<title>(.+?)</title><image>(.+?)</image><url>(.+?)</url>'
 for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
  o0o0oOoOO0 , iIi1iIiii111 , url = OooO0OO . groups ( )
  if 75 - 75: Ooo0O . I11
  list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 15 , 'fanart' : '' , 'icon' : iIi1iIiii111 , 'url' : url } )
  if 54 - 54: OOOo0 % ooOo % Oo0oO0ooo % iIii1I11I1II1 + iIii1I11I1II1 * I11
 for I11i1I1I in list :
  oO0Oo ( I11i1I1I [ 'title' ] , I11i1I1I [ 'url' ] , I11i1I1I [ 'mode' ] , I11i1I1I [ 'icon' ] , I11i1I1I [ 'fanart' ] )
  if 87 - 87: I11 * Ooo00oOo00o % i11iIiiIii % ooOo - oO0o
  if 68 - 68: oo00 % i1IIi . O0Oooo00 . Ii11111i
def o0 ( method , type ) :
 list = [ ]
 iII111ii = ''
 oo0oOo = ''
 if 89 - 89: ooOo
 if type == 1 :
  if method in ( 'nhl' , 'nba' , 'nfl_new' ) :
   if method == 'nhl' :
    OO0oOoOO0oOO0 = 'http://nhlstream.net'
    oo0oOo = 'http://www.printyourbrackets.com/nhl-logos/'
   elif method == 'nba' :
    OO0oOoOO0oOO0 = 'http://nbastream.net'
    oo0oOo = 'http://www.printyourbrackets.com/nba-logos/'
   elif method == 'nfl_new' :
    OO0oOoOO0oOO0 = 'http://livenflstream.net'
    oo0oOo = 'http://www.printyourbrackets.com/nfl-logos/'
   else :
    return
    if 86 - 86: oO0o
   OOO00 = oOo0oooo00o ( OO0oOoOO0oOO0 )
   if 55 - 55: Ooo00oOo00o + iIii1I11I1II1 / ooOo * iiI1i1 - i11iIiiIii - IiIiI11iIi
   I1I11I1I1I = r'<a href= "([^"]+)" title= "(.)(.*?) at (.)(.*?)" style= "text-decoration:none; color:inherit;">\s.+?<strong>(.+?)</strong>'
   for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
    iII111ii , ii1ii1ii , oooooOoo0ooo , o0OoOoOO00 , I1I1IiI1 , time = OooO0OO . groups ( )
    if 5 - 5: Ooo0O * I11 + ooOo . oO0o + ooOo
    o0o0oOoOO0 = '[COLOR=white](' + time + ')[/COLOR] [COLOR=FF00FF00]' + ii1ii1ii + '[/COLOR][COLOR=blue]' + oooooOoo0ooo + ' [/COLOR] [COLOR=orange]@[/COLOR]  [COLOR=FF00FF00]' + o0OoOoOO00 + '[/COLOR][COLOR=blue]' + I1I1IiI1 + ' [/COLOR]'
    o0o0oOoOO0 = o0o0oOoOO0 . replace ( ' Live Stream' , '' )
    if 91 - 91: O0
    iII111ii = OO0oOoOO0oOO0 + '/' + iII111ii
    if 61 - 61: OOOo0
    Oo0oO0oo0oO00 = ( o0OoOoOO00 + I1I1IiI1 ) . replace ( ' Live Stream' , '' ) . replace ( ' ' , '-' ) . lower ( )
    if 64 - 64: I11 / ooOo - O0 - Oo0oO0ooo
    Oo0oO0oo0oO00 = oo0oOo + Oo0oO0oo0oO00 + '-logo.png'
    if 86 - 86: Oo0oO0ooo % ooOo / Oo / ooOo
    list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 22 , 'fanart' : '' , 'icon' : Oo0oO0oo0oO00 , 'url' : iII111ii } )
    if 42 - 42: I1IiI
   IIi1I1Ii11iI ( list )
   if 67 - 67: oo00 . O0OOo . O0
 elif type == 2 :
  OO0oOoOO0oOO0 = method
  if 10 - 10: Ii11111i % Ii11111i - iIii1I11I1II1 / oO0o + IiIiI11iIi
  OOO00 = oOo0oooo00o ( OO0oOoOO0oOO0 )
  if 87 - 87: iiI1i1 * Ii11111i + oO0o / iIii1I11I1II1 / O0OOo
  I1I11I1I1I = r'<a href=\'(.+?)\' target="video_iframe" class=\'newbutton\'>(.+?)</a>'
  for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
   iII111ii , o0o0oOoOO0 = OooO0OO . groups ( )
   if 37 - 37: O0OOo - I11 * iiI1i1 % i11iIiiIii - oo00
   iII111ii = OO0oOoOO0oOO0 [ : OO0oOoOO0oOO0 . rfind ( '/' ) ] + '/' + iII111ii
   print iII111ii
   if 83 - 83: Oo0oO0ooo / Oo
   if 34 - 34: O0Oooo00
   oOo = oOo0oooo00o ( iII111ii )
   oOO00Oo = r'iframe id=\'su-ivp\' src=\'(.+?)\' scrolling=\'no\''
   i1iIIIi1i = re . search ( oOO00Oo , oOo , re . DOTALL | re . IGNORECASE )
   iII111ii = i1iIIIi1i . group ( 1 )
   if 43 - 43: ooOo % oO0o
   list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 15 , 'fanart' : '' , 'icon' : '' , 'url' : iII111ii } )
   if 5 - 5: i11iIiiIii - i1IIi / iIii1I11I1II1
  IIi1I1Ii11iI ( list )
  if 26 - 26: Oo0oO0ooo . OoooooooOO
  if 39 - 39: O0OOo - O0 % i11iIiiIii * oo00 . O0Oooo00
def OOooo0O00o ( locatetv_url ) :
 list = [ ]
 if 85 - 85: Ooo0O - Ooo00oOo00o
 OOO00 = oOo0oooo00o ( locatetv_url )
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - Ooo0O
 I1I11I1I1I = r'<li class="time">(.+?)</li>\s.+?" href="(.+?)"><img src=".+?" title="(.+?)" alt="(.+?)"/>'
 for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
  time , iII111ii , o00oooO0Oo , Oo0oO0oo0oO00 = OooO0OO . groups ( )
  if 78 - 78: IiIiI11iIi % oo00 + Ii11111i
  o00oooO0Oo = o00oooO0Oo . replace ( '&#039;' , '\'' )
  if 64 - 64: iiI1i1 * O0 . Oo + OOOo0
  o0o0oOoOO0 = '[COLOR=FF00FF00](' + time + ')[/COLOR] [COLOR=blue]' + o00oooO0Oo + '[/COLOR]'
  if 6 - 6: ooOo / O0OOo . O0Oooo00 . O0Oooo00
  list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 21 , 'fanart' : '' , 'icon' : Oo0oO0oo0oO00 , 'url' : iII111ii } )
  if 62 - 62: Ii11111i + O0Oooo00 % O0OOo + oO0o
 IIi1I1Ii11iI ( list )
 if 33 - 33: O0 . O0Oooo00 . Oo
 if 72 - 72: i1IIi / I1IiI + OoooooooOO - Ooo00oOo00o
def iI1Iii ( minorleague_url ) :
 list = [ ]
 if 68 - 68: oO0o % oo00
 OOO00 = oOo0oooo00o ( minorleague_url )
 if 88 - 88: iIii1I11I1II1 - I11 + oO0o
 I1I11I1I1I = r'Game Time : (.+?)http://(.+?).m3u8'
 for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
  o0o0oOoOO0 , iII111ii = OooO0OO . groups ( )
  if 40 - 40: Oo * IiIiI11iIi + oO0o % O0OOo
  iII111ii = 'http://' + iII111ii + '.m3u8'
  if 74 - 74: iiI1i1 - Ooo00oOo00o + OoooooooOO + oo00 / ooOo
  list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 15 , 'fanart' : '' , 'icon' : '' , 'url' : iII111ii } )
  if 23 - 23: O0
 IIi1I1Ii11iI ( list )
 if 85 - 85: IiIiI11iIi
 if 84 - 84: Oo . iIii1I11I1II1 % OoooooooOO + IiIiI11iIi % OoooooooOO % I1IiI
def IIi1 ( onba_url ) :
 list = [ ]
 if 45 - 45: O0OOo / O0OOo + oo00 + I11
 OOO00 = oOo0oooo00o ( onba_url )
 if 47 - 47: Ooo0O + I11
 I1I11I1I1I = r'<p>([^"]+)<a href="([^"]+)/nlds/([^"]+)/([^"]+)/as/live/([^"]+)">'
 for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
  OoO , O00 , I1iI1 , iiiIi1 , i1I1ii11i1Iii = OooO0OO . groups ( )
  if 26 - 26: Oo0oO0ooo - iIii1I11I1II1 - Oo / I1IiI . ooOo % iIii1I11I1II1
  o0o0oOoOO0 = ( '[COLOR=FF00FF00]' + OoO + '[/COLOR][COLOR=blue]' + iiiIi1 + ' [/COLOR]' ) . replace ( 'bos' , 'Boston Celtics' ) . replace ( 'bkn' , 'Brooklyn Nets' ) . replace ( 'dal' , 'Dallas Maverics' ) . replace ( 'hou' , 'Houston Rockets' ) . replace ( 'nyk' , 'New York Knicks' ) . replace ( 'mem' , 'Memphis Grizzlies' ) . replace ( 'phi' , 'Philadelphia 76ers' ) . replace ( 'nop' , 'New Orleans Pelicans' ) . replace ( 'tor' , 'Toronto Raptors' ) . replace ( 'SAS' , 'San Antonio Spurs' ) . replace ( 'chi' , 'Chicago Bulls' ) . replace ( 'den' , 'Denver Nuggets' ) . replace ( 'cle' , 'Cleveland Cavaliers' ) . replace ( 'min' , 'Minnesota Timberwolves' ) . replace ( 'det' , 'Detroit Pistons' ) . replace ( 'okc' , 'Oklahoma City Thunder' ) . replace ( 'ind' , 'Indiana Pacers' ) . replace ( 'por' , 'Portland Trail Blazers' ) . replace ( 'mil' , 'Milwaukee Bucks' ) . replace ( 'uta' , 'Utah Jazz' ) . replace ( 'atl' , 'Atlanta Hawks' ) . replace ( 'gsw' , 'Golden State Warriors' ) . replace ( 'cha' , 'Charlotte Hornets' ) . replace ( 'lac' , 'Los Angeles Clippers' ) . replace ( 'mia' , 'Miami Heat' ) . replace ( 'lal' , 'Los Angeles Lakers' ) . replace ( 'orl' , 'Orlando Magic' ) . replace ( 'phx' , 'Phoenix Suns' ) . replace ( 'was' , 'Washington Wizards' ) . replace ( 'sac' , 'Sacramento Kings' )
  if 91 - 91: Ooo0O . iIii1I11I1II1 / iiI1i1 + i1IIi
  iII111ii = O00 + '/nlds/' + I1iI1 + '/' + iiiIi1 + '/as/live/' + i1I1ii11i1Iii
  if 42 - 42: I11 . Ooo0O . I11 - Ii11111i
  list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 37 , 'fanart' : '' , 'icon' : '' , 'url' : iII111ii } )
  if 40 - 40: I11 - i11iIiiIii / IiIiI11iIi
 IIi1I1Ii11iI ( list )
 if 35 - 35: IiIiI11iIi - Oo % Ooo0O . OoooooooOO % IiIiI11iIi
def I1i1Iiiii ( wnet_url , url_type ) :
 list = [ ]
 if 94 - 94: Ooo0O * IiIiI11iIi / Ooo00oOo00o / IiIiI11iIi
 OOO00 = oOo0oooo00o ( wnet_url )
 if 87 - 87: Ooo00oOo00o . O0Oooo00
 if ( url_type == 1 ) :
  I1I11I1I1I = r'<a class="clip-link" data-id=".+?" title="(.)(.*?)" href="(.+?)">.+?<img src="(.+?)"'
  for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
   O0OO0O , OO , iII111ii , Oo0oO0oo0oO00 = OooO0OO . groups ( )
   if 83 - 83: O0 / Oo - I1IiI - oO0o
   o0o0oOoOO0 = '[COLOR=FF00FF00]' + O0OO0O + '[/COLOR][COLOR=blue]' + OO + ' [/COLOR]'
   if 36 - 36: O0Oooo00
   list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 34 , 'fanart' : '' , 'icon' : Oo0oO0oo0oO00 , 'url' : iII111ii } )
 elif ( url_type == 2 ) :
  I1I11I1I1I = r'return false;"  href="(.+?)">(.)(.*?)</a>'
  for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
   iII111ii , O0OO0O , OO = OooO0OO . groups ( )
   if 36 - 36: I11 / O0 * Ooo00oOo00o - oO0o % iIii1I11I1II1 * iiI1i1
   o0o0oOoOO0 = '[COLOR=FF00FF00]' + O0OO0O + '[/COLOR][COLOR=blue]' + OO + ' [/COLOR]'
   if 79 - 79: O0
   iII111ii = 'http://www.dailymotion.com/embed/video/' + iII111ii . split ( '/' ) [ 4 ]
   if 78 - 78: Ii11111i + oO0o - oo00
   list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 35 , 'fanart' : '' , 'icon' : '' , 'url' : iII111ii } )
   if 38 - 38: Ooo0O - iiI1i1 + iIii1I11I1II1 / ooOo % Ooo00oOo00o
 elif ( url_type == 3 ) :
  I1I11I1I1I = r'}],"(.)(.*?)":.+?"url":"(.+?)"'
  for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
   O0OO0O , OO , iII111ii = OooO0OO . groups ( )
   if 57 - 57: I1IiI / I11
   o0o0oOoOO0 = '[COLOR=FF00FF00]' + O0OO0O + '[/COLOR][COLOR=blue]' + OO + ' [/COLOR]'
   if 29 - 29: iIii1I11I1II1 + ooOo * I1IiI * oO0o . Oo * Oo
   iII111ii = iII111ii . replace ( '\/' , '/' )
   if 7 - 7: O0Oooo00 * oo00 % IiIiI11iIi - Ooo0O
   list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 15 , 'fanart' : '' , 'icon' : '' , 'url' : iII111ii } )
   if 13 - 13: IiIiI11iIi . i11iIiiIii
 IIi1I1Ii11iI ( list )
 if 56 - 56: Ii11111i % O0 - Oo
 if 100 - 100: IiIiI11iIi - O0 % iiI1i1 * oO0o + Oo
def Oo0O0oooo ( ilive_url , url_type ) :
 if 33 - 33: oo00 + O0OOo * iiI1i1 / iIii1I11I1II1 - Oo
 list = [ ]
 if 54 - 54: oo00 / oO0o . iiI1i1 % O0OOo
 OOO00 = oOo0oooo00o ( ilive_url )
 if 57 - 57: i11iIiiIii . Ii11111i - IiIiI11iIi - iiI1i1 + ooOo
 if ( url_type == 1 ) :
  I1I11I1I1I = r'<noscript><img.*?src="([^"]+)".*?/></noscript>\s*</a>\s*<a href="[^"]+live\.to[^\d]+([\d]+)[^"]+"><strong>([^<\t\n]+)'
  for OooO0OO in re . finditer ( I1I11I1I1I , OOO00 , re . DOTALL | re . IGNORECASE ) :
   Oo0oO0oo0oO00 , iII111ii , o0o0oOoOO0 = OooO0OO . groups ( )
   if 63 - 63: ooOo * O0OOo
   list . append ( { 'title' : o0o0oOoOO0 , 'mode' : 36 , 'fanart' : '' , 'icon' : Oo0oO0oo0oO00 , 'url' : iII111ii } )
   if 69 - 69: O0 . I1IiI
 IIi1I1Ii11iI ( list )
 if 49 - 49: Oo - Oo0oO0ooo
 if 74 - 74: iIii1I11I1II1 * Ii11111i + ooOo / i1IIi / OOOo0 . Ooo00oOo00o
def oooOo0OOOoo0 ( url ) :
 if 51 - 51: Ooo00oOo00o / ooOo . oO0o * Ooo0O + I1IiI * O0Oooo00
 if o0o0oOOOo0oo ( url ) :
  url = iI ( url )
  if 73 - 73: I1IiI + OoooooooOO - O0 - IiIiI11iIi - OOOo0
 O0O ( url )
 if 80 - 80: IiIiI11iIi * Ooo0O / Ooo0O
 if 5 - 5: Oo
def O0O ( url ) :
 iIiIi11iI = url
 Oo0O00O000 = xbmcgui . ListItem ( i11I1IiII1i1i , path = iIiIi11iI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0O00O000 )
 return
 if 95 - 95: i11iIiiIii
def iI1111iiii ( ) :
 Oo0OO = [ ]
 O0OooOo0o = sys . argv [ 2 ]
 if len ( O0OooOo0o ) >= 2 :
  iiI11ii1I1 = sys . argv [ 2 ]
  Ooo0OOoOoO0 = iiI11ii1I1 . replace ( '?' , '' )
  if ( iiI11ii1I1 [ len ( iiI11ii1I1 ) - 1 ] == '/' ) :
   iiI11ii1I1 = iiI11ii1I1 [ 0 : len ( iiI11ii1I1 ) - 2 ]
  oOo0OOoO0 = Ooo0OOoOoO0 . split ( '&' )
  Oo0OO = { }
  for II in range ( len ( oOo0OOoO0 ) ) :
   o0Oo0oO0oOO00 = { }
   o0Oo0oO0oOO00 = oOo0OOoO0 [ II ] . split ( '=' )
   if ( len ( o0Oo0oO0oOO00 ) ) == 2 :
    Oo0OO [ o0Oo0oO0oOO00 [ 0 ] ] = o0Oo0oO0oOO00 [ 1 ]
 return Oo0OO
 if 92 - 92: OoooooooOO * oo00
def ooOO0O00 ( name , url , mode , iconimage , fanart ) :
 o0000oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 I1II1 = True
 oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oooO . setProperty ( 'fanart_image' , fanart )
 I1II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0000oO , listitem = oooO , isFolder = True )
 return I1II1
 if 26 - 26: IiIiI11iIi % Ii11111i
def oO0Oo ( name , url , mode , iconimage , fanart ) :
 o0000oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 oooO = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oooO . setProperty ( 'fanart_image' , fanart )
 oooO . setProperty ( 'IsPlayable' , 'true' )
 I1II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0000oO , listitem = oooO )
 if 76 - 76: O0Oooo00 * O0OOo
iiI11ii1I1 = iI1111iiii ( )
iII111ii = None
i11I1IiII1i1i = None
ooooooo00o = None
o0oooOO00 = None
if 32 - 32: oo00
try :
 iII111ii = urllib . unquote_plus ( iiI11ii1I1 [ "url" ] )
except :
 pass
try :
 i11I1IiII1i1i = urllib . unquote_plus ( iiI11ii1I1 [ "name" ] )
except :
 pass
try :
 ooooooo00o = int ( iiI11ii1I1 [ "mode" ] )
except :
 pass
try :
 o0oooOO00 = urllib . unquote_plus ( iiI11ii1I1 [ "iconimage" ] )
except :
 pass
 if 30 - 30: iIii1I11I1II1 / Oo0oO0ooo . I1IiI - Ooo0O
 if 48 - 48: i1IIi - IiIiI11iIi / O0 * I1IiI
 if 71 - 71: Ii11111i
 if 7 - 7: Ii11111i - Oo . iIii1I11I1II1 - i1IIi
 if 59 - 59: Ooo0O
 if 81 - 81: ooOo - ooOo . O0OOo
if ooooooo00o == None or iII111ii == None or len ( iII111ii ) < 1 :
 iI11 ( 'main_menu' )
 if 73 - 73: Oo0oO0ooo % i11iIiiIii - Oo
elif ooooooo00o == 1 :
 iI11 ( iII111ii )
 if 7 - 7: O0 * i11iIiiIii * IiIiI11iIi + I11 % I1IiI - I11
elif ooooooo00o == 11 :
 OOoOO00OOO0OO ( iII111ii )
 if 39 - 39: Ooo00oOo00o * oO0o % oO0o - OoooooooOO + Ooo0O - Oo0oO0ooo
elif ooooooo00o == 12 :
 I1III ( iII111ii )
 if 23 - 23: i11iIiiIii
elif ooooooo00o == 15 :
 oooOo0OOOoo0 ( iII111ii )
 if 30 - 30: Ooo0O - i1IIi % OOOo0 + Oo0oO0ooo * iIii1I11I1II1
elif ooooooo00o == 21 :
 o0 ( iII111ii , 1 )
 if 81 - 81: O0Oooo00 % i1IIi . iIii1I11I1II1
elif ooooooo00o == 22 :
 o0 ( iII111ii , 2 )
 if 4 - 4: i11iIiiIii % I1IiI % i1IIi / O0Oooo00
elif ooooooo00o == 23 :
 o0 ( iII111ii , 3 )
 if 6 - 6: O0OOo / Oo % oO0o - Oo
elif ooooooo00o == 31 :
 OOooo0O00o ( iII111ii )
 if 31 - 31: oO0o
elif ooooooo00o == 32 :
 iI1Iii ( iII111ii )
 if 23 - 23: oo00 . O0Oooo00
elif ooooooo00o == 33 :
 I1i1Iiiii ( iII111ii , 1 )
 if 92 - 92: ooOo + oo00 * IiIiI11iIi % Oo
elif ooooooo00o == 34 :
 I1i1Iiiii ( iII111ii , 2 )
 if 42 - 42: Ooo00oOo00o
elif ooooooo00o == 35 :
 I1i1Iiiii ( iII111ii , 3 )
 if 76 - 76: Oo * O0OOo % oo00
elif ooooooo00o == 36 :
 Oo0O0oooo ( iII111ii , 1 )
 if 57 - 57: iIii1I11I1II1 - i1IIi / oo00 - O0 * OoooooooOO % OOOo0
elif ooooooo00o == 37 :
 IIi1 ( iII111ii )
 if 68 - 68: OoooooooOO * Oo0oO0ooo % ooOo - O0Oooo00
if o0OOO :
 xbmcplugin . endOfDirectory ( o0OO00 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
