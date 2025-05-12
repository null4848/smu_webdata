import requests
from bs4 import BeautifulSoup
import csv

sum = 0

### 파일 저장
ff = open("w0512/stock.csv","a",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)

for j in range(1,6):
    url = f"https://finance.naver.com/sise/sise_market_sum.naver?&page={j}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status() # 에러 발생시 종료

    # 파싱
    soup = BeautifulSoup(res.text,"lxml")

    ### 상단타이틀 저장부분
    if j ==1:

        title = []
        tdata = soup.find("thead")
        ths = tdata.find_all("th")
        for th in ths[:-1]:
            title.append(th.get_text().strip())

        ## 파일 저장  
        writer.writerow(title)

    data = soup.find("tbody")
    trs = data.find_all("tr")
    # print(trs[1])

    for tr in trs:
        tds = tr.find_all("td")
        contents = []
        if len(tds) <= 1:
            continue
        
        for i,td in enumerate(tds):
            if i==2:
                number = td.get_text().strip()
                contents.append(number)
                price = number.replace(",","") # 천단위 표시 제거
                sum += int(price)
                print(price)
                continue

            if i == 3:
                em1 = td.find("em").get_text().strip()
                span1 = td.find("span",{"class":"tah"}).get_text().strip()
                contents.append(em1+span1)
                print(em1+span1)
                continue
            tcontents = td.get_text().strip()
            contents.append(tcontents)
            print(tcontents)
        writer.writerow(contents) # 내용파일저장
        print("-"*50)
        
    
print(f"총합계 : {sum:,d}")    
ff.close()
print("프로그램을 종료합니다.")


# for tr in trs:
#     tds = tr.find_all("td")
#     for i, td in enumerate(tds):
#         if i==2:
#             price = td.strip().replace(",","") # 천단위 표시 제거
#             int(price)
#             sum += price
            
#             # number = td.get_text()
#             # number2 = number.replace(',','')
#             # sum += int(number2)

# print(sum)

# # td 여러개
# tds = trs[1].find_all("td")
# # print(tds)

# for td in tds:
#     print(td.get_text().strip())

# print("-"*50)
    
# tds = trs[2].find_all("td")
# # print(tds)

# for td in tds:
#     print(td.get_text().strip())

# for tr in trs:
#     tds = tr.find_all("td")
#     for td in tds:
#         print(td)
#     print()
        

# data = soup.find("thead")
# print(data)

# print("-"*50)
# th1 = data.find("th")
# print(th1)
# print("-"*50)
# ths = data.find_all("th")
# print(ths)
# print("-"*50)
# tr1 = data.find("th",{"class":"tr"})
# print(tr1.get_text())
