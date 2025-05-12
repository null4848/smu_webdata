import requests
from bs4 import BeautifulSoup
import csv

with open ("w0509/게시판3.html", "r", encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
        
# html 태그 출력 soup.title
print(soup.title)
print(soup.title.get_text())
# 속성 출력 soup.a['href']
print(soup.a['href'])
# find(), find_all()
# print(soup.find("thead"))
data = soup.find("thead")
ths = data.find_all("th")
print("th 개수 : ",len(ths))

# for i in range(len(ths)-1):
#     print(ths[i])

# 파일저장
fileName = "board.csv"
ff = open("w0509/"+fileName,"w",encoding="utf-8-sig", newline="")
# with open("w0509/"+fileName,"w",encoding="utf-8-sig", newline="") as ff:
writer = csv.writer(ff)

txt = "qjsgh,wp"

####################################################### 1 
# 상단 제목 저장
topTitle = []
for i, th in enumerate(ths):  
    if i<5: 
        print(th.get_text(), end="\t")
        topTitle.append(th.get_text())
writer.writerow(topTitle) # 리스트타입만 입력 가능
print()

####################################################### 2
data2 = soup.find("tbody")
trs = data2.find_all("tr")
# print("tr 개수 : ",len(trs))
for tr in trs:
    tds = tr.find_all("td")
    if len(tds)<=1: continue
    bodyData = [] # 게시글 부분 데이터 저장
    for i,td in enumerate(tds):
        if i<5:
            print(td.get_text(), end="\t")
            bodyData.append(td.get_text())
    writer.writerow(bodyData) # 파일에 게시글 1개를 저장
    print()

print("저장 완료")

# theads = soup.thead.find_all("th")
# # print(theads)
# tbodys = soup.tbody.find_all("tr")
# # print(tbodys)

# for thead in theads:
#     print(thead.get_text())
# print()

# for tbody in tbodys:
#     tds = tbody.find_all("td")
#     if(len(tds)>1):
#         for i in range(len(tds)-1):
#             print(tds[i].get_text())
#         print()
