#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from public import login
from public import logout
import time
from excel import data


driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')
login.open(driver,'金康高科', 'guest', '789996')
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/ul/li[5]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/div[2]/ul/li/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[3]/div/form[1]/div[4]/div/div/div/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_fwfDCZ.xls')[0])
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[3]/div/form[1]/div[5]/div/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[5]/div[1]/div[3]/table/tbody/tr/td[10]/div/span[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[1]/div/form/div[3]/div/div/div/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_fwfDCZ.xls')[1])
#上传图片
driver.find_element_by_name('fileX').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_fwfDCZ.xls')[2])   #定位上传按钮
time.sleep(1)

driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[1]/div/form/div[6]/div/button[1]/span').click()
time.sleep(5)
logout.logout(driver)


