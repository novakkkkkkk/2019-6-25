from selenium import webdriver
from public import login
from public import logout
import time

driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')
login.open(driver, '金康高科华中区', 'admin', '123456')

#点击组织管理
time.sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/ul/li[2]/a").click()
time.sleep(3)
#点击服务商管理菜单
driver.find_element_by_xpath("//*[@id='menu_left']/ul/li[1]/a").click()
time.sleep(2)
#点击新建服务商按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[1]/button/span").click()
time.sleep(3)
#输入服务商的基本信息
#输入服务商全称
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[1]/div/div/input").send_keys("服务商zdh8")
#输入服务商简称
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[2]/div/div[1]/input").send_keys("服务商简称zdh8")
#输入所属收银系统
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[3]/div/div/input").send_keys("美瑞华")
#填写负责人
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[4]/div/div/input").send_keys("肖磊")
#填写手机号
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div/input").send_keys("15012345678")
#找到省份输入框的位置
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[1]/div[1]/span").click()
time.sleep(3)
#输入省份、城市、区域信息
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[1]/div[1]/div/ul/li[1]").click()
#填写具体地址
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[2]/div/input").send_keys("天安门广场")
#选择OEM信息并点击
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[2]/form/div/div/div/label[2]/span[1]/span").click()
#点击下一步按钮，进入填写开票信息页面
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[3]/div/button/span").click()
#等待页面加载3秒
time.sleep(3)
#在开票信息页面，点击下一步按钮，进入填写账号页面
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[3]/div/button/span").click()
time.sleep(3)
#填写服务商的账号信息
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[4]/div/div[1]/input").send_keys("ceshi103")
#填写密码
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[5]/div/div/input").send_keys("123456")
#确认密码
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[6]/div/div/input").send_keys("123456")
#填写负责人姓名
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[7]/div/div/input").send_keys("张三")
#点击保存按钮
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[2]/div/button/span").click()
time.sleep(3)

logout.logout(driver)