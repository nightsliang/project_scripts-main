# -*- coding: utf-8 -*-
# @author:六柒
# @time  :2019-09-23 09:24:25
import smtplib
# 引入smtplib和MIMEText
from email.mime.text import MIMEText
from time import sleep

class EmailHepler(object):
    def __init__(self):
        # 设置发件服务器地址
        self.host = 'smtp.163.com'
        # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
        self.port = 465
        # 设置发件箱
        self.sender = 'liangqi_up@163.com'
        # 设置授权码
        self.pwd = 'mi950420'
        # 设置邮件接收人
        self.receiver = 'liangqi_up@foxmail.com'

    def write_email(self, ithem, content):
        # 设置正文为符合邮件格式的HTML内容
        msg = MIMEText('<h1>{}</h1><80002778>{}</80002778>'.format(ithem, content), 'html')
        # 设置邮件标题
        msg['subject'] = '代码通知'
        # 设置发送人
        msg['from'] = self.sender
        # 设置接收人
        msg['to'] = 'liangqi_up@foxmail.com'
        return msg

    def send_email(self,msg):
        try:
            s = smtplib.SMTP_SSL(self.host, self.port)
            # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            s.login(self.sender, self.pwd)
            # 登陆邮箱
            s.sendmail(self.sender, self.receiver, msg.as_string())

            # 发送邮件！
            print('Done.sent email success')
        except smtplib.SMTPException:
            print('Error.sent email fail')

    def receive_email(self):
        pass

if __name__ == '__main__':
    user = EmailHepler()
    msg = user.write_email('努力工作', '今天加班吗？兄弟')
    user.send_email(msg)





# if __name__ == '__main__':
#     sentemail()
