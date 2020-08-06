# encoding: utf-8
from http.cookiejar import MozillaCookieJar
from urllib import request, parse

__author__ = 'jonty_yang'

# cookiejar = MozillaCookieJar('cookie.txt')  # cookie信息将存储在本地文件中
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/78.0.3904.17 Safari/537.36'
#
# }
#
#
# # 使用代理
# def build_proxyhandler():
#     handler = request.ProxyHandler({'HTTP': '113.120.34.145:9999'})
#     return handler
#
#
# # 使用cookie
# def build_cookiehandler():
#     handler = request.HTTPCookieProcessor(cookiejar)
#     return handler
#
#
# # 获取opener
# def get_opener():
#     proxyhandler = build_proxyhandler()
#     cookiehandler = build_cookiehandler()
#     opener = request.build_opener(proxyhandler, cookiehandler)
#     return opener
#
#
# # 登录人人网，时opener获取cookie信息
# def login(opener):
#     data = {
#         'email': '13345016132',
#         'password': 'pythonspider'
#     }
#     login_url = 'http://www.renren.com/PLogin.do'
#     req = request.Request(url=login_url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
#     opener.open(req)  # 此时opener已经改变，包含cookie的信息
#
#
# # 无登录访问
# def visit(opener):
#     dapeng_url = 'http://www.renren.com/880151247/profile'
#     req = request.Request(url=dapeng_url, headers=headers)
#     resp = opener.open(req)
#     with open('dapeng.html', 'w', encoding='utf-8') as fp:
#         fp.write(resp.read().decode('utf-8'))
#
#
# # 打印cookie信息
# def print_cookie():
#     cookiejar.save(ignore_discard=True)
#     cookiejar.load(ignore_discard=True)
#     for cookie in cookiejar:
#         print(cookie)
#
#
# if __name__ == '__main__':
#     opener = get_opener()
#     login(opener)
#     visit(opener)
#     print_cookie()

