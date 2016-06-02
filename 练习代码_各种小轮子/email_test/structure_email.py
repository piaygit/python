#-*-coding=utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText

__author__ = 'piay'
from email.mime.multipart import MIMEMultipart
import os
class structure_email(object):
    '''
    构造邮件模块
    '''


    def StrctureEmail(self,file_path):
        '''
        创建邮件的msg:标题，附件，正文，附件名
        :param file_path:
        :return:
        '''
        msg=MIMEMultipart()  # 创建一个带附件的实例
        subject='ptyhon-smtp 邮件封装'
        msg['Subject'] = Header(subject, 'utf-8')
        if file_path is not None:
            att=MIMEText(open(file_path).read(),'base64','utf-8')
            att["Content-Type"] = 'application/octet-stream'
            filename='attachment; filename=""'+os.path.split(file_path)[-1] #获取到文件名，当做附件名
            att["Content-Disposition"] =str(filename)  # 附件名称
            msg.attach(att)  # 将附件添加到邮件中

        if msg is not None:
            msg.attach(MIMEText('封装邮件的正文','plain','utf-8'))
            return msg


