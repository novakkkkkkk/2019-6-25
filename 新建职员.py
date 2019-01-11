from selenium import webdriver
import time

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(5)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(1)
#登录
#输入公司名称
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys("金康高科")
#输入账号信息
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys("guest")
#输入密码
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys("789996")
#点击登录按钮
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()
time.sleep(5)
#点击系统设置菜单
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/ul/li[7]/a").click()
time.sleep(3)
#点击职员维护菜单
driver.find_element_by_xpath("//*[@id='menu_left']/div[1]/ul/li[2]/a").click()
time.sleep(2)
#点击新建职员按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[1]/div[1]/button[2]/span").click()
time.sleep(2)
#填写登录账号
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[3]/div/form/div[1]/div[1]/div/div/input").send_keys("zy-cdh001")
#填写职员姓名
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div[1]/div[3]/div/form/div[1]/div[2]/div/div/input").send_keys("测试职员")
#填写工号
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[3]/div/form/div[1]/div[3]/div/div/input').send_keys('123456')
#填写密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[3]/div/form/div[1]/div[4]/div/div/input').send_keys('123456')
#确认密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[3]/div/form/div[1]/div[5]/div/div/input').send_keys('123456')
#选择角色
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[3]/div/form/div[3]/div[1]/div/div/div[1]/input').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[16]/span').click()
time.sleep(1)
#点击【确定】按钮
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[3]/div/div[2]/button[2]/span').click()