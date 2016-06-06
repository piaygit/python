# -*-coding=utf-8 -*-
import re

__author__ = 'piay'

import requests
from bs4 import BeautifulSoup

class main_spider(object):


    def craw(self, url):
        try:
            page=requests.get(url)
            page.encoding='utf-8'
            respone=page.text
        except:
            print 'error'
        soup=BeautifulSoup(respone,'html5lib')
        texts=soup.find_all('div',attrs={'class':'article block untagged mb15'})
        m=0
        for text in texts:
            # 获取用户名和头像
            users=text.findAll('img')
            for user in users:
                username = user['alt']
                user_url = user['src']
                #print username,user_url

            #获取正文
            qsbk=text.findAll('div', attrs={'class':'content'})
            for qsbk_text in qsbk:
                qsbk_text=qsbk_text.string
                print qsbk_text



















if __name__=='__main__':
    page=1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    spider=main_spider()
    spider.craw(url)


