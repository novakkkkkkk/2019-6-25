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
logout.logout(driver)

