from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(5)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(3)
#登录http://jkserver:81/zentao/bug-view-1152.html
#输入公司名称
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys("金康高科")
#输入账号信息
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys("guest")
#输入密码信息
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys("789996")
#点击登录按钮
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()
time.sleep(3)

#退出登录
e=driver.find_element_by_class_name("user-name")
#将鼠标移动到用户名的按钮上悬浮
ActionChains(driver).move_to_element(e).perform()
time.sleep(3)
#找到退出按钮并点击
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div[2]/ul/li/a[2]").click()

time.sleep(3)
driver.quit()