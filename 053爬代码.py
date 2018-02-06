import urllib.request#一个模块

url = "https://www.dy2018.com/i/31210.html"

Headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
req = urllib.request.Request(url,headers=Headers)

response = urllib.request.urlopen(req)
html = response.read()
html = html.decode("gb2312")#编码形式
print(html)
