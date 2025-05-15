import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

# 페이지 접속

for j in range(1,6):
    url = f"https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2025-05-16&checkOut=2025-05-17&personal=2&freeForm=true&page={j}"
    browser.get(url)
    time.sleep(2) # 페이지 로딩 대기

    soup = BeautifulSoup(browser.page_source,"lxml")

    # 위치점 가져오기
    data = soup.find("div", {"class":"css-1qumol3"})
    # print(data)

    ### 1페ㅔ이지 20개 가져오기
    hotels = data.find_all("a",{"target":"_blank"})
    # print(hotels)

    # 평점 9.1미만 평가수 1000미만 제외 후 출력
    for i,hotel in enumerate(hotels):

        title = hotel.find("h3",{"class":"gc-thumbnail-type-seller-card-title"}).get_text()
        
        rank = hotel.find("span",{"class":"css-9ml4lz"}).get_text()
        rank = float(rank)
        
        rating = hotel.find("span",{"class":"css-oj6onp"})
        rating = rating.get_text().strip().replace(",","")
        rating = int(rating[:-4])
        
        
        if rank < 9.1 and rating < 1000:
            print("*** 평점 평가수 미만 제외 ***")
            continue
        
        print(20*(j-1)+i+1)
        print(title)
        print(rank)
        print(rating)
        
        price = hotel.find("span",{"class":"css-5r5920"})
        if price != None:
            print(price.get_text()) # 데이터가 없을 때 출력시 error
        else:
            print("다른 날짜 확인")
        print("-"*30)

# 프로그램 종료 
input("프로그램 종료 (엔터키 입력) ")