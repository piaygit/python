#-*— coding=utf-8 -*-
import mysql,uuid

def get_code(number=200):
    code_list=[]
    for i in range(number):
        uuid1 = uuid.uuid1()
        code=str(uuid1).replace('-','')
        code_list.append(code)
    return code_list

code_list=get_code(200)

dbconfig={
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': '',
        'db': 'spider',
    }
db=mysql.mysql_conn(dbconfig)
# creat_sql = 'create table shop_code(id int,shop_code char)'
# db.create('create table test(id int,info varchar(20))')


for i in code_list:
    sql='insert into shop_code (shop_code) values ("%s")'%(str(i))
    db.insert(sql)
    if db.err_code==1193:
        print '找不到表或者列，错误码：1193'
        break
