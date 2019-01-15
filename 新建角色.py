from selenium import webdriver
import time
from public import login_zb,logout

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(1)
#登录
login_zb.login(driver)
#点击系统设置菜单
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/ul/li[7]/a").click()
time.sleep(3)
#点击角色维护菜单
driver.find_element_by_xpath("//*[@id='menu_left']/div[1]/ul/li[1]/a").click()
time.sleep(3)
#点击新建平台角色按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/button/span").click()
time.sleep(2)

#选择层级
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[5]/div/div[1]/form/div/div[1]/div/div/div[1]/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()
time.sleep(3)
#填写角色名称
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[5]/div/div[1]/form/div/div[2]/div/div/input").send_keys("总部销售员")
#填写角色说明
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[5]/div/div[1]/form/div/div[3]/div/div/input").send_keys('总部销售产品的人员')
#勾选角色的权限
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/div[2]/div/div[3]/div/label/span/span").click()
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/div[2]/div/div[5]/div/label/span/span").click()
#点击【确定】按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[5]/div/div[4]/button[2]/span").click()
#调用退出方法
logout.logout(driver)
