from bs4 import BeautifulSoup
import html5lib
import urllib2,re,xbmc,xbmcgui,xbmcplugin,xbmcaddon,sys,urllib2,urllib

htmlpage = urllib2.urlopen("http://www.teamliquid.net/")
soup = BeautifulSoup(htmlpage,from_encoding="utf-8")
my_addon = xbmcaddon.Addon('plugin.video.test3')



#Extracting upcoming section from TeamLiquid page and saving the time and title into a list
def getUpcoming():

    listUpcoming = []

    for extract1 in soup.body.table.find("table",{"class":"upcoming"}).find_all("tr"):
    	time = extract1.find(text=True)
    	title = extract1.a['title']
    	listUpcoming.append([time,title])

    return listUpcoming

#GUI part

thisPlugin = int(sys.argv[1])
settings = xbmcaddon.Addon(id='plugin.video.test3')
translation = settings.getLocalizedString

def addDir(name,url,mode,iconimage,index=0):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&siteIndex="+str(index)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def MainMenu():
    addDir(translation(30001),'','playing_now','')
    addDir(translation(30002),'','player_streams','')
    addDir(translation(30003),'','upcoming','')
    xbmcplugin.endOfDirectory(thisPlugin)


def parameters_string_to_dict(parameters):
        # Convert parameters encoded in a URL to a dict.
        paramDict = {}
        if parameters:
            paramPairs = parameters[1:].split("&")
            for paramsPair in paramPairs:
                paramSplits = paramsPair.split('=')
                if (len(paramSplits)) == 2:
                    paramDict[paramSplits[0]] = paramSplits[1]
        return paramDict


def Upcoming():
    a=getUpcoming()
    global thisPlugin
    for item in a:
        piece=xbmcgui.ListItem(str(item[1])+translation(30010)+str(item[0]))
        xbmcplugin.addDirectoryItem(thisPlugin,'',piece)

    xbmcplugin.endOfDirectory(thisPlugin)

    




params=parameters_string_to_dict(sys.argv[2])
mode=params.get('mode')
url=params.get('url')
sIndex=params.get('siteIndex')

print sys.argv 

if mode == 'playing_now':
  print "1"
elif mode == 'player_streams':
  print "2"
elif mode == 'upcoming':
  Upcoming()

else:
  MainMenu()

