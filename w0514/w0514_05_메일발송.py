import smtplib
from email.mime.text import MIMEText

# 중요 정보
sendEmail="seungmin0055@gmail.com"
password="Z1MD26V1SZK8"
recvEmail = "seungmin0055@gmail.com"

# 보내는 글 내용
text = "날씨 정보 오늘 날씨 : 맑음, 내일날씨 : 흐리고 비"

msg = MIMEText(text)
msg['Subject'] = "웹스크래핑 이메일 보내기"
msg['From'] = "chanyeol0406@naver.com"
msg['To'] = recvEmail

s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("chanyeol0406@naver.com", password)

## 보내는 주소가 네이버 메일이 아니면 에러 처리
s.sendmail("chanyeol0406@naver.com",recvEmail, msg.as_string())
s.close()

print("메일 발송 완료")
