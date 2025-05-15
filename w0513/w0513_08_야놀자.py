import requests

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
import random

# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

#1 호텔/리조트 클릭
#2 지역 선택 클릭 후 제주 서귀포시/모슬포 클릭
#3 6/7 ~ 6/8 적용하기 버튼 클릭
#4 스크롤 내리기
#5 호텔, 호텔이름, 평점, 후기갯수 금액 출력
# 없으면 없음 이라고 출력

# 야놀자 접속
url = "https://nol.yanolja.com/"
browser.get(url)
time.sleep(1) # 페이지 로딩 대기

# 호텔 리조트 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/a[1]/div')
elem.click()
time.sleep(1)

# 지역 선택 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div/button')
elem.click()
time.sleep(1)

# 제주 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[1]/button[3]')
elem.click()
time.sleep(1)

# 서귀포시/모슬포 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/a[2]')
elem.click()
# time.sleep(10)

# 날짜 선택
wait = WebDriverWait(browser, 10)  # 최대 10초 대기
elem = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".mr-2.truncate.typography-body-14-regular-line-clamp-1"))
)
elem.click()
time.sleep(1)

# 6월 7일 선택
elem = browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button')
elem.click()
time.sleep(1)

# 6월 8일 선택
elem = browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button')
elem.click()
time.sleep(1)

# 적용하기 클릭
elem = browser.find_element(By.XPATH,'//*[@id="pc-dialog-sheet"]/div/div/div[3]/button')
elem.click()
time.sleep(1)

# 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height: break
    prev_height = curr_height
    
print("스크롤 내리기 종료")

#5 호텔, 호텔이름, 평점, 후기갯수 금액 출력
soup = BeautifulSoup(browser.page_source,"lxml")
datas = soup.find_all("div",{"class":"grid w-full grid-flow-row gap-[12px]"})
for data in datas:
    hotel = data.find("p",{"class":"text-text-neutral-sub typography-body-12-regular"})
    print(hotel.get_text().strip())
    
    name = data.find("p",{"class":"mb-4 line-clamp-2 text-start text-fill-neutral-main typography-subtitle-16-bold"})
    print(name.get_text().strip())
    
    stars = data.find_all("p",{"class":"flex items-center justify-start gap-2 pl-2"})

    rank = stars[0]
    print(rank.get_text().strip())
    
    people = stars[1]
    print(people.get_text().strip())
    
    price = data.find("span",{"class":"shrink-0 grow-0 text-text-neutral-main typography-subtitle-18-bold"})
    print(price.get_text().strip())


# 없으면 없음 이라고 출력


# 프로그램 종료 
input("프로그램 종료 (엔터키 입력) ")
