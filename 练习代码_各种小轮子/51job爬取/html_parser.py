#-*- coding=utf-8 -*-
import requests,sys,mysql
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

class html_parser(object):

    def __init__(self):
        self.dbconfig = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '',
            'db': 'spider',
            'charset': 'utf8'
        }
        self.code=0
        self.cur=mysql.mysql(conn_db=self.dbconfig)


    def get_data(self,url):
        page=requests.get(url)
        self.code=page.status_code
        page.encoding='gbk'
        page=page.text.strip()
        soup=BeautifulSoup(page,'html5lib')
        soup=soup.find_all('div',attrs={'class':'el'})
        for data in soup:
            title=None
            name=None
            data1=data.find_all('a',attrs={'target':'_blank'})
            # 职位名称，公司名称
            if data1 is not None and len(data1)!=0:
                title=data1[0]['title']
                name=data1[1]['title']
            # 公司地址
            data2=data.find('span',attrs={'class':'t3'})
            if data2 is not None and len(data2)!=0:
                address=data2.string
            # 钱
            data3 = data.find('span', attrs={'class': 't4'})
            if data3 is not None and len(data2) != 0:
                money = data3.string
            # 发布时间
            data4 = data.find('span', attrs={'class': 't5'})
            if data4 is not None and len(data2) != 0:
                date = data4.string

            if title is not None and name is not None:
                sql='insert into 51job (title,name,address,money,date) values ("%s","%s","%s","%s","%s")'%(title,name,address,money,date)
                self.cur.insert(sql)










# m=html_parser()
# for i in range(1,100111):
#     url='http://search.51job.com/jobsearch/search_result.php?jobarea=090200%2C00&keyword=%E6%B5%8B%E8%AF%95&keywordtype=2&curr_page='+str(i)
#     m.get_data(url)
#     if m.code!=200:
#         break