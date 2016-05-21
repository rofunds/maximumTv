import xbmcaddon
import xbmcgui
import os


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


def update():
    os.system('sh git.sh')




dialog = xbmcgui.Dialog()
i = dialog.yesno("Max TV Wizard", "Would you like to update your box?")

if i == 0:
    pass

else:
    dialog.ok("Max TV Wizard", "Please restart box after update.")
    update()
