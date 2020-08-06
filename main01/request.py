# encoding: utf-8

# 使用request.Request设置请求头

from urllib import request, parse

url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# response = request.urlopen(url)
# print(response.read())    #反爬虫机制，读取不了
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.17 Safari/537.36',
           'Referer': 'https://www.lagou.com/'
           }
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')  # Request为一个类
response = request.urlopen(req)
print(response.read().decode('utf-8'))
