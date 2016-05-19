#coding=utf-8
#�����Ƿ��в���ִ�в�ͬ��װ����
import functools
def log(text):
    if callable(text): #����ִ�в���
        @functools.wraps(text)
        def wrapper(*args,**kwargs):
            print "start"+text.__name__
            p=text(*args,**kwargs)
            print "end"+text.__name__
            return p
        return wrapper
    else:      #��������ַ���
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                print "%s start"%text
                p1=func(*args,**kwargs)
                print "end"
                return p1
            return wrapper
        return decorator

@log
def now(r):
    print r

@log("2222")
def now1():
    print 'm'
now(1)#��ʵ����log(now)
now1()#��ʵ����log("222",now)