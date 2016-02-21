import urllib2
import re
import os
from os.path import basename
from urlparse import urlsplit
from urlparse import urlparse
from posixpath import basename,dirname
 
## function that processes url, if there are any spaces it replaces with '%20' ##
 
def process_url(raw_url):
 if ' ' not in raw_url[-1]:
     raw_url=raw_url.replace(' ','%20')
     return raw_url
 elif ' ' in raw_url[-1]:
     raw_url=raw_url[:-1]
     raw_url=raw_url.replace(' ','%20')
     return raw_url
 
url='http://www.mbi.com.br/mbi/biblioteca/simbolo/brasao-municipios-sao-paulo' ## give the url here
urlcontent=urllib2.urlopen(url).read()
imgurls=re.findall('img .*?src="(.*brasao-mini.jpg)"',urlcontent)
for imgurl in imgurls:
 try:
    print imgurl
    picture_page = 'http://www.mbi.com.br' + imgurl[:-9] + '.jpg'
    opener1 = urllib2.build_opener()
    page1 = opener1.open(picture_page)
    my_picture = page1.read()
    filename = (imgurl[imgurl.rfind("/"):-16][1:] + '.jpg').replace('-', '_')
    print filename  
    fout = open(filename, "wb")
    fout.write(my_picture)
    fout.close()

     
 except:
     pass