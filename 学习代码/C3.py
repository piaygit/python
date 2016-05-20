#coding=utf-8
#多重继承C3算法
class A(object):
    pass
class B(A):
    pass
class C(B):
    pass
class D(A):
    pass
class E(D):
    pass
class F(C,E):
    pass
print F.__mro__

#c->b->a->object
#e->d->a->object
#遇到节点，就去遍历其他分支，最后结算节点
#c3算法的顺序为：F,C,B,E,D,A,O