#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmcaddon,base64,socket
from bs4 import BeautifulSoup


















plugin_handle=int(sys.argv[1])

def add_video_item(url,infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], 
        iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable','true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem,isFolder=False)


base_url='http://cdn.jerryseinfeld.com/assets'
html = urllib2.urlopen('http://www.jerryseinfeld.com/').read()
for v in re.finditer('"title":"(.+?)","filename":"(.+?)"'+
    ',"appearance":"(.+?)","venue":"(.+?)"', html):
    title, filename, year, venue = v.groups()
    add_video_item('%s/%s.mp4' % (base_url,filename),
        {'title': '%s (%s,%s)' % (title,venue, year),
        'year': int(year)},
        '%s/%s.jpg' % (base_url, filename))

xbmcplugin.endOfDirectory(plugin_handle)


