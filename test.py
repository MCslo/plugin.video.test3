from bs4 import BeautifulSoup
import urllib2
import re

#risanje mej
def limiter():
	return "++++++++++++++" 

htmlpage = urllib2.urlopen("http://www.teamliquid.net/")
soup = BeautifulSoup(htmlpage,from_encoding="utf-8")

for link in soup.find_all('a',attrs={'href': re.compile("^/video/streams/")}):
	if link == "/video/streams/":
		pass
	else:
		print link['href']


print "LIVE STREAM LINKS******************************************************************\
**************************************************************************"

#Upcoming events

table = soup.find("div",{"style":"font-size: 8pt;padding-top:7px"}).find_all("tr")

list1 = []	
for td in table:
	a = td.find(text=True)
	b = td.a['title'].encode('utf-8')
	
	list1.append([a,b])
	
#print list1

"""def add_upcoming_item(cas,vsebina,img):
    listitem = xbmcgui.ListItem(infolabels['title'], 
        iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable','false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem,isFolder=False)

for x in xrange(0,9):
	add_upcoming_item(cas, list1[x,[0]], img)
	

xbmcplugin.endOfDirectory(plugin_handle)


"""



#Get the title of first on air section
for section in soup.find("div",{"style":"font-size: 8pt;padding-top:7px"}).find_all("strong"):
	nextNode = section
	print section

	while True:
		nextStrong = nextNode.next_sibling
		try: 
			nextTitle = nextStrong.find("strong").find(text=True)
			print nextTitle.encode('utf-8')
		except AttributeError:
			print "wrong Attribute"

		

		try:
			tagName = nextNode.name
		except AttributeError:
			tagName="" 
		if tagName == "div":
			print nextNode.string
		else:
			print "########"
			break










title1= soup.find("div",{"style":"font-size: 8pt;padding-top:7px"}).find_all("strong")

num_of_strong = len(title1)
num_of_strong_fixed = len(title1)

while num_of_strong > 1:
	#print title1[num_of_strong_fixed - num_of_strong]
	title2 = soup.find("div",{"style":"font-size: 8pt;padding-top:7px"}).find_all("strong")[num_of_strong_fixed - num_of_strong].find(text=True)
	print limiter()
	print title2.encode('utf-8')
	

	
	num_of_strong-=1




#print title1.encode('utf-8')


for link in soup.find_all("div",{"style":"margin-left:8px;margin-bottom:2px"}):
	print link


print "ON AIR******************************************************************\
**************************************************************************"

upcoming = soup.find('div',id="span_more_events").previous_sibling.previous_sibling

upcoming_exp = soup.find('div',id="span_more_events")

print upcoming
print upcoming_exp

print "UPCOMING EVENTS ******************************************************************\
**************************************************************************" + limiter()




