import requests
from bs4 import BeautifulSoup
import csv # csv 파일 저장

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status() # 에러 발생시 종료
soup = BeautifulSoup(res.text, "lxml")

# print(soup.thead)

ff = open("w0509/stock.csv","w",encoding="utf-8-sig", newline="")
writer = csv.writer(ff)

ths = soup.thead.find_all("th")

fileName = []
for th in ths:
    print(th.get_text(),end="\t")
    fileName.append(th.get_text())
writer.writerow(fileName)

## 내용 부분 5개 -> 50개 저장

trs = soup.tbody.find_all("tr")
print("tr 게수 : ",len(trs))

for tr in trs:
    tds = tr.find_all("td")
    if len(tds)<=1: continue
    print(tds)
    for td in tds:
        print(td.get_text().strip(),end="\t")
    print()



ff.close()
print("파일저장 완료")
    