import requests
from lxml import etree


HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Cookies': 'user_trace_token=20191111163828-f0ec2e02-7170-4cf2-a2ac-850c3b6f0b00; _ga=GA1.2.648722606.1573461509; LGUID=20191111163828-a259e921-045e-11ea-a62d-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e599dcb0b382-0c00264e8f4447-771123e-921600-16e599dcb0c88d%22%2C%22%24device_id%22%3A%2216e599dcb0b382-0c00264e8f4447-771123e-921600-16e599dcb0c88d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.1621461277.1574942963; JSESSIONID=ABAAABAAAGFABEF7BA6DC5CEAA83EA6C51B027A7FBC468A; WEBTJ-ID=20191128215110-16eb247a688d7-07d0bf8ceb3153-7711a3e-921600-16eb247a689467; LGSID=20191128215109-21f5c15f-11e6-11ea-a9f4-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1573986731,1574942963,1574945863,1574949071; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=c6ad9a975ce15e3b324159475128f0134da30c7a25; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574951425; LGRID=20191128223023-9d0981e1-11eb-11ea-a68a-5254005c3644; SEARCH_ID=75e0ba67715c4adf8c9e36456d850390',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Sec-Fetch-Site': 'same-origin'
}
def request_list():

    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first': 'false',
        'pn': '1',
        'kd': 'python'
    }
    for x in range(1, 13):
        data['pn'] = x
        response = requests.post(url, headers=HEADERS, data=data)
        result = response.json()    #  返回的是一个字典
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            url = 'https://www.lagou.com/jobs/%s.html' % positionId
            parse_url(url)
            break
        break

def parse_url(url):
    response = requests.get(url, headers= HEADERS)
    text = response.content.decode('utf-8')
    htmlElement = etree.HTML(text)



def main():
    request_list()

if __name__ == '__main__':
    main()