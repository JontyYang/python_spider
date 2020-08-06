# -*- coding: utf-8 -*-
__author__ = 'jonty yang'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class QiangPiaoSpider(object):
    def __init__(self):
        self.__login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.__my_url = "https://kyfw.12306.cn/otn/view/index.html"
        self.__search_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.__driver_path = 'D:/SS/pycharm/workplace/chromedriver.exe'
        self.__driver = webdriver.Chrome(executable_path=self.__driver_path)
        self.__tickets = []

    # def wait_input(self):
    #     self.from_station = input("起始站: ")
    #     self.to_station = input("目的地： ")
    #     self.depart_time = input("出发时间：")

    def __login(self):
        self.__driver.get(self.__login_url)
        WebDriverWait(self.__driver, 1000).until(
            EC.url_to_be(self.__my_url)
        )
        print("登陆成功！！！")

    def __order_ticket(self):
        # 1. 跳转到查询界面
        self.__driver.get(self.__search_url)

        # # 2. 等待出发地是否输入正确
        # WebDriverWait(self.__driver, 1000).until(
        #     EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), self.from_station)
        # )
        #
        # WebDriverWait(self.__driver, 1000).until(
        #     EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        # )
        #
        # WebDriverWait(self.__driver, 1000).until(
        #     EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        # )

        # 等待查询按钮是否可以点击
        # 定位元素,操作输入框
        # inputTag = self.__driver.find_element_by_id('fromStationText')
        # inputTag.send_keys('青岛')
        # inputTag = self.__driver.find_element_by_id('toStationText')
        # inputTag.send_keys('兰州')
        # inputTag = self.__driver.find_element_by_id('train_date')
        # inputTag.send_keys('2020-04-20')

        # WebDriverWait(self.__driver, 1000).until(
        #     EC.element_to_be_clickable((By.ID, "query_ticket"))
        # )


        # 点击查询按钮
        searchBtn= self.__driver.find_element_by_id("query_ticket")
        searchBtn.click()

        # 在点击查询按钮以后，等待车次信息是否显示出来
        WebDriverWait(self.__driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, "//tbody[@id='queryLeftTable']/tr"))
        )

        tr_list = self.__driver.find_elements_by_xpath("//tbody[@id='queryLeftTable']/tr[not(@datatran)]")

        for list in tr_list:
            train_number = list.find_element_by_class_name("number").text
            left_tickets = list.find_element_by_xpath(".//td[4]").text
            time_length = list.find_element_by_xpath(".//div[@class='ls']/strong").text
            ticket = {
                'train_number': train_number,
                'left_tickets': left_tickets,
                'time_length': time_length
            }
            self.__tickets.append(ticket)
            print(ticket)

    def run(self):
        # self.wait_input()
        self.__login()
        self.__order_ticket()


if __name__ == '__main__':
    spider = QiangPiaoSpider()
    spider.run()
