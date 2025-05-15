import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#중요 부분
password="Z1MD26V1SZK8"
recvMail = "seungmin0055@gmail.com"

# 파일 첨부 부분
# msg 객체화
msg = MIMEMultipart('alternative')

# 보내는 글 내용
text = "이메일 글자 발송"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = "chanyeol0406@naver.com"
msg['To'] = recvMail
msg['Subject'] = "시가총액 250개 주식 정보를 보냅니다."

# 파일 첨부
part = MIMEBase('application', "octet-stream")

## 파일 읽어오기
with open("w0514/stock.csv","rb") as f:
    # part 담기
    part.set_payload(f.read())
    
# 파일 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)
## header 정보
part.add_header('Content-Disposition','attachment', filename='시가총액')
msg.attach(part)

# 메일 발송 부분
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("chanyeol0406", password)
recvMails = ["chanyeol0406@naver.com", "seungmin0055@gmail.com"]
for recvMail in recvMails:
    s.sendmail("chanyeol0406@naver.com", recvMail, msg.as_string())
    
s.quit()

print("메일 발송 완료")
