#-*-coding=utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    print name,addr
    return formataddr((Header(name,'utf-8').encode(),addr.encode('utf-8')if isinstance(addr,unicode)
                      else addr))

from_addr='1111'
password='1111'
smtp_server='smtp.qq.com'
to_addr='1111'
msg = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')


msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)

msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)

msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()





server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)  #登录smtp服务器
server.sendmail(from_addr,[to_addr],msg.as_string())#sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list
server.quit()