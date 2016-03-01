#!/usr/bin/python
import re 
import urllib

def getHtml(url): 
    page = urllib.urlopen(url)
    html = page.read()
    return html 
def getImg(html):
    reg = r'src="(.*?\.jpg)"><'
    imglist = re.findall(reg, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, "%s.jpg" % x)
        x+=1

html = getHtml("http://pic.gamersky.com/HTML/183933.shtml")
getImg(html)
