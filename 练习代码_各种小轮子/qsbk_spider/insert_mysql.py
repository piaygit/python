# -*-coding=utf-8 -*-
from qsbk_spider import mysql

__author__ = 'piay'


class insert_mysql(object):
    def __init__(self):
        self.dbconfig = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '',
            'db': 'spider',
            'charset': 'utf8'
        }
        self.cur = mysql.mysql(self.dbconfig)


    def insert_mysql(self, page_data):
        sql = '''
                CREATE TABLE if not exists `qsbk` (
                `username` varchar(255) NOT NULL COMMENT '用户名',
                `user_url` varchar(255) DEFAULT NULL COMMENT '用户头像url',
                `text` varchar(1000) DEFAULT NULL COMMENT '内容'
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='qsbk爬虫';
                '''
        self.cur.create(sql)  # 创建表结构
        if page_data == None or page_data == 0 or len(page_data) == 0:
            return

        for data in page_data:
            username = data[0]
            user_url = data[1]
            text = data[2]
            sql = 'insert into qsbk (username,user_url,text) values ("%s","%s","%s")' % (username, user_url, text)
            self.cur.insert(sql)





