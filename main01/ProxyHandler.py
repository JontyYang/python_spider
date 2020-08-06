# encoding: utf-8
from http.cookiejar import CookieJar
from urllib import request, parse

# http://httpbin.org 测试http请求的开源项目(查看http请求的一些参数)
# ProxyHandler处理器(代理设置）
# 快代理，代理云

# 未使用代理的外网ip
url = 'http://www.httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read().decode('utf-8'))

# 使用代理的ip
# 1. 使用ProxyHandler ,传入代理构建一个对象
# handler = request.ProxyHandler({'http': '123.139.56.238:9999'})
# # 2. 使用上面创建的handler 创建一个 opener
# opener = request.build_opener(handler)
# # 3. 使用一个opener发送一个请求
# resp = opener.open(url)     #接受一个url，Request对象
# print(resp.read().decode('utf-8'))

# cookie
# cookie是服务器发送给用户浏览器的数据，一般不超过4KB
# Cookie: NAME=VALUE; expires/max-age=DATE; path=PATH; domain=DOMAIN-NAME; SECURE
# name: cookie 的名字
# VALUE: cookie的值
# expires: cookie的过期时间
# Path : cookie作用的路径
# domain: cookie作用的域名
# SECURE: 是否只在https下起作用


# 使用cookielib库和HTTPCookieProcessor模拟登陆

# 第一种自己设定cookie登录
# url = 'http://www.renren.com/880151247/profile'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) '
#                  'Chrome/78.0.3904.17 Safari/537.36',
#     'Cookie': 'anonymid=k2vj383c-t9maqr; depovince=SD; _r01_=1; '
#               'jebe_key=917bd333-5a1b-4386-b07c-4d0e5267f772%7C31708b9141'
#               '88e965940860d1e2d06d47%7C1573543605785%7C1%7C1573543610931; '
#               'jebe_key=917bd333-5a1b-4386-b07c-4d0e5267f772%7C31708b914188e96'
#               '5940860d1e2d06d47%7C1573543605785%7C1%7C1573543610934; wp_fold=0; '
#               'JSESSIONID=abcYdkw7xHmqi84HAIE5w; ick_login=fed9aa7a-6148-4a3b-95d4-'
#               'cb4e9d959df3; t=851b22500f02e81c8b34247312385fac6; societyguester=851'
#               'b22500f02e81c8b34247312385fac6; id=972844206; xnsid=a17640b6; jebecook'
#               'ies=fcd9b87a-a164-4ae9-8fd1-7a9f83a40d6f|||||; ver=7.0; loginfrom=null'
# }
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
# # request.urlretrieve(url, 'renren.html')       # 有反爬虫机制，访问不了
# with open('renrenw.html', 'w', encoding='utf-8') as fp:
# # write函数必须写入一个str的数据类型,但是存储在磁盘中的是字节
#     fp.write(resp.read().decode('utf-8'))


# 第二种，爬虫自己设置
# http.cookiejar模块
# 该模块主要由 CookieJar, FileCookieJar, MozilaCookieJar, LWPCookieJar四个类组成
# CookieJar : 管理Http cookie值，存储Http请求生成的cookie，向传出的http请求添加cookie的
# 对象，整个cookie存储在内存中，对CookieJar实例进行垃圾回收时，实例也将删除
# FileCookieJar（filename，delayload=None，policy=None）: 派生自Cookiejar，其将cookie
# 存储在文件中，delayload为TRUE时支持需要时才访问文件中存储的数据

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.17 Safari/537.36'
}


def get_opener():
    # 1.登录
    # 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 使用cookiejar创建一个HTTPProcessor对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)  # build_opener参数为可变参数
    return opener


def login(opener):
    # 使用opener发送登录的请求（人人网的邮箱和密码）

    data = {
        'email': '13345016132',
        'password': 'pythonspider'
    }

    url = 'http://www.renren.com/PLogin.do'
    req = request.Request(url=url, data=parse.urlencode(data).encode('utf-8'), headers=headers, method='POST')
    opener.open(req)


def visit(opener):
    # 2. 访问个人主页
    dapeng_url = 'http://www.renren.com/880151247/profile'
    # 获取个人页面的时候，不需要重新创建一个opener
    # 而应该是用用之前的那个opener，因为之前的哪个opener
    # 已经包含了需要的cookie信息
    req = request.Request(dapeng_url, headers=headers)
    resp = opener.open(req)
    with open('renren111.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login(opener)
    visit(opener)
