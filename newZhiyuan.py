from selenium import webdriver
import time
from public import login_zb,logout

driver = webdriver.Chrome("F:\driver\chromedriver_win32_2.46\chromedriver.exe")
time.sleep(5)
driver.get("http://120.79.59.41:81")
driver.maximize_window()
time.sleep(1)

#调用登录方法
login_zb.login(driver)
#点击系统设置菜单
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/ul/li[8]/a").click()
time.sleep(3)
#点击职员维护菜单
driver.find_element_by_xpath("//*[@id='menu_left']/div[1]/ul/li[2]/a").click()
time.sleep(3)
#点击新建职员按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/button[2]/span").click()
time.sleep(2)
#填写登录姓名
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[4]/div/form/div[1]/div[1]/div/div/input").send_keys("测试职员1")
#填写职员工号
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[4]/div/form/div[1]/div[2]/div/div/input").send_keys("123456")
#点击绑定微信
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[4]/div/form/div[1]/div[3]/div/span').click()
#
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/input').send_keys('Ethan')
#
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/div[2]/div[1]/div[2]/button/span').click()
#
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span[1]/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[5]/div/div[3]/span/button/span').click()
time.sleep(1)

#填写登录账号
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[4]/div/form/div[1]/div[4]/div/div[1]/input').send_keys('zy001')
#填写登录密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[4]/div/form/div[1]/div[5]/div/div/input').send_keys('123456')
#再次确认密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[4]/div/form/div[1]/div[6]/div/div[1]/input').send_keys('123456')
#选择角色
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[4]/div/form/div[3]/div/div/div/div[1]/div/div[1]/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[14]').click()
#点击确定
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[4]/div/div[2]/button[2]/span').click()
time.sleep(2)
#调用退出方法
logout.logout(driver)