#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from public import login
from public import logout
from selenium import webdriver
import time

driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')
login.open(driver,'金康高科','guest','789997')
#time.sleep(1)
#print(driver.find_element_by_css_selector('div.el-message.el-message--error.is-closable').text)
print(driver.find_element_by_xpath('/html/body/div[2]/p').text)