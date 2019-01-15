# coding=utf-8
import time
from selenium.webdriver.common.action_chains import ActionChains

def logout(driver):
    a = driver.find_element_by_class_name("user-name")
    #将鼠标移动到用户名的按钮上悬浮
    ActionChains(driver).move_to_element(a).perform()
    time.sleep(2)
    #点击退出按钮
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div[2]/ul/li/a[2]").click()
    time.sleep(2)
    driver.quit()
