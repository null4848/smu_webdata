import requests
from bs4 import BeautifulSoup
import csv # csv 파일 저장

with open("w0509/join02_info_input.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
ff = open("w0509/title.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(ff)

fieldsets = soup.find_all("fieldset")
# print(fieldsets)

titleList = []
for fieldset in fieldsets:
    dts = fieldset.find_all("dt")
    for dt in dts:
        print(dt.get_text().strip(), end=" ")
        titleList.append(dt.get_text().strip())
writer.writerow(titleList)
print()

ff.close()

print("파일 저장 완료")





