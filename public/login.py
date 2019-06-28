# coding=utf-8
import time

#登录
def login(driver,companyname,username,psw):
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[2]/span").click()
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div[1]/input").send_keys(companyname)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[2]/div/div/div/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/form/div[3]/div/div/div/input").send_keys(psw)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[3]/div/button/span").click()
    time.sleep(3)