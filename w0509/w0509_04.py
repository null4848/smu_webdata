import requests
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/article/011/0004483132?ntype=RANKING"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

# print(res.text)
# 문자열 -> html, css 파싱
soup = BeautifulSoup(res.text, "lxml")
# print(soup) # html, css

# <title> 태그에 접근해서 가져옴
# print(soup.title)
# print(soup.title.get_text())

# print(soup.header)
# print(soup.header.div)
# print(soup.header.div.a)

## html 속성을 출력
# print(soup.header.div.a.attrs) # 속성 전체 출력
# print(soup.header.div.a['href']) # 속성 href 출력
# print(soup.header.div.a['class']) # 속성 class 출력

## id, class 속성 출력
# find() 해당태그를 검색할때 사용

# data1 = soup.find("a", attrs = {"class" : "ofhd_float_back"})
# print(data1)
# data1 = soup.find("a", {"class" : "ofhd_float_back"})
# print(data1)
# data1 = soup.find("a", class_ =  "ofhd_float_back")
# print(data1)

# data2 = soup.find("h2", attrs={"id":"title_area"})
# print(data2)
# print(data2.get_text())

# data2 = soup.find("h2", {"id":"title_area"})
# print(data2)
# data2 = soup.find("h2", id = "title_area")
# print(data2)

## find() 1개만 검색,  find_all() 복수개를 검색
ul_data = soup.find("ul", {"class" : "ranking_list"})
# li_data = ul_data.find("li",{"class":"rl_item"})
li_datas = ul_data.find_all("li",{"class":"rl_item"})
print(len(li_datas))
for li_data in li_datas:
    print(li_data.find("p",{"class":""}))