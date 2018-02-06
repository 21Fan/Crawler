import urllib.request as ur#一个模块
response = ur.urlopen("https://www.dy2018.com/index.html")
html = response.read()
html = html.decode("gb2312")#编码形式
addrs = []
a = html.find('href=')
while a != -1:
    
    #html = html[a:a+5]
    
    addrs.append(html[a+9:a+14])
    url = 'https://www.dy2018.com/i/97747.html'
    a = html.find('href=',a+20)
for each in addrs:
    

    print(each)
