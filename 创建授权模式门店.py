from selenium import webdriver
import time
from public import login_fws,logout
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('F:\driver\chromedriver_win32\chromedriver.exe')
driver.get('http://120.79.59.41/#/login')
driver.maximize_window()
time.sleep(1)

#调用登录模块
login_fws.login(driver)

#点击进入组织管理->门店管理菜单
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='menu_left']/ul/li[3]/a").click()
time.sleep(2)
#点击新建门店按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/button/span").click()
time.sleep(2)
#点击归属商家下拉框
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[1]/div/div/div/input").send_keys("金康开发平台")

time.sleep(3)
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[3]/div/div[1]/input').send_keys("年付费门店001")

