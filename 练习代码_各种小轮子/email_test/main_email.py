#-*-coding=utf-8 -*-
import smtplib

from email_test import structure_email, from_email, send_mail, read_mail

__author__ = 'piay'

class main_email(object):
    def __init__(self):
        self.strcture_email=structure_email.structure_email()   # 构造邮件
        self.from_email=from_email.from_email()  # 发件方
        self.read_mail=read_mail.read_mail()   # 读取收件人邮件列表
        self.send_mail=send_mail.send_mail()  # 发邮件


    def sendmail(self):
        to_addr1='luoyong@medlinker.com'
        message=self.strcture_email.StrctureEmail()  # 邮件message
        from_addr=self.from_email.FromEmail() #得到发件人邮件和密码的字典
        to_addr=self.read_mail.ReadMail()    # 得到一个收件人list
        message['From']=from_addr['from_addr']
        message['To']=to_addr1
        # self.send_mail.SendEmail(from_addr,list(to_addr),message.as_string())
        server=smtplib.SMTP()
        server.set_debuglevel(1)
        server.connect('smtp.qq.com',25)
        server.login(from_addr['from_addr'],from_addr['passwd'])
        server.sendmail(from_addr['from_addr'],to_addr1,message.as_string())






if __name__=='__main__':

    # 构造一个发送邮件实例
    send_email=main_email()
    # 调用邮件发送方法
    send_email.sendmail()