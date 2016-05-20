#coding=utf-8
#参考链接：https://segmentfault.com/a/1190000000749061
class A(object):
    def __init__(self):
        print "enter A"
        print "leave A"
class B(object):
    def __init__(self):
        print "enter B"
        print "leave B"
class C(A):
    def __init__(self):
        print "enter C"
        super(C,self).__init__()
        print "leave C"
class D(A):
    def __init__(self):
        print "enter D"
        super(D,self).__init__()
        print "leave D"
class E(B,C):
    def __init__(self):
        print "enter E"
        super(B, self).__init__()
        super(C, self).__init__()
        print "leave E"
class F(E,D):
    def __init__(self):
        print "enter F"
        super(E, self).__init__()
        super(D, self).__init__()
        print "leave F"

print E.__mro__
print F.__mro__
#E的C3算法顺序为：E,B,C,A,O
# super实际上是通过__MRO__序列来确定访问哪一个类的...实际上就是调用__MRO__中此类后面的一个类的方法.
e=E()
print '------------'
f=F()
# E,B,C,A,O
# 执行顺序为：super指向下一个
# print "enter E"
# super(B, self).__init__()-->等价于执行class C的__init__方法
# print "enter C"
# super(C,self).__init__()-->等价于执行class A的__init__方法
# print "enter A"
# print "leave A"
# print "leave C"
# super(C, self).__init__()-->等价于执行class A的__init__方法
# print "enter A"
# print "leave A"
# print "leave E"
#
# 所以打印为：e,c,a,a,c,a,a,e