# coding=utf-8
import time

#登录
def login(driver):
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys('金康高科')
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys('guest')
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys('789996')
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()
    time.sleep(5)



