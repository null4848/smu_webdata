import requests
from bs4 import BeautifulSoup

# html 파일을 읽어와서 파일 html, css 형태로 파싱
with open("w0509/게시판3.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f, "lxml")

# data = soup.find("div", {"id":"input"})
# print(data.div.get_text())

# html 태그 찾는 법
# print(soup.thead)
# soup.find("thead", {"class":""})
# data = soup.find("thead")
# ths = data.find_all("th")
# for th in ths:
#     print(th.get_text())

# ths = soup.table.thead.tr.find_all("th")
# for th in ths:
#     print(th.get_text())

## find_next_sibling 이후 형제 관계 찾기, find_previous_sibling 이전형제관계찾기
# data = soup.find("div",{"id":"input"})
# data2 = data.find_next_sibling().find_next_sibling().find_previous_sibling()
# print(data2)

# print(data.div.get_text())

data = soup.find("tbody",{"id":"tbody"})
trs = data.find_all("tr")
print(len(trs))

for tr in trs:
    tds = tr.find_all("td")
    if len(tds)>1: # td가 1개인 것은 출력하지 말것
        for i in range(len(tds)-1):
            print(tds[i].get_text())
    # print(tds)
    
