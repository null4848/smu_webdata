import requests
from bs4 import BeautifulSoup
import csv # csv 파일 저장

with open("w0509/notice_list.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

# csv 파일저장
ff = open("w0509/list.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(ff) # csv list 타입 저장

#### 상단타이틀, 내용부분
trs = soup.table.find_all("tr")
# print(len(trs))

for i,tr in enumerate(trs):
    fileName = []
    if i==0: # 상단타이틀
        ths = soup.table.find_all("th")
        for th in ths:
            print(th.get_text(), end="\t")
            fileName.append(th.get_text())
        writer.writerow(fileName)
        print()
        continue
    # 내용부분
    tds = tr.find_all("td")
    for td in tds:
        print(td.get_text(), end="\t")
        fileName.append(td.get_text())
    print()
    writer.writerow(fileName)
    
print("파일 저장 완료")
    
# trs = []
# for i in range(len(datas2)):
#     if i>1:
#         trs.append(i)
        
    
# print(trs)
