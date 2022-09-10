# 라이브러리 불러오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# target url
url = 'https://google.com'
# 드라이버 연결
driver = webdriver.Chrome()
# 웹사이트 이동
driver.get(url)
time.sleep(1)

# 검색창
search_box = driver.find_element_by_id('query')

actions = webdriver.ActionChains(driver).send_keys_to_element(search_box, '아이스크림').send_keys(Keys.ENTER)
actions.perform()
