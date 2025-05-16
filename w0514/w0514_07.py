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

### 1. 네이버 접속
url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)

soup = BeautifulSoup(browser.page_source,"lxml")

ff = open("w0514/news.csv","w",encoding="utf-8-sig")
writer = csv.writer(ff)

dataList = []
title = ['언론사','뉴스 기사 제목']
writer.writerow(title)

data = soup.find("div",{"class":"_officeCard _officeCard0"})
boxes = data.find_all("div",{"class":"rankingnews_box"})
for i,box in enumerate(boxes):
    print(i+1)
    title = box.find("a",{"class":"list_title nclicks('RBP.rnknws')"}).get_text().strip()
    print(title)
    news = box.find("strong",{"class":"rankingnews_name"}).get_text().strip()
    print(news)
    
    dataList = [news, title]
    writer.writerow(dataList)
    
ff.close()
print("프로그램 종료")

# 중요 정보
password = ""
recv_email = "onulee@naver.com"

msg = MIMEMultipart('alternative')

text = "네이버 12개 랭킹 1위 뉴스를 보내드립니다."
part2 = MIMEText(text)
msg.attach(part2)
msg['From']="chanyeol0406@naver.com"
msg['To']=recv_email
msg['Subject']="네이버 랭킹뉴스 보냄."

part = MIMEBase('application', 'octet-stream')

with open("w0514/news.csv","rb") as f:
    part.set_payload(f.read())
    
encoders.encode_base64(part)

part.add_header('Content-Disposition','attachment', filename = '언론사별 랭킹 1위 뉴스.csv')
msg.attach(part)

s = smtplib.SMTP("smtp.naver.com", 587)
s.starttls()
s.login("chanyeol0406", password)
s.sendmail("chanyeol0406@naver.com", recv_email, msg.as_string())

s.quit()

print("메일 발송 완료")


# 신문사 기사
# news.csv 파일 생성
# 뉴시스, '전원일기 일용이' 박은수 수천만원 사기 혐의로 피소
# 한국경제, '지금 계약해도 '

# 파일 첨부 메일로 발송
# 제목 : 네이버 랭킹뉴스 보냄.
# 내용 : 네이버 12개 랭킹 1위 뉴스를 보내드립니다.
# 메일 발송 주소는 onulee@naver.com