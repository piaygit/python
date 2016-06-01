#-*-coding=utf-8 -*-
from email_test import structure_email, from_email, send_mail, email_type

__author__ = 'piay'

class main_email(object):
    def __init__(self):
        self.strcture_email=structure_email.structure_email()
        self.from_email=from_email.from_email()
        self.send_mail=send_mail.send_mail()
        self.email_type=email_type.email_type()


    def sendmail(self):
        email=self.strcture_email



if __name__=="__mian__":
    #构造一个发送邮件实例
    send_eami=main_email()
    #调用邮件发送方法
    send_eami.sendmail