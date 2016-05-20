#-*- coding=utf-8 -*-
import requests,sys,re,MySQLdb
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")
url="http://blog.sina.com.cn/s/blog_496c75c50102w48x.html"
respone=requests.get(url)
respone.encoding='utf-8'
html=respone.text
html=re.search('sina_keyword_ad_area2(.*?)div',html,re.S).group(1)
soup=BeautifulSoup(html,"html5lib").find_all("p")
card_code_city={}
for data in soup:
    try:
        if data.string[0:6].isdigit():
            card_code_city[data.string[0:6]]= data.string[7:]
    except:
        continue
def insert_data(args={}):
    '''

    :param args: 字典，code和city对应的字典
    :return: insert mysql——spider-city_code表
    '''
    try:
        #获取连接
        conn=MySQLdb.Connect(
            port=3306,
            user="root",
            passwd="",
            db="spider",
            charset="utf8"
        )
    except:
        print "请检查数据库连接是否正确"
    cur=conn.cursor()#获取游标
    for key in args.keys():
        try:
            cur.execute("insert into card_province (card_code,card_city) values (%s,%s)",(str(key),str(args[key])))
        except:
            print "请检查你的插入语句是否正确"
    conn.commit()#提交insert
    #关闭连接
    cur.close()
    conn.close()
insert_data(card_code_city)


