
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
from datetime import datetime
# standard_time = datetime(2025,5,31,17,00,00)
# now_time = datetime(2025,5,31,15,00,00)

# print(standard_time)
# print(now_time)
# print(standard_time>now_time)


# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

### 네이버 항공권
url = "https://flight.naver.com/"
browser.get(url)
time.sleep(2) # 페이지 로딩 대기

### 네이버 항공권
# 김포, 제주 5/31 - 6/1
# 금액 9만원 이하 제외
# 김포 출발 시간 17:00 이후 제외

# 창닫기
elem = browser.find_element(By.CLASS_NAME,"FullscreenPopup_close")
elem.click()

# 출발공항클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]')
elem.click()
time.sleep(1)

# 김포 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button')
elem.click()
time.sleep(1)

# 도착공항클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]')
elem.click()
time.sleep(1)

# 제주 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button')
elem.click()
time.sleep(1)

# 가는날 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(1)

# 5/31 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[7]/button')
elem.click()
time.sleep(1)

# 6/1 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/button')
elem.click()
time.sleep(1)

# 항공권 검색 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button')
elem.click()
time.sleep(6)

# 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바 스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 실행
while True:
    # 현재 브라우저에 현재 높이까지 스크롤 내리기
    # 자바 스크립트 실행
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    # 변동된 현재 문서 높이를 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤 높이가 변동이 없을 시 
    if curr_height == prev_height: break 
    prev_height = curr_height # 현재 높이를 다시 입력해서 스크롤 내리기 재실행

print("스크롤 내리기 종료")

soup = BeautifulSoup(browser.page_source,"lxml")
data = soup.find("div",{"class":"domestic_results__gp5WB"})
divs = data.find_all("div",{"class":"domestic_inner__8geIy"})

for div in divs:
    title = div.find("div", {"class": "domestic_item__5CAye"})
    # airport = title.find("span", {"class": "airline_Airline__uUBCa"})
    # title_airport = airport.find("b", {"class": "airline_name__0Tw5w"}).get_text().strip()
    # print("항공사:", title_airport)

    bottom = div.find("div", {"class": "domestic_prices__WBiv_"})
    price = bottom.find("b", {"class": "domestic_price__SAqlB"})
    bottom_price = price.find("i", {"class": "domestic_num__ShOub"}).get_text().strip()
    print("가격:", bottom_price)
    print("-" * 40)
    
    if int(bottom_price.replace(",", "")) <= 110000: continue


input("엔터")
