import xbmcaddon
import xbmcgui
import subprocess
import os


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


def update():
    wd = os.getcwd()
    subprocess.call('cd /home/osmc/.kodi/', shell=True)
    subprocess.Popen("git pull")




dialog = xbmcgui.Dialog()
i = dialog.yesno("Max TV Wizard", wd)

if i == 0:
    pass

else:
    dialog.ok("Max TV Wizard", "Please restart box after update.")
    update()
