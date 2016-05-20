#coding=utf-8
import functools
def log(text):
    if callable(text): #函数执行步骤
        @functools.wraps(text)
        def wrapper(*args,**kwargs):
            print "start"+text.__name__
            p=text(*args,**kwargs)
            print "end"+text.__name__
            return p
        return wrapper
    else:      #传入的是字符串
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
now(1)#其实调用log(now)
now1()#其实调用log("222",now)