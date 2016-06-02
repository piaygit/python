#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="luoyong@medlinker.com"    #用户名
mail_pass="Med123456"   #口令


sender = 'luoyong@medlinker.com'
receivers = ['luoyong@medlinker.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#创建一个带附件的实例
message=MIMEMultipart()

message['From'] = Header("邮件测试服务器", 'utf-8') #发件方
message['To'] =  Header("luoyong@medlinker.com", 'utf-8') #收件方
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8') #邮件标题

#邮件正文内容
message.attach(MIMEText('带附件的邮件正文','plain','utf-8'))


att1=MIMEText(open('./email').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="111"' #附件名称
# att2=MIMEText(open('./2').read(),'base64','utf-8')
message.attach(att1)
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    print smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"