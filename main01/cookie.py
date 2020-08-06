# encoding: utf-8
__author__ = 'jonty yang'

from http.cookiejar import MozillaCookieJar
from urllib import request

cookiejar = MozillaCookieJar('cookie.txt')
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://www.httpbin.org/cookies/set?course=abc')  # 该url可以设置cookies
cookiejar.save(ignore_discard=True)  # ignore_discard 可以忽略过期信息
cookiejar.load()
for cookie in cookiejar:
    print(cookiejar)
