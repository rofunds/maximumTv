# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para TV3
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

#import urlparse,urllib2,urllib,re
#import os
#from core import config

import re
from core import scrapertools
from core import logger
from core import jsontools

def get_video_url(page_url, premium = False, user="", password="", video_password="", page_data=""):

    logger.info("[tv3.py] get_video_url(page_url='%s')" % page_url)

    video = []
    urlbase = "http://dinamics.ccma.cat/pvideo/media.jsp?media=video&version=0s&idint=%s&profile=tv"

    try:

        # Se mira si la URL tiene el formato nuevo o el antiguo y entonces se usa un patrón u otro para extraer
        # el número de video, que es lo único que importa para obtener en última instancia la URL del video en MP4.
        # Precondición: los dos únicos tipos de URLs que pueden llegar aquí son, por ejemplo:
        # http://www.ccma.cat/tv3/alacarta/telenoticies/telenoticies-vespre-17042015/video/5505723/
        # http://www.tv3.cat/videos/5495372/La-baldana
        #
        if page_url.startswith("http://www.ccma.cat"):
            patron = '/tv3/alacarta/.*?/.*?/video/(\d+)'
        else:
            patron = '/videos/(\d+)/.*?'

        matches = re.compile(patron,re.DOTALL).findall(page_url)
        data = scrapertools.cachePage(urlbase % matches[0])
        response = jsontools.load_json(data.decode('iso-8859-1').encode('utf8'))
        video.append([ "HTTP [mp4]", response['media']['url']])

    except:
        import traceback
        logger.info(traceback.format_exc())

    return video

