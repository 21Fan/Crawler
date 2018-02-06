import urllib.request as ur
import random

url = 'https://www.dy2018.com/i/31210.html'

iplist = ['219.157.114.65']
proxy_support = ur.ProxyHandler({'http':random.choice(iplist)})
#创建一个opener
opener = ur.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]
#安装opener
ur.install_opener(opener)
response = ur.urlopen(url)
html = response.read().decode('gb2312')
print(html)
