#coding:utf-8
import urllib,urllib2
import json

content = raw_input("请输入需要翻译的内容：")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.urlencode(data)#.encode('utf-8')

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'

'''
代理使用方法：
proxy_support = urllib2.ProxyHandler({'http':'111.1.32.28:81'})
opener = urllib2.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
opener.open("http://www.baidu.com")

'''
#一次将数据信息和头部信息都加入，需要提前写好头部字典
req = urllib2.Request(url,data,head)
html = urllib2.urlopen(req).read()
'''
加入头部信息的两种方法:
import urllib2
req = urllib2.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')
r = urllib2.urlopen(req)
OpenerDirector automatically adds a User-Agent header to every Request. To change this:

import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
opener.open('http://www.example.com/')
'''

result = json.loads(html)
print result['translateResult'][0][0]['tgt']
