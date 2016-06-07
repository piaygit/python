# -*-coding=utf-8 -*-
import re

from qsbk_spider import mysql

__author__ = 'piay'

import requests
from bs4 import BeautifulSoup

class main_spider(object):


    def __init__(self,dbconfig):
        self.cur=mysql.mysql(dbconfig)


    def craw(self, url):
        try:
            page=requests.get(url)
            page.encoding='utf-8'
            respone=page.text.strip()
            respone=respone.replace('<br/>','')
            respone=respone.replace('\n','')
        except:
            print 'error'
        soup=BeautifulSoup(respone,'html5lib')
        texts=soup.find_all('div',attrs={'class':'article block untagged mb15'})
        qsbk_list=[]

        # 创建表结构，如果存在就不创建
        sql='''
        CREATE TABLE `qsbk` (
        `username` varchar(255) NOT NULL COMMENT '用户名',
        `user_url` varchar(255) DEFAULT NULL COMMENT '用户头像url',
        `text` varchar(255) DEFAULT NULL COMMENT '内容'
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='qsbk爬虫';
        '''
        self.cur.create(sql)
        for text in texts:
            # 获取用户名和头像
            users=text.findAll('img')
            for user in users:
                username = user['alt']  #用户姓名
                user_url = user['src']  #用户头像url

            # 获取正文
            qsbk=text.findAll('div', attrs={'class':'content'})
            for qsbk_text in qsbk:
                qsbk_text=qsbk_text.string  #正文

            insert_sql='insert into qsbk (username,user_url,text) values ("%s","%s","%s")'\
                       %(username,user_url,qsbk_text)
            self.cur.insert(insert_sql)






if __name__=='__main__':
    dbconfig = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '',
        'db': 'spider',
        'charset': 'utf8'
    }
    page=1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    spider=main_spider(dbconfig)
    m=spider.craw(url)


