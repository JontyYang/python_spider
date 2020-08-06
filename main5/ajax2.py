import re
import time

import pymongo
from selenium import webdriver
from lxml import etree
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Spider(object):
    driver_path = 'D:/SS/pycharm/workplace1/chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Spider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="pager_container"]'
                                                        '/span[last()]'))
            )
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
            if 'pager_next pager_next_disabled' in next_btn.get_attribute('class'):
                break
            time.sleep(10)      # 沉睡五秒钟，以待按钮可以点击
            actions = ActionChains(self.driver)
            actions.move_to_element(next_btn)
            actions.click(next_btn)
            actions.perform()
        self.lianjie()

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href')
        for link in links:
             self.request_detail_page(link)
             time.sleep(1)
             # 关闭当前详情页面窗口
             self.driver.close()
             # 切换到总页面
             self.driver.switch_to.window(self.driver.window_handles[0])

    def request_detail_page(self, url):
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        company = html.xpath('//h4[@class="company"]/text()')[0].strip()
        job_request_spans = html.xpath('//dd[@class="job_request"]//span')
        salary = job_request_spans[0].xpath('./text()')[0].strip()
        city = job_request_spans[1].xpath('./text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)
        position = {
            'company': company,
            'salary': salary,
            'city': city
        }
        self.positions.append(position)
        print(position)
        print("++++"*20)


    # 数据库连接
    def lianjie(self):
        client = pymongo.MongoClient('127.0.0.1', port=27017)
        db = client.lagou
        collection = db.positions
        collection.insert_many(self.positions)


if __name__ == '__main__':
    spider = Spider()
    spider.run()