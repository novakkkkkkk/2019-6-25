from selenium import webdriver
from public import login
from public import logout
import time


path ='F:\driver\chromedriver_win32_0625\chromedriver.exe'
url = 'http://120.79.59.41:81/#/login'
driver = webdriver.Chrome(path)
driver.get(url)
driver.maximize_window()
time.sleep(1)

login.login(driver, '利楚', 'admin', '123456')
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/ul/li[2]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu_left"]/ul/li[3]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/button/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[1]/div/div/div/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
#输入门店名称
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[2]/div/div[1]/input').send_keys('zdhmd002')
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[6]/div/div[1]/div[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[6]/div/div[1]/div[1]/div/ul/li[1]').click()
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[6]/div/div[2]/div/input').send_keys('三里屯广场')
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[7]/div/div[1]/input').send_keys('肖磊')
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[1]/form/div[8]/div/div/input').send_keys('15012345678')
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[2]/form/div[1]/div/div[1]/input').send_keys('mendian-zdhmd2')
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[2]/form/div[2]/div/div/input').send_keys('123456')
driver.find_element_by_xpath('//*[@id="companyinfos_box"]/div[3]/div/button/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[3]/div/div[3]/span/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/button/span').click()
time.sleep(1)
logout.logout(driver)

