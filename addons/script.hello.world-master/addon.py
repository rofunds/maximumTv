import xbmcaddon
import xbmcgui
import subprocess


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


def update():
    #subprocess.Popen("git pull", cwd = "//home//osmc//.kodi//")
    os.chdir("//home//osmc//.kodi//")
    os.sysytem("git pull")



dialog = xbmcgui.Dialog()
i = dialog.yesno("Max TV Wizard", "Would you like to update your box now?")

if i == 0:
    pass

else:
    dialog.ok("Max TV Wizard", "Please restart box after update.")
    update()
