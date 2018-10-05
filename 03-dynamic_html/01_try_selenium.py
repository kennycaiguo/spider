# author: aspiring

import time
from selenium import webdriver

# 实例化一个浏览器

chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path)
# driver = webdriver.PhantomJS()

# 设置窗口大小
# driver.set_window_size(1920, 1080)

# 最大化窗口
driver.maximize_window()

# 发送请求
driver.get("http://www.baidu.com/")

# 进行页面截屏
# driver.save_screenshot("files/baidu.png")
#
# # 元素定位方法
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()
#
# # driver 获取html字符串
# print(driver.page_source)
#
# # driver获取cookie
# cookies = driver.get_cookies()
# print(cookies)
#
# print("*"*100)
#
# cookies = {i["name"]:i["value"] for i in cookies}
# print(cookies)
#

time.sleep(5)

# # 退出浏览器
driver.quit()
