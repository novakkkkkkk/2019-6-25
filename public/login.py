#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
import time


url  = 'http://120.79.59.41:81/#/login'
def open(driver,companyname,username,psw):
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[2]/span").click()
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div[1]/input").send_keys(companyname)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[2]/div/div/div/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[3]/div/div/div/input").send_keys(psw)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/div/button/span").click()
    time.sleep(3)