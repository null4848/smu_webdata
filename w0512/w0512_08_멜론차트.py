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

# 페이지 집속
url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(3) # 페이지 로딩 대기

soup = BeautifulSoup(browser.page_source,"lxml")

# 1-100등
# 순위  곡정보       가수   좋아요   이미지링크
# 1    너에게 닿기를 10cm   59060   https://

# 합계 : 좋아요 총개수 : 100,000
# 파일 melon1.jpg ... melon100.jpg


ff = open("w0512/melon_chart.csv","w",encoding="utf-8-sig")
writer = csv.writer(ff)

title = ['순위', '곡정보', '가수', '좋아요']
writer.writerow(title)
data = soup.find("tbody")
trs = data.find_all("tr")
for tr in trs:
    tds = tr.find_all("td")

    dataList = []
    
    # 순위
    rank = tds[1].find("span",{"class":"rank"}).get_text()
    print(rank)
    
    # 곡제목
    song = tds[5].find("div", {"class":"rank01"}).a.get_text()
    print(song)

    # 가수
    singer = tds[5].find("div", {"class":"rank02"}).a.get_text()
    print(singer)

    # 좋아요
    cnt = tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip()
    ### 천단위표시제거, int타입으로 변경
    cnt = int(cnt.replace(",",""))
    print(cnt)
    
    writer.writerow([rank,song,singer,cnt])
    
    # 이미지저장
    imgUrl = tds[3].img["src"]
    img_res = requests.get(imgUrl)
    with open(f"w0512/images/melon_chart{rank}.jpg","wb") as f:
        f.write(img_res.content)
    print(imgUrl)
    
ff.close()

print("프로그램 종료")

#############################################################################################################

# total = 0

# for i, tr in enumerate(trs):
#     tds = tr.find_all("td")
    
#     srank = tds[1].find("span",{"class":"rank"}).get_text().strip()
    
#     simgUrl = tds[3].img["src"]
#     img_res = requests.get(simgUrl)
#     with open(f"w0512/melon{i}.jpg","wb") as f:
#         f.write(img_res.content)
        
#     div_title = tds[5].find("div", {"class":"ellipsis rank01"})
#     stitle = div_title.find("a").get_text().strip()
    
#     div_singer = tds[5].find("div",{"class":"ellipsis rank02"})    
#     ssinger = div_singer.find("a").get_text().strip()
    
#     slike = tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip()
#     ### 천단위표시제거, int타입으로 변경
#     slike_cnt = int(slike.replace(",",""))
    
#     total += slike_cnt
    
#     print(f"{srank}\t{stitle}\t{ssinger}\t{slike_cnt}\t{simgUrl}\t")

    
# print("합계 : 좋아요 총개수 : ", total)

input("종료시 enter>> ")