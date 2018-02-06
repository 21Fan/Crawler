import re
import urllib.request as ur #一个模块
import random
import time

iplist = ['219.157.114.65']
proxy_support = ur.ProxyHandler({'http':'121.232.147.239'})
#创建一个opener
opener = ur.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]
#安装opener
ur.install_opener(opener)


response = ur.urlopen("https://www.dy2018.com/index.html")
html = response.read()
html = html.decode("gb2312")#编码形式

url = []
movie_num = re.findall(r'/i/\d\d\d\d\d',html)
magnet = []

for each in movie_num:
    url.append('https://www.dy2018.com'+each+'.html')


for each in url:
   
    print(each)
    

    response = ur.urlopen(each)
    each = response.read().decode('gb2312','ignore')
    
    
    a = each.find('magnet:?xt=urn:btih:')
    if a != -1:
        b = each.find('&tr',a)
        print(each[a:b])






