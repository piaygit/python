#-*- coding=utf-8 -*-
import MySQLdb
def conn_mysql():
    '''

    :return: 返回一个数据库连接
    '''
    try:
        conn=MySQLdb.Connect(
            host="127.0.0.1",
            port=3306,
            user='root',
            passwd='',
            db='spider'
        )
    except:
        print("检查你的数据库连接是否正确")
    return conn
def update_database(sql,*args):
    conn=conn_mysql()
    cur=conn.cursor()
    m1=cur.execute(sql,args)
    return m1
m=update_database('select count(*) from city_code')
print m





