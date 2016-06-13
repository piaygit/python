# -*- coding=utf-8 -*-
import MySQLdb,sys
reload(sys)
sys.setdefaultencoding('utf-8')


class mysql(object):
    _conn = None  # 数据库连接
    _cur = None  # 数据库游标

    def __init__(self, conn_db):
        '''

        :param conn_db: 数据库连接配置
        :return:
        '''
        try:
            self._conn = MySQLdb.Connect(
                host=conn_db['host'],
                user=conn_db['user'],
                passwd=conn_db['passwd'],
                db=conn_db['db'],
                charset=conn_db['charset'],
                port=conn_db['port']
            )
        except MySQLdb.Error, e:
            print e

        self._cur = self._conn.cursor()

    def select(self, sql):
        '''
        查询
        :param sql:
        :return:
        '''
        try:
            self._cur.execute(sql)
        except MySQLdb.Error, e:
            print e

    def fetchAllows(self):
        '''
        返回结果，一个list
        :return:
        '''
        return self._cur.fetchall()


    def insert(self, sql):
        '''
        插入
        :param sql:
        :return:
        '''
        try:
            self._cur.execute(sql)
            self._conn.commit()
            print 'success:'+sql
            return self._conn.insert_id()
        except MySQLdb.Error, e:
            raise e

    def create(self, sql):
        '''
        见表
        :param sql:
        :return:
        '''
        if self.is_tables('51job'):  # 判断是否存在表qsbk
            try:
                self._cur.execute(sql)
                self._conn.commit()
            except MySQLdb.Error, e:
                print e
        else:
            print '已经存在表结构'

    def is_tables(self, table):
        '''
        判断表是否存在
        :param table:
        :return:
        '''
        self._cur.execute('show tables')
        # 得到返回的table 类型为：
        # ((u'card_province',), (u'city_code',), (u'city_code1',), (u'qsbk',), (u'shop_code',))的数据
        result = self.fetchAllows()
        tables = [result[i][0] for i in range(len(result))]
        if table not in tables:
            return 1
        else:
            return 0







