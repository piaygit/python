#-*-coding=utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText

__author__ = 'piay'
from email.mime.multipart import MIMEMultipart
class structure_email(object):
    '''
    构造邮件模块
    '''


    def StrctureEmail(self):

        msg=MIMEMultipart()  # 创建一个带附件的实例
        subject='简单封装邮件模块'
        msg['Subject']=Header(subject,'utf-8')
        att = MIMEText(open('./email').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="1111"'  # 附件名称
        msg.attach(att)  # 将附件添加到邮件中
        if msg is not None:
            return msg


