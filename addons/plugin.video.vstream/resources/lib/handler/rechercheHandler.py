#-*- coding: utf-8 -*-
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui

import sys
import os
import urllib
import xbmcgui

class cRechercheHandler:
    
    def __init__(self):
        self.__sText = ""
        self.__sDisp = ""

    def getPluginHandle(self):
        try:
            return int( sys.argv[ 1 ] )
        except:
            return 0

    def getPluginPath(self):
        try:
            return sys.argv[0]
        except:
            return ''
            
    def setText(self, sText):
        self.__sText = sText

    def getText(self):
        if not self.__sText:
            oGui = cGui()
            sSearchText = oGui.showKeyBoard()
            self.__sText = urllib.quote(sSearchText)
        return self.__sText
        

    def setDisp(self, sDisp):
        self.__sDisp = sDisp

    def getDisp(self):
        if not self.__sDisp:
            disp = ['search1','search2','search3','search4']
            dialog2 = xbmcgui.Dialog()
            dialog_select = [cConfig().getSetting('search1_label'), cConfig().getSetting('search2_label'), cConfig().getSetting('search3_label'), cConfig().getSetting('search4_label')]

            ret = dialog2.select('Select Recherche',dialog_select)
    
            if ret > -1:
                self.__sDisp = disp[ret]
        return self.__sDisp

    def __getFileNamesFromFolder(self, sFolder):
        aNameList = []
        #items = os.listdir(sFolder)
        items = os.listdir(unicode(sFolder, 'utf-8'))

        for sItemName in items:
            #sFilePath = os.path.join(sFolder, sItemName)
            sFilePath = os.path.join(unicode(sFolder, 'utf-8'), sItemName)
            # xbox hack
            sFilePath = sFilePath.replace('\\', '/')
            
            if (os.path.isdir(sFilePath) == False):
                #if (str(sFilePath.lower()).endswith('py')):
                if (sFilePath.lower().endswith('py')):
                    sItemName = sItemName.replace('.py', '')
                    aNameList.append(sItemName)
        return aNameList

    def __importPlugin(self, sName, sLabel, sText):
        oConfig = cConfig()
        sPluginSettingsName = sLabel+'_' +sName
        bPlugin = oConfig.getSetting(sPluginSettingsName)
        
        OnPlugins = oConfig.getSetting('plugin_' + sName)
        

        if (bPlugin == 'true') and (OnPlugins == 'true'):    
            try:
                oGui = cGui()
                oGui.addText(sName,'[COLOR olive]'+sName+'[/COLOR]')
                cConfig().log("Load Recherche: " + str(sName))
                exec "from resources.sites import " + sName
                exec "sSearch = " + sName + ".URL_SEARCH"
                #exec "sFunction = " + sName + ".FUNCTION_SEARCH"
                #sPluginSettingsName = sLabel+'_' + sName
                sUrl = sSearch[0]+sText
                
                searchUrl = "%s.%s('%s')" % (sName, sSearch[1], sUrl)
                exec searchUrl   
                return True
            except Exception, e:
                cConfig().log("cant import plugin: " + str(sName))            
                return False, False
        else:
            #cConfig().log("cant import plugin: " + str(sName))            
            return False, False
            

    def getRootFolder(self):        
        sRootFolder = cConfig().getAddonPath()
        cConfig().log("Root Folder: " + sRootFolder)
        return sRootFolder
        
    def getRootArt(self):
        oConfig = cConfig()

        sFolder =  self.getRootFolder()
        sFolder = os.path.join(sFolder, 'resources/art/')
       
        sFolder = sFolder.replace('\\', '/')
        return sFolder

    def getAvailablePlugins(self):
        oConfig = cConfig()
        sText = self.getText()
        if not sText:
            return False
        sLabel = self.getDisp()
        sFolder =  self.getRootFolder()
        sFolder = os.path.join(sFolder, 'resources/sites')

        # xbox hack        
        sFolder = sFolder.replace('\\', '/')
        cConfig().log("Sites Folder: " + sFolder)
        
        aFileNames = self.__getFileNamesFromFolder(sFolder)

        aPlugins = []
        for sFileName in aFileNames:
                
            aPlugin = self.__importPlugin(sFileName, sLabel, sText)

        return True

    def __createAvailablePluginsItem(self, sPluginName, sPluginIdentifier, sPluginDesc):
        aPluginEntry = []
        aPluginEntry.append(sPluginName)
        aPluginEntry.append(sPluginIdentifier)
        aPluginEntry.append(sPluginDesc)
        return aPluginEntry