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
url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)
soup = BeautifulSoup(browser.page_source,"lxml")

## 언론사별 랭킹뉴스 전체
data = soup.find("div",{"class":"rankingnews_box_wrap"})
## 랭킹뉴스 리스트 - 12개
rNews = data.find_all("div",{"class":"rankingnews_box"})


for r in rNews:
    ## 언론사 이름
    newsName = r.find("strong",{"class":"rankingnews_name"}).get_text().strip()
    print(newsName)

    ## 기사제목
    newsContent = r.find("a",{"class":"list_title"}).get_text().strip()
    print(newsContent)
    
    writer.writerow([newsName, newsContent])
    
f.close()
    
# 파일 생성하는 동안 잠시 대기
time.sleep(2)
    
#중요 부분
password="Z1MD26V1SZK8"
recvMail = "seungmin0055@gmail.com"

# 파일 첨부 부분
# MIME 객체화
msg = MIMEMultipart('alternative')

# 보내는 글 내용
text = """<h2>랭킹뉴스 기사 모음<h2>
<img src = 'https://mail.naver.com/read/image/original/?mimeSN=1747271376.577487.342.18176&offset=1764&size=4808542&u=chanyeol0406&cid=ea8c5027f82ae8b8b5d4db94f03b1cdc@cweb003.nm&contentType=image/jpeg&filename=1747271368772.jpeg&org=1'>
"""
part2 = MIMEText(text,"html")
msg.attach(part2)
msg['From'] = "chanyeol0406@naver.com"
msg['To'] = recvMail
msg['Subject'] = "시가총액 250개 주식 정보를 보냅니다."

# 파일 첨부
part = MIMEBase('application', "octet-stream")

## 파일 읽어오기
with open("w0515/news.csv","rb") as f:
    # part 담기
    part.set_payload(f.read())
    
# 파일 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)
## header 정보
part.add_header('Content-Disposition','attachment', filename='시가총액')
msg.attach(part)

# 메일 발송 부분
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("chanyeol0406", password)
# 보내는 주소가 네이버메일이 아니면 에러 처리
s.sendmail("chanyeol0406@naver.com", recvMail, msg.as_string())
s.quit()

print("메일 발송 완료")

input("끝내려면 enter")