# 动态数据获取
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = 'D:/SS/pycharm/workplace/chromedriver.exe'
# 初始化一个driver，并且指定cheomedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
# time.sleep(5)
# print(driver.page_source)
# driver.close()   # 关闭当前页面
# driver.quit()    # 退出浏览器


# 定位元素,操作输入框
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')
# inputTag.clear()    #
button = driver.find_element_by_id('su')
# button.click()

# 操作select，须使用Select对象，select_by_id...


# 行为链
# inputTag = driver.find_element_by_id('kw')
# submitBtn = driver.find_element_by_id('su')
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag, 'python')
# actions.move_to_element(submitBtn)
# actions.click(submitBtn)
# actions.context_click()
# actions.perform()


# cookies
driver.delete_all_cookies()
for cookie in driver.get_cookies():
    print(cookie)

# 显示等待
# driver.implicitly_wait(10)
# 隐式等待


# 打开多窗口，切换窗口
# driver.execute_script("window.open('https://www.douban.com/')")
# print(driver.current_url)     # 但是当前driver还在百度
# driver.switch_to.window(driver.window_handles[1])  # 切换至豆瓣
# print(driver.current_url)
# 可直接用driver.get()替代之前

# 使用代理ip
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://jfdjal")
# driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
# driver.get('http://httpbin/ip')

