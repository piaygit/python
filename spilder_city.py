#-*- coding=utf-8 -*-
import urllib,MySQLdb,sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )
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
            cur.execute("insert into city_code (code,city) values (%s,%s)",(str(key),str(args[key])))
        except:
            print "请检查你的插入语句是否正确"
    conn.commit()#提交insert
    #关闭连接
    cur.close()
    conn.close()
#获取页面内容
page=urllib.urlopen("http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201401/t20140116_501070.html").read()
#删除html的&nbsp空格符
page=page.replace("&nbsp;","")
#筛选出p标签的内容
soup=BeautifulSoup(page, "html5lib").find_all("p")
code_city={}
f=open("code_city","w+")
#读取p标签的text,讲code和city存入字典
for data in soup:
    #去掉空格
    if data.string!=None:
        #得到格式为：659004 五家渠市的数据
        choose_data=data.string
        f.write(choose_data+"\n")
        code_city[choose_data[0:6]]=choose_data[7:]
f.close()
insert_data(code_city)




