import urllib.request as ur
import os

def url_open(url):
    req = ur.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    response = ur.urlopen(url)
    html = response.read()
    return html
def get_page(url):
    url

    a = html.find('current-comment-page') + 23 #find返回字符串首位置
    b = html.find(']',a) #起始位置a开始找]

    return html[a:b]
def find_imgs(url):

    
def save_imgs(folde,img_addrs):
    
def download_1(folder='data',page=1):
    os.mkdir(folder) # 创建文件夹
    os.chdir(folder) # 进入文件夹

    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments' #图片网址
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_1()
    
