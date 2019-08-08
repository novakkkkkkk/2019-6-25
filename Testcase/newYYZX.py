from selenium import webdriver
from public import login
from public import logout
import time

driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')
login.open(driver, '金康高科', 'guest', '789996')
#点击组织管理
time.sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/ul/li[2]/a").click()
#点击运营中心管理
time.sleep(1)
driver.find_element_by_xpath("//*[@id='menu_left']/ul/li[1]/a").click()
time.sleep(3)
#点击新建运营中心按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/a/span[2]").click()
time.sleep(1)
#输入运营中心的名称
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/form/div[1]/div/div/input").send_keys("测试6区")
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div/div/input").send_keys("金康高科测试6区")
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/button[1]/span").click()
time.sleep(3)
#输入密码和确认密码
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[5]/div/div/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[6]/div/div/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div/input").send_keys("杨雷")
#点击保存按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/button/span").click()
time.sleep(2)

logout.logout(driver)