from selenium import webdriver
import time

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(3)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(1)
#输入公司名称
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys("利楚")
#输入账号信息
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys("admin")
#输入密码
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys("123456")
#点击登录按钮
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()

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
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[1]/div/div/div/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[34]/span").click()
time.sleep(2)
#输入门店名称
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[3]/div/div[1]/input").send_keys("自动化测试门店002")
#选择门店类型
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[4]/div/div/div/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[1]/span").click()
time.sleep(1)


#选择门店省份
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[1]/div[1]/span").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[1]/div[1]/div/ul/li[1]").click()
time.sleep(2)
#填写门店地址
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[2]/div/input").send_keys("世界城广场1号")
#填写门店负责人
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[7]/div/div[1]/input").send_keys("肖磊")
#填写联系电话
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[8]/div/div/input").send_keys("87311111")

#填写账号
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[2]/form/div[1]/div/div[1]/input").send_keys("md-zdh002")
#填写密码
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[2]/form/div[2]/div/div/input").send_keys("123456")
#点击完成创建按钮
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[3]/div/button/span").click()
time.sleep(2)
#点击确认按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[3]/span/button[2]/span").click()
time.sleep(2)
#点击取消按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/button/span").click()







