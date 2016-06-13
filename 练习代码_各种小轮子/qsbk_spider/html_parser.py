# -*-coding=utf-8 -*-
from bs4 import BeautifulSoup

__author__ = 'piay'
'''
html页面解析
'''

import requests


class html_parser(object):
    def __init__(self):
        self.data = []

    def HtmlParser(self, url):
        if url is not None:
            try:
                page = requests.get(url)
                page.encoding = 'utf-8'
                respone = page.text.strip()
                respone = respone.replace('<br/>', '')  # 替换掉正文中的br空标签
                respone = respone.replace('\n', '')  # 替换掉换行
                soup = BeautifulSoup(respone, 'html5lib')
                # 提取正文的div
                texts = soup.find_all('div', attrs={'class': 'article block untagged mb15'})

                for text in texts:
                    list_data = []
                    # 获取用户名和头像
                    users = text.findAll('img')
                    for user in users:
                        username = user['alt']  # 用户姓名
                        user_url = user['src']  # 用户头像url
                    # 获取正文
                    qsbk = text.findAll('div', attrs={'class': 'content'})
                    for qsbk_text in qsbk:
                        qsbk_text = qsbk_text.string  # 正文
                    list_data.append(username)
                    list_data.append(user_url)
                    list_data.append(qsbk_text)
                    self.data.append(list_data)  # 将每一组数据组成一个list添加到一个总的list中去
                # print self.data
                return self.data

            except requests.ConnectionError, e:
                print '连接错误：%s', e
                return 0  # 连接错误返回0

