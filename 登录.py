from selenium import webdriver
import time


driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(5)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(3)
#输入公司名称
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys("金康高科")
#输入账号信息
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys("guest")
#输入密码
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys("789996")
#点击登录按钮
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()

time.sleep(3)
driver.close()
