from selenium import webdriver
import os
path = os.path.join(os.path.dirname(__file__),'chromedriver')
driver = webdriver.Chrome(executable_path=path)
driver.get('http://baidu.com')