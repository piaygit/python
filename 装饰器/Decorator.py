#coding=utf-8
#װ����,�ڳ���ʼ�ͽ����ֱ��ӡstart��end
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