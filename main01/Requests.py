#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

# requests 库

# 发送get请求
response = requests.get('http://www.baidu.com')
# print(type(response.text))
# print(response.text)     # text返回类型为str，但会出现乱码
# print(type(response.content))   # 返回类型为bytes
# print(response.content.decode('utf-8'))

print(response.url)  # 返回完整url
print(response.encoding)  # 返回编码
print(response.status_code)  # 返回状态码

# 如果想添加headers，可以传入headers传入请求头中，如果要将参数放在url中
# 可以利用params参数
headers = {
    'USer-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/78.0.3904.17 Safari/537.36'
}

# get 请求使用 params参数传递数据
# # 默认？之后的内容
# params = {
#     'wd': '中国'
# }
#
# response = requests.get('http://www.baidu.com/s', params=params, headers=headers)
# print(response.content.decode('utf-8'))
# print(response.url)
#
# with open('baidu.html', 'w', encoding='utf-8') as fp:
#     fp.write(response.content.decode('utf-8'))


# 发送post请求
# data = {
#     'id': '1624635413',
#     'name': 'Jonty',
#     'wd':'中国'
# }
#
# response = requests.post('http://www.baidu.com/s', data=data, headers=headers)
# 如果返回的事json数据，可以使用response.json()
# 来将返回内容转换为字典或者列表
# print(response.content.decode('utf-8'))


# # 使用代理
# response = requests.get('http://httpbin.org/ip')
# print(response.text)
# url = 'http://httpbin.org/get'
# proxy = {
#     'http': '123.139.56.238:9999'
# }

# response = requests.get('http://httpbin.org/ip', headers= headers, proxies= proxy)
# print(response.text)

# cookie 处理
# url = 'http://www.renren.com/PLogin.do'
# data = {
#     'email': '13345016132',
#     'password': 'pythonspider'
# }
# # 一个会话对象，相当于urllib中的opener
# # 之前的opener对象可以发送多个请求，多个请求可以共享opener的cookie，
# # 因此session对象也遵循这一点，支持多个请求共享cookie
# session = requests.Session()
# res = session.post(url, data=data, headers=headers)    # 返回一个response对象
# for cookie in session.cookies:    # 打印cookie值
#     print(cookie)
#
# response = session.get('http://www.renren.com/880151247/profile', headers=headers)
# print(response.content)
# with open('session.html', 'w', encoding='utf-8') as fp:
#     fp.write(response.content.decode('utf-8'))


# 处理不信任的ssl证书（一般针对于https）
# 当请求为https时，默认会对网站进行ssl证书的检验，
# 但也可以用verify参数修改
# resp = requests.get('https://www.12306.cn/index/')
# print(resp.content.decode('utf-8'))


