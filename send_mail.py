# E-mail
import smtplib
import time
from email.mime.text import MIMEText
import email.utils

from password import mail_info

class send_message:
    def __init__(self, to_mail, title= '제목을 입력해주세요', msg= '내용을 입력해주세요'):
        self.to_mail = to_mail
        self.title = title
        self.msg = msg

        self.__config = mail_info()

    def send(self):
        try:
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login(self.__config['id'], self.__config['pw'])
            msg = MIMEText(self.msg)
            msg['Subject'] = self.title
            smtp.sendmail(self.__config['id'], self.to_mail, msg.as_string())

        finally:
            smtp.quit()

    def __call__(self):
        return self.send()
    