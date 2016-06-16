# -*-coding=utf-8 -*-
__author__ = 'piay'
import time, functools


def foo():
    '''
    定义一个普通函数
    :return:
    '''
    print 'this is foo'


foo()

'''
这里如果我们需要查看函数执行时间，修改为：
'''


def foo1():
    start_time = time.clock()
    print 'this is foo1'
    end_time = time.clock()
    print '执行时间为：', end_time - start_time


foo1()

'''
如果我们其他的函数也需要执行时间，或者这个函数不需要执行时间，那么我们就需要复制到其他的函数中去
这是一种最差的方法
'''


def foo3():
    print 'this is foo3'


def timeit(func):
    '''
    我们可以考虑重新定义一个函数timeit，将foo的引用传递给他，
    然后在timeit中调用foo并进行计时，这样，我们就达到了不改动foo定义的目的
    :param func: 传入的函数
    :return:
    '''
    start_time = time.clock()
    func()
    end_time = time.clock()
    print 'used:', end_time - start_time


timeit(foo3)
'''
这样写修改调用部分的代码。原本我们是这样调用的：foo3()，现在变成timeit(foo),这样的话，如果foo在N处都被调用了，
你就不得不去修改这N处的代码。或者更极端的，考虑其中某处调用的代码无法修改这个情况，比如：这个函数是你交给别人使用的。
'''

'''
想想办法不修改调用的代码；如果不修改调用代码，也就意味着调用foo()需要产生调用timeit(foo)的效果。我们可以想到将timeit赋值给foo，
但是timeit似乎带有一个参数……想办法把参数统一吧！如果timeit(foo)不是直接产生调用效果，
而是返回一个与foo参数列表一致的函数的话……就很好办了，将timeit(foo)的返回值赋值给foo，然后，调用foo()的代码完全不用修改！
'''


def foo4():
    print 'this is foo4'


# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit4(func):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start_time = time.clock()
        func()
        end_time = time.clock()
        print 'used:', end_time - start_time

    # 将包装后的函数返回
    return wrapper


foo_1 = timeit(foo4)
'''
上面的代码就类似装饰器了，可以修改为如下：
'''


@timeit4  # 定义上加上这一行与另外写foo = timeit(foo)完全等价
def foo5():
    print 'this is foo5'
foo5()


'''
-----------------------------------------------
使用functools.wraps(func)装饰器实现功能
'''
def timeit_3_for_wraps(func):
    @functools.wraps(func)
    def wrapper():
        start=time.clock()
        func()
        end=time.clock()
        print 'used:',end-start
    return wrapper

@timeit_3_for_wraps
def foo6():
    print 'this is foo6'
foo6()

