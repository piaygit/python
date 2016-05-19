#coding=utf-8
#装饰器,在程序开始和结束分别打印start和end
import functools
def log(hh):
    @functools.wraps(hh)
    def m(*args,**kw):
        print "start"
        q= hh(*args,**kw)
        print  "end"
        return q
    return m
@log
def now():
    print "1"
now()