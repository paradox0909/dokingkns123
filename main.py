#This code is concert macro program (lan py)
#from selenium import driver
import selenium
from argparse import Action
from this import d
from outcome import acapture
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


#-------------------------------------------------------------------------------------------------------------------------
#함수가 ---t로 끝나면 단수, s로 끝나면 복수. (복수는 여러개를 다 찾는것,그 페이지에 보여지는 것을 다 찾는것) 단수는 하나만

driver = webdriver.Chrome("/Users/doking/Downloads/chromedriver")
url = 'https://ticket.melon.com'
driver.get(url)
driver.maximize_window()
Action = Actionchains(driver)

driver.find_element_by_css_selector('#sub_area > a').click()
driver.find_element_by_css_selector('#btn_gate kakaon').click()
driver.find_element_by_css_selector('#id_email_2_label').click()
action.send.keys('dokingkns0909@naver.com').perform()











