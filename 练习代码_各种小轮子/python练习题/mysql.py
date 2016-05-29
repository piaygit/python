#-*- coding=utf-8 -*-
'''
封装mysql
'''
import MySQLdb,time
class mysql_conn(object):
    err_code='' # mysql错误码
    _instance=None #本来的实例
    _conn=None #数据库连接
    _cur=None #数据库游标

    _TIMEOUT=30 #默认超时时间为30s
    _timeout=0

    def __init__(self,dbconfig):
        try:
            self._conn=MySQLdb.Connect(
                port=dbconfig['port'],
                host=dbconfig['host'],
                passwd=dbconfig['passwd'],
                db=dbconfig['db'],
                user=dbconfig['user']
            )
        except MySQLdb.Error ,e:
            self.err_code=e.args[0]
            error_msg='Mysql error %d:%s'%(e.args[0],e.args[1])
            print error_msg

            #如果没有超过预设时间，则再次尝试连接
            if self._timeout<self._TIMEOUT:
                interval=5
                self._timeout+=interval
                time.sleep(interval)
                return self.__init__(dbconfig)
            else:
                raise Exception(error_msg)
        self._cur=self._conn.cursor()
        self._instance=MySQLdb

    def select(self,sql):
        '''
        执行select语句
        :param sql:
        :return:
        '''
        try:
            self._cur.execute('set names utf8')
            result=self._cur.execute(sql)
        except MySQLdb.Error,e:
            self.err_code=e.args[0]
            print "数据库错误代码 %d：%s"%(e.args[0],e.args[1])
            result=False
        return result

    def update(self,sql):
        '''
        执行update和delete的操作
        :param sql:
        :return:
        '''

        try:
            self._cur.execute('set names utf8')
            result=self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error,e:
            self.err_code = e.args[0]
            print "数据库错误代码 %d：%s"%( e.args[0], e.args[1])
            result = False
        return result

    def insert(self,sql):
        '''
        执行insert语句，如主键为自增长int，则返回新生成的id
        :param sql:
        :return:
        '''
        try:
            #self._cur.execute('set name utf8')
            self._cur.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except MySQLdb.Error,e:
            self.err_code=e.args[0]
            print "数据库错误代码 %d：%s" % (e.args[0], e.args[1])
            result=False
            return result

    def create(self,sql):
        '''
        创建表
        :param sql:
        :return:
        '''
        try:
            self._cur.execute('set name utf8')
            self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error,e:
            self.err_code=e.args[0]
            self.err_code = e.args[0]
            print "创建表：数据库错误代码 %d：%s" % (e.args[0], e.args[1])
            result=False
        return result
    def fetchAllRows(self):
        '''
        返回结果列表
        :return:
        '''
        return self._cur.fetchall()

    def fetchOneRow(self):
        '''
        返回一行结果，然后游标指向下一行，到达最后一行以后，返回None
        :return:
        '''
        return self._cur.fetchone()
    def getRowCount(self):
        '''
        获取结果行数
        :return:
        '''
        return self._cur.rowcount
    def commit(self):
        '''
        数据库提交操作
        :return:
        '''
        self._conn.commit()

    def rollback(self):
        '''
        回滚操作
        :return:
        '''
        self._conn.rollback()

    def __del__(self):
        '''
        释放资源（系统GC自动调用）
        :return:
        '''
        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def close(self):
        '''
        关闭数据库
        :return:
        '''
        self.__del__()



# if __name__=='__main__':
#     '''
#     使用说明
#     '''
#     dbconfig={
#         'host': 'localhost',
#         'port': 3306,
#         'user': 'root',
#         'passwd': '',
#         'db': 'spider',
#     }
# #连接数据库，创建这个类的实例
# db=mysql_conn(dbconfig)
# sql='select count(*) from city_code'
# db.select(sql)
# #获取结果列表
# result=db.fetchAllRows()
# print result
# for row in result:
#     for colum in row:
#         print colum
# db.close()

