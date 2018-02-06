import urllib.request as ur
import os
import random



    
def url_open(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
    req = ur.Request(url,headers=headers)
    #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')

    proxies = ['117.66.132.40:8118','222.185.155.170:8118','27.190.27.218:8118']
    proxy = random.choice(proxies)
    proxy_support = ur.ProxyHandler({'http':proxy})
    opener = ur.build_opener(proxy_support)
    ur.install_opener(opener)

    html = ur.urlopen(req).read()
    #response = ur.urlopen(url)
    #html = response.read()

    
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23 #find返回字符串首位置
    b = html.find(']',a) #起始位置a开始找]

    return html[a:b]
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a+255) # 限制范围
        if b != -1:
            img_addrs.append('html:'+html[a+9:b+4]) # 加入
        else:
            b = a+9

        a = html.find('img src=',b)

    return img_addrs

    
def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1] # 以反斜杠分割，拿出最后一个反斜杠
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            
def download_1(folder='data',page=10):
    os.makedirs(folder,exist_ok=True) # 创建文件夹
    os.chdir(folder) # 进入文件夹

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(page):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments' #图片网址
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_1()
    
