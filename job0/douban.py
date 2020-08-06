# encoding: utf-8
__author__ = 'jonty yang'
from lxml import html
import requests

# 将目标网站上的页面抓取下来
url = 'https://movie.douban.com/cinema/nowplaying/qingdao/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}
response = requests.get(url=url, headers=headers)
with open('douban.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

# 将抓取下来的数据按照规则进行提取
moives = []
parser = html.etree.HTMLParser(encoding='utf-8')
htmlElement = html.etree.parse('douban.html', parser=parser)
lis = htmlElement.xpath('//div[@id="nowplaying"]//ul[@class="lists"]/li')
for li in lis:
    name = li.xpath('./@data-title')[0]
    score = li.xpath('./@data-score')[0]
    release = li.xpath('./@data-release')[0]
    duration = li.xpath('./@data-duration')[0]
    region = li.xpath('./@data-region')[0]
    director = li.xpath('./@data-director')[0]
    actors = li.xpath('./@data-actors')[0]
    voteCount = li.xpath('./@data-votecount')[0]
    poster = li.xpath('.//img/@src')[0]
    movie = {
        'name': name,
        'score': score,
        'release': release,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'voteCount': voteCount,
        'poster': poster
    }
    moives.append(movie)

for mov in moives:
    print(mov)
