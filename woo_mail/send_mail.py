# E-mail
import smtplib
from email.mime.text import MIMEText

class send_message:
    def __init__(self, email_id, email_pw):
        self.email_id = email_id
        self.email_pw = email_pw

    def send(self, to_mail, title= '제목을 입력해주세요', msg= '내용을 입력해주세요'):
        try:
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login(self.email_id, self.email_pw)
            msg = MIMEText(msg)
            msg['Subject'] = title
            smtp.sendmail(self.email_id, to_mail, msg.as_string())

        finally:
            smtp.quit()

    def __call__(self):
        return self.send()
    