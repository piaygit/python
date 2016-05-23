#!/usr/bin/python 
#-*- coding=utf-8 -*-
#db.py
import threading

#数据库引擎对象
class _Engine(object):
    def __init__(self,connect):
        self._connect=connect
    def connect(self):
        return self._connect

engine=None

#持有数据库连接的上下文对象
class _DbCtx(threading.local):
    def __init__(self):
        self.connection=None
        self.transactions=0
    def is_inint(self):
        return not self.connection is None
    def init(self):
        self.connection=_LasyConnection()
        self.transactions=0
    def cleanup(self):
        self.connection.cleanup()
        self.connection=None
    def cursor(self):
        return self.connection.cursor()
_db_ctx = _DbCtx()
