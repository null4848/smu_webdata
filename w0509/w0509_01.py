# requests 라이브러리 - 웹 정보 요청하는 라이브러리 (문자열로 받아옴)
# beautifulsoup4 라이브러리 - HTML 및 XML 파일에서 원하는 데이터를 손쉽게 Parsing 할 수 있는 라이브러리
# lxml 라이브러리 - css 문법으로 특정 요소를 쉽게 가져올 수 있는 라이브러리

# 웹크롤링 - Web 상에 존재하는 컨텐츠를 수집하는 작업(프로그래밍으로 자동화 가능)

import requests

# 사이트 접속해서 html 소스를 가져옴.
# res = requests.get("https://www.google.com/") # 접근 가능
# res = requests.get("https://www.melon.com/")
# 파이썬에서 웹스크래핑 -> 
res = requests.get("https://www.naver.com/")

if res.status_code == 200:
    print("정상적인 프로그램 진행")
    print(res)
    # 200 - 정상코드 / 400~404 - 페이지 없음, 접근제한 / 500 - 프로그램 에러
    print("응답코드 : ",res.status_code) 
    # res.raise_for_status() # 에러 발생 시 종료
    print(res.text) # text 글자 타입으로 출력
else:
    print("프로그램 종료")
