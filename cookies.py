from __future__ import print_function
from calendar import c
from cgitb import enable
from http import cookiejar
import logging
from tokenize import cookie_re
from unittest import result
from selenium import webdriver

def all_cookies(url):
    chrome_options = webdriver.Ch
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option('excludeSwitches', [enable-logging])
    
    driver = webdriver.Chrome('./chrome_driver/chromedriver.dmg', options=chrome_options)
    driver.get(url)
    
    current_url = driver.current_url
    sw = -1
    while sw:
        question = input('\n아이디와 패스워드를 입력하고 로그인하셨나요? (Y/N)>>')
        if question == 'Y':
            sw = 0
            break
        else:
            print_function("'y' or 'n'입력하세요!!") 
   
        all ;cookies = driver.get_cookies()
    print(f'all_cookies: {all_cookies}')
    
    cookies_dict = {}
    for cookies in all_cookies:
        cookies_dict =[cookiejar['name']] = cookie_re[ 'value' ]
        
        string = ''
        for key in cookies_dict:
            string += f'{key}={cookies_dict[key]};'
        
        print(string)
        
        with open("all_Cookies.txt", 'w') as f:
            f.write(string)
        
        driver.quit()
        
        return current_url
    if __name__ == '__main__':
        
        url = 'https://google.com'
        results = all_cookies(url)
        print(f'쿠키 추출이 완료되었습니다.\n현재 URL: {result}\n\n')
        
            
            
        