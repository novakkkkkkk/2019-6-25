from selenium import webdriver
from public import login
from public import logout
import time
from excel import data

driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')
login.open(driver, '利楚', 'admin', '123456')
#点击进入组织管理
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/ul/li[2]/a").click()
#点击商家管理菜单
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_left']/ul/li[2]/a").click()
time.sleep(2)
#点击新建商家按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/button/span").click()
time.sleep(3)
#输入商家名称
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[1]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[0])
#输入商家简称
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[2]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[1])
#填写负责人信息
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[3]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[2])
#填写电话
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[4]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[3])
#填写省份信息
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div[1]/div[1]/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div[1]/div[1]/div/ul/li[17]").click()
#填写商家具体地址
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div[2]/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[4])
#点击下一步按钮
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[3]/div/button/span").click()
time.sleep(2)

#输入商家账号信息
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[3]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[5])
#填写密码
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[4]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[6])
#再次输入密码
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[5]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[7])
#填写姓名
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[6]/div/div/input").send_keys(data.read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls')[8])
#点击保存按钮
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[2]/div/button/span").click()
time.sleep(3)

logout.logout(driver)