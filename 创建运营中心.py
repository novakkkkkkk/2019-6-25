from selenium import webdriver
import time

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(3)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(1)

#登录
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys("金康高科")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys("guest")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys("789996")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()
time.sleep(5)
#点击组织管理->运营中心管理
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/ul/li[2]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_left']/ul/li[1]/a").click()
time.sleep(5)
#点击新建运营中心按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[23]/a").click()
time.sleep(1)
#输入运营中心的名称
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/form/div[1]/div/div/input").send_keys("金康高科亚洲区")
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div/div/input").send_keys("金康高科亚洲有限公司")
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/button[1]/span").click()
time.sleep(5)
#输入密码和确认密码
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[5]/div/div/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[6]/div/div/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div/input").send_keys("杨雷")
#点击保存按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/button/span").click()

