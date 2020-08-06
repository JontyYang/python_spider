from queue import Queue
import requests
from lxml import etree
from urllib import request
import os
import re

import threading


'''
Queue(maxsize) 初始化队列
qsize() 返回队列大小
empty() 判断是否为空
full() 判断时候满了
get() 获取第一个数据
put() 将一个数据放入队列中
'''



def parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Referer': 'http://www.doutula.com/article/list/?page=1'
    }
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    for img in imgs:
        img_url = img.get('data-original')  # 使用get方法获取属性值
        img_name = img.get('alt')
        img_name = re.sub(r'[\?？\.。！!]', '', img_name)   # 将非法字符串替换
        suffix = os.path.splitext(img_url)[1]   # 取图片后缀名
        filename = img_name + suffix
        print(img_url)
        request.urlretrieve(img_url, 'D:/SS/pycharm/workplace1/images2/' + filename)

def main():
    for x in (1, 200):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        parse(url)


if __name__ == '__main__':
    main()