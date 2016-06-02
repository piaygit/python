#-*-coding=utf-8 -*-
class read_mail(object):

    def __init__(self):
        self.mail_list=[]


    def ReadMail(self):
        '''
        读取一个文件中的邮箱，返回一个收件方列表
        :return:
        '''
        for line in open(r'D:\python\email_test\email'):
            if line.strip() is not None and line  not in self.mail_list:
                self.mail_list.append(str(line).strip())
        # print self.mail_list
        return self.mail_list



