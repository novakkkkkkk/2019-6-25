#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://www.youdao.com")

#向cookie的name
cookie = driver.get_cookies()
#将获得cookie信息打印
print(cookie)
driver.quit()