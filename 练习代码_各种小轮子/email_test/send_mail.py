#-*-coding=utf-8 -*-
import smtplib

__author__ = 'piay'

class send_mail(object):



    def SendEmail(self,from_addr,to_addr,message):
        try:
            server=smtplib.SMTP()
            server.connect('smtp.qq.com',25) # 登录邮件服务器
            server.login(from_addr['from_addr'],from_addr['passwd']) # 登录发送邮件
            server.set_debuglevel(1)
            server.sendmail(from_addr['from_addr'],to_addr,message)
        except:
            print 'error'




