import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
import random

# # 크롬 옵션 설정
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
# options.add_argument("start-maximized")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# # 브라우저 실행
# browser = webdriver.Chrome(options=options)

# # 네이버 접속 -> 검색창 시가 총액 입력 -> enter 키 입력 -> 삼성 전자 클릭 이동

# # 네이버 접속
# url = "https://www.naver.com/"
# browser.get(url)
# time.sleep(2) # 페이지 로딩 대기


# # 검색창 시가 총액 입력
# elem = browser.find_element(By.ID,"query")
# elem.send_keys("시가 총액")
# time.sleep(1)

# # enter 키 입력
# elem.send_keys(Keys.ENTER)
# time.sleep(1)

# # 삼성 전자 클릭 이동
# elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a')
# elem.click()
# time.sleep(1)

# browser.switch_to.window(browser.window_handles[0])
# browser.back()

# # 프로그램 종료 
# input("프로그램 종료 (엔터키 입력) ")

### fly1.html 불러오기
## 항공사 추랍ㄹ시간 도착시간 금액 출력

with open ("w0513/fly1.html", "r", encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

    
datas = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})

dataList = []
for i,data in enumerate(datas):
    # print(data)
    
    airport = data.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()
    # print(airport)
    
    flightime = data.find_all("b",{"class":"route_time__xWu7a"})
    starttime = flightime[0].get_text().strip()
    # print(starttime)
    
    endtime = flightime[1].get_text().strip()
    # print(endtime)r
    
    price = data.find("i",{"class":"domestic_num__ShOub"}).get_text().strip()
    price = int(price.replace(",",""))

    dataList.append([i+1, airport, starttime, endtime, price])
    
    
dataList.sort(key=lambda x: x[4])
for data in dataList:
    print(data)
    
    