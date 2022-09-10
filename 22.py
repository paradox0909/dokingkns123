import selenium 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#크롬드라이버 자동업데이트
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://ticket.melon.com/performance/index.htm?prodId=207126")  
login_btn = driver.find_element(By.CSS_SELECTOR,"#login_area > a")
login_btn.click()

login_btn1 = driver.find_element(By.CSS_SELECTOR,"#conts_section > div > div > div:nth-child(1) > button")

id = driver.find_element(By.CSS_SELECTOR, "#id_email_2_label")
id.click()
id.send_keys("dokingkns0909@naver.com")

pw = driver.find_element(By.CSS_SELECTOR, "#id_password_3_label")
pw.click()
pw.send.keys("Blaster_09")

loginkakao = driver.find_element(By.CSS_SELECTOR,"#login-form > fieldset > div.wrap_btn > button.btn_g.btn_confirm.submit")
loginkakao.click()

driver.get("https://ticket.melon.com/performance/index.htm?prodId=207126")   

popup_1 = driver.find_element(By.CSS_SELECTOR,"#noticeAlert_layerpopup_close")
popup_1.click()

realbutton1 = driver.find_element(By.CSS_SELECTOR,"#dateSelect_20220917 > button > span")
realbutton1.click()

realbutton2 = driver.find_element(By.CSS_SELECTOR,"#list_time > li > button > span")
realbutton2.click()

realbutton3 = driver.find_element(By.CSS_SELECTOR,"#ticketReservation_Btn")
realbutton3.click()