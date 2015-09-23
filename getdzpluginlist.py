# -*- coding:utf-8 -*-
import urllib2
import re


def getsigledate(i):
    url = 'http://addon.discuz.com/index.php?view=plugins&f_order=create&page=' + str(i)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read()
        pattern = re.compile('<a href="http:\/\/addon.discuz.com/\?@([0-9a-zA-Z_]*)\.plugin" class="avt">',re.S)
        items = re.findall(pattern,content)
        for item in items:
                print item
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

if __name__ == '__main__':
    for i in range(1,140):
        getsigledate(i)
        
