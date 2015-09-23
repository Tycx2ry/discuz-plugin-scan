# -*- coding:utf-8 -*-
import urllib2

def checkplugin(i):
    url = host+'/plugin.php?id='+str(i)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf8')
        if content.find(u"\u63d2\u4ef6\u4e0d\u5b58\u5728\u6216\u5df2\u5173\u95ed") != -1:
            #pass
            print i+'__notfind'
        else:
            print i+'____find'
            list.append(i)
    except urllib2.URLError, e:
        open('error.txt','a').write(str(i)+'\n')
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason



if __name__ == '__main__':
    host = 'http://bbs.tuniu.com' #
    list = []
    for i in open('dzpluginlist_t.txt').readlines():
        #print i.strip()
        checkplugin(i.strip())
    for l in list:
        print '[-] '+host+'/plugin.php?id='+l
