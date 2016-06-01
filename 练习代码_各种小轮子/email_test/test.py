#-*-coding=utf-8 -*-
__author__ = 'piay'
import smtplib


from_addr='your email'
password='密码'
smtp_server='smtp.163.com'
to_addr='邮箱'

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)  #登录smtp服务器
server.sendmail(from_addr,[to_addr],'test')#sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list
server.quit()