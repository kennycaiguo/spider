# author:aspiring

from selenium import webdriver

# chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome()

# driver.get("http://neihanshequ.com/")
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=python&rn=&oq=&rsv_pq=87739988000939bf&rsv_t=b194dxdCny6hrJFXQrh4D6bavkKZwfpeT4s7j7V6AvGfiiAvTgxqGAvWbCM&rqlang=cn")

# ret1 = driver.find_element_by_xpath("//ul[@id='detail-list']/li")
# print(ret1)


# for li in ret1:
#     print(li.find_element_by_xpath(".//h1/p").text)
#     print(li.find_element_by_xpath(".//a[@class='image share_url']").get_attribute("href"))

# find_element_by_link_text
print(driver.find_element_by_link_text("下一页>").get_attribute("href"))

# find_elements_by_partial_link_text 文本中包含下一页a的标签
print(driver.find_elements_by_partial_link_text("下一页").get_attribute("href"))


driver.quit()


