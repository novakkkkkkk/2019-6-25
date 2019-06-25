# coding:utf-8
import time

def login(driver):
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[2]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div[1]/input").send_keys('利楚')
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[2]/div/div/div/input").send_keys('admin')
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[3]/div/div/div/input").send_keys('123456')
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/div/button/span").click()
    time.sleep(5)