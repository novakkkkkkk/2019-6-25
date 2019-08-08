#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

path = 'F:\driver\chromedriver_win32_0625\chromedriver.exe'
url = 'https://www.baidu.com/'
driver = webdriver.Chrome(path)
driver.get(url)
driver.maximize_window()
time.sleep(1)

#把鼠标悬停在设置按钮上
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="u1"]/a[8]')).perform()
time.sleep(2)
#然后点击搜索设置
driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
time.sleep(2)
#选择下拉框中的第二个选项
Select(driver.find_element_by_name('NR')).select_by_index(1)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
time.sleep(1)
driver.quit()


