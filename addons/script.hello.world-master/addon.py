import xbmcaddon
import xbmcgui
import subprocess


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


def update():
    subprocess.call('cd /home/osmc/.kodi/', shell=True)
    subprocess.Popen("git pull")




dialog = xbmcgui.Dialog()
i = dialog.yesno("Max TV Wizard", "Would you like to update your box now?")

if i == 0:
    pass

else:
    dialog.ok("Max TV Wizard", "Please restart box after update.")
    update()
