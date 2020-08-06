#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Jonty yang"

'''
2019.11.11
通用爬虫，聚焦爬虫
准备工具：python3.6 | pycharm professional | virtualenv/virtualenvwrapper(虚拟环境)
http(80端口），https(是http的加密版本，在其下方加入了ssl层，端口443）

URL：
scheme://host:port/path?query-string&query-string#anchor
scheme:代表的是访问协议，一般为http/https/ftp
host:主机名，域名,比如www.baidu.com
port:端口号
path:请求的网站的某个页面
query-string:查询字符串,使用&连接，
anchor:锚点，即页面的定位符
在浏览器中请求一个url,浏览器会将除ASCii的进行%（十六进制数）的方式编码

http常见请求方法：
get:只从服务器获取资源，并不对服务器资源产生影响
post:会对服务器产生请求（如登录，改密码等）

在http协议中，向服务器发送一个请求，数据分为三部分(第一个放在URL中，第二个放在body中（post请求），第三放在headers中)
http请求头常见参数：
User-Agent:浏览器名称,若是爬虫则默认为python
Referer:表明当前这个请求是从哪个Url过来的
Cookie:http协议是无状态的，即同一个人发送了两次请求，服务器并不知道是同一个人发送的。
       此时使用cookie来标识，一般做登录的网站要使用到Cookie

常见响应状态码：
200: 请求正常，服务器正常返回数据
301: 永久重定向,比如访问www.jingdong.com时会访问到www.jd.com
302: 临时重定向，比如访问一个需要登录的页面时，没有登陆，此时会重定向到登录页面
400: 请求的url在服务器上找不到
403: 服务器拒绝访问，权限不够
500: 服务器内部错误，可能是服务器出现bug
405: 表示请求的方式不对

'''

from urllib import parse
from urllib import request  # 所有与网络请求相关的方法,都被集中在request模块下

# urlopen()函数
# 返回值是http.client.HTTPResponse对象，这个对象是一个类文件句柄对象(鸭子对象)
# 有read(size),readline(),readlines()以及getcode()等方法
# resp = request.urlopen('http://www.tv432.com')
# print(resp.read())
# print(resp.read(10))
# print(resp.readline())
# print(resp.readlines())    #读取多行，以列表元素展示，每一行为列表元素
# print(resp.getcode())      #获取状态码
# urlretrieve()函数
# 该函数可以将网页上的文件保存到本地
# request.urlretrieve('http://www.tv432.com', 'baidu.html')

# 参数编码与解码
# urlencode()函数    #将非ascii码进行16进制编码(对字典，或两元素的元组序列）
params = {'name': '张三', 'age': 19, 'greet': 'Hello world'}
result = parse.urlencode(params)
print(result)
params = {'wd': '刘德华'}
resul = parse.urlencode(params)
print(resul)
url = 'http://www.baidu.com/s?resul'
resp = request.urlopen(url)

# parse_qs()函数
# params = {'name': '张三', 'age': 19, 'greet': 'Hello world'}
# result = parse.urlencode(params)
print(parse.parse_qs(result))  # 还原

# urlparse和urlsplit：
# 基本一样，唯一不一样的是split返回之中无params参数
# 有时想到将url的各个组分进行拆分，如scheme，name...
url = 'http://www.baidu.com/s;jonty?wd=python&usernam=abc#a'
result = parse.urlparse(url)
print(result)
# print('scheme: ', result.scheme)
# print('netloc: ', result.netloc)
# result = parse.urlsplit(url)
# print(result)    #没有params参数
