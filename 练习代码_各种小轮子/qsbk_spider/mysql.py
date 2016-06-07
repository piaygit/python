#-*- coding=utf-8 -*-
import  MySQLdb
class mysql(object):

    _conn=None #数据库连接
    _cur=None #数据库游标

    def __init__(self,conn_db):
        try:
            self._conn=MySQLdb.Connect(
            host=conn_db['host'],
            user=conn_db['user'],
            passwd=conn_db['passwd'],
            db=conn_db['db'],
            charset=conn_db['charset'],
            port=conn_db['port']
            )
        except MySQLdb.Error,e:
            print e

        self._cur=self._conn.cursor()

    def select(self,sql):
        try:
            self._cur.execute(sql)
        except MySQLdb.Error,e:
            print e

    def fetchAllows(self):
        return self._cur.fetchall()


    def insert(self,sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except MySQLdb.Error,e:
            print e

    def create(self,sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error,e:
            print e




#
# if __name__=='__main__':
#     '''
#     使用说明
#     '''
#     dbconfig={
#         'host': '127.0.0.1',
#         'port': 3306,
#         'user': 'root',
#         'passwd': '',
#         'db': 'spider',
#         'charset':'utf8'
#     }
# #连接数据库，创建这个类的实例
# db=mysql(dbconfig)
# sql='select count(*) from code_city'
# db.create()



