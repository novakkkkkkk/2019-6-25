from selenium import webdriver
import time

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(3)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(3)
#输入公司名称
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys("利楚")
#输入账号信息
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys("admin")
#输入密码
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys("123456")
#点击登录按钮
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()

#点击进入组织管理->商家管理
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='menu_left']/ul/li[1]/a").click()
time.sleep(2)
#点击新建商家按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/button/span").click()
time.sleep(1)
#输入商家名称
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[1]/div/div/input").send_keys("自动化测试商家001")
#输入商家简称
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[2]/div/div/input").send_keys("自动化商家001")
#填写负责人信息
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[3]/div/div/input").send_keys("肖磊")
#填写电话
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[4]/div/div/input").send_keys("15012345678")
#填写省份信息
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div[1]/div[1]/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div[1]/div[1]/div/ul/li[8]").click()
#填写商家具体地址
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div[2]/div/input").send_keys("江汉路1号")
#点击下一步按钮
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[3]/div/button/span").click()
time.sleep(2)

#输入商家账号信息
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[3]/div/div/input").send_keys("sj-zdh001")
#填写密码
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[4]/div/div/input").send_keys("123456")
#再次输入密码
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[5]/div/div/input").send_keys("123456")
#填写姓名
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[6]/div/div/input").send_keys("肖磊")
#点击保存按钮
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[2]/div/button/span").click()

