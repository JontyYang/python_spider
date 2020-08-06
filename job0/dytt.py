import requests
from lxml import html
import pymongo
__author__ = 'jonty yang'

DOMAIN_NAME = 'https://www.dytt8.net/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Referer': 'https://www.dytt8.net/html/gndy/dyzz/index.html',
    'Cookies': '37cs_user=37cs83056503782; UM_distinctid=16e863dc50f241-0820a3b5c45186-7711a3e-e1000-16e863dc5105bd; bz_finger=93fdf8ceb389101cdd2e4ea3be06e006; '
               '37cs_pidx=2; 37cs_show=253%2C75; XLA_CI=d09e044d52a4413f8dcfaac9c382766f; fikker-9Ruf-S6cn=UtJVcZePA6Uf12eTqF7pSDotUlWtIVQD; '
               'fikker-9Ruf-S6cn=UtJVcZePA6Uf12eTqF7pSDotUlWtIVQD; CNZZDATA1278139455=630272779-1574209539-https%253A%252F%252Fwww.dytt8.net%252F%7C1574420164; '
               'CNZZDATA1260535040=1186970384-1574206509-https%253A%252F%252Fwww.dytt8.net%252F%7C1574417150; cscpvrich5041_fidx=2'
}
PARSER = html.etree.HTMLParser(encoding='gb2312')




# 返回每一个页面的电影url列表
def fullurls(url):
    response = requests.get(url=url, headers=HEADERS)
    print(response.status_code)
    text = response.content.decode('utf-8', errors='ignore')
    htmlElement = html.etree.HTML(text)
    urls = htmlElement.xpath('//div[@class="co_content8"]/ul//a/@href')
    fullurls = map(lambda url:DOMAIN_NAME + url, urls)
    return fullurls

# 字符串优化
def parse_infos(info, keys):
    return info.replace(keys, '').strip()

# 返回电影相关信息字典
def movie_detail(detail_urls):
    movie = {}
    resp = requests.get(detail_urls, headers=HEADERS)
    text = resp.content.decode(encoding='gb2312', errors='ignore')
    htmlElement = html.etree.HTML(text)
    titles = htmlElement.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    movie['title'] = titles
    Zooms = htmlElement.xpath('//div[@id="Zoom"]')[0]
    hrefs = Zooms.xpath('.//img/@src')
    cover = hrefs[0]
    screenshot = hrefs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot
    # 提取段落信息
    infos = Zooms.xpath('.//text()')
    # print(infos)
    for index, info in enumerate(infos):
        if info.startswith('◎年　　代'):
            info = parse_infos(info, '◎年　　代')
            print(info)
            movie['info'] = info
        elif info.startswith('◎产　　地'):
            info = parse_infos(info, '◎产　　地')
            print(info)
            movie['country'] = info
        elif info.startswith('◎类　　别'):
            info = parse_infos(info, '◎类　　别')
            print(info)
            movie['type'] = info
        elif info.startswith('◎语　　言'):
            info = parse_infos(info, '◎语　　言')
            print(info)
            movie['language'] = info
        elif info.startswith('◎豆瓣评分'):
            info = parse_infos(info, '◎豆瓣评分')
            print(info)
            movie['score'] = info
        elif info.startswith('◎片　　长'):
            info = parse_infos(info, '◎片　　长')
            print(info)
            movie['duration'] = info
        elif info.startswith('◎导　　演'):
            info = parse_infos(info, '◎导　　演')
            print(info)
            movie['director'] = info
        elif info.startswith('◎主　　演'):
            info = parse_infos(info, '◎主　　演')
            actors = [info]
            for x in range(index+1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            print(actors)
            movie['actors'] = actors
        elif info.startswith('◎简　　介'):
            profile = infos[index + 1].strip()
            print(profile)
            movie['profile'] = profile
    return movie

# 通过迭代页面来爬取电影信息
i = 0
def spider():
    movies = []
    basic_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    # 迭代电影页数
    for x in range(3, 5):
        basic_url = basic_url.format(x)
        detail_urls = fullurls(basic_url)
        # 迭代每一页中的电影url
        for detail_url in detail_urls:
            movie = movie_detail(detail_url)
            movies.append(movie)
    # client = pymongo.MongoClient('127.0.0.1', port=27017)
    # db = client.dytt
    # collection = db.dy
    # collection.insert_many(movies)
    print(movies)

if __name__ == '__main__':
    spider()

