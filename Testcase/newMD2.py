#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from public import login
from public import logout
from selenium.webdriver.common.keys import Keys
import time
from excel import data


driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')

login.open(driver, '利楚', 'admin', '123456')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/ul/li[2]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu_left"]/ul/li[3]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/button/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[1]/div/div/div/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
#输入门店名称
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[2]/div/div[1]/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls')[0])
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[5]/div/div/label[2]/span[1]/span').click()
a = driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[6]/div/div[1]/input')
a.send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls')[1])
a.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[7]/div/div[1]/div[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[7]/div/div[1]/div[1]/div/ul/li[1]').click()
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[7]/div/div[2]/div/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls')[2])
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[8]/div/div/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls')[3])
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[9]/div/div/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls')[4])
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[2]/form/div[1]/div/div/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls')[5])
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[2]/form/div[2]/div/div/input').send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls')[6])
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[3]/div/button/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[3]/div/div[3]/span/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/button/span').click()
time.sleep(1)
logout.logout(driver)