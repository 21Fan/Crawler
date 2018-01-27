import urllib.request
import urllib.parse
import json

while True:

    content = input("请输入需要翻译的内容:")
    data ={}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1516978611507'
    data['sign'] = 'a0d98ee87b37c691ba0493781efe11bb'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

        



    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    target = json.loads(html)

    print("翻译结果:%s"%(target['translateResult'][0][0]['tgt']))
