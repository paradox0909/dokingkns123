##This code is concert macro program (lan py)
from selenium import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome("/Users/doking/Downloads/chromedriver")

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add.experimental_option("detach", True)

#불필요한 에러 메세지 없애기
chrome_options.add.experimental_option("excludeSwitches", ["enable-logging"])


Service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)
#웹주소 이동
driver.get('https://google.com')
#셀렉터로 복사하기