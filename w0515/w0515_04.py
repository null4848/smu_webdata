import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random
import pyautogui # 마우스 제어
# 메일관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화


## csv 파일 생성
f = open('w0515/news.csv', 'w', encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = ['언론사','기사제목']
writer.writerow(title)

### 1. 네이버 접속
url = "https://www.daum.net/"
browser.get(url)

# pyautogui 마우스 제어 라이브러리 
# pyautogui.doubleClick()
pyautogui.sleep(1)
pyautogui.scroll(-700) # 아래방향으로 700만큼 이동
pyautogui.sleep(1)
pyautogui.scroll(500) # 위방향으로 500만큼 이동
pyautogui.sleep(2)
pyautogui.moveTo(800,500)
pyautogui.sleep(1)
pyautogui.moveTo(500,500)
pyautogui.click()

input("종료시 엔터")

