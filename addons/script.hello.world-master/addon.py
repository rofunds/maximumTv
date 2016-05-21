import xbmcaddon
import xbmcgui
import subprocess


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


def update():
    subprocess.Popen("git pull", cwd = "C:\\Program Files (x86)\\Kodi\\")
    #subprocess.cwd('C:\\Program Files (x86)\\Kodi\\addons')k
    #subprocess.call(["git pull"])
    #os.chdir("home//osmc//.kodi//")
    #os.chdir("C:\\Program Files (x86)\\Kodi\\addons")
    #os.system("cd", "git pull")



line1 = "Do you want to update your box at this time?"


dialog = xbmcgui.Dialog()
i = dialog.yesno("Max TV Wizard", "Would you like to update your box now?")

if i == 0:
    pass

else:
    update()
