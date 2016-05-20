#-*- coding=utf-8 -*-
class student(object):
    '''
    @property装饰器就是负责把一个方法变成属性调用
    '''
    @property
    def socre(self):
        return self._score
    @socre.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError ('成绩必须为整数')
        if value<0 or value>100:
            raise ValueError ("请输入1-100的成绩")
        self._score=value
s=student()
s.score=50
print s.score

class chain(object):
    '''
    __getattr__:动态返回一个属性，调用不存在的方法或者属性时会执行
    本例子：动态生成一个链式调用（可用于api调用）
    '''
    def __init__(self,url=""):
        self._url=url
    def __getattr__(self, url):
        return chain("%s/%s"%(self._url,url))
    def __str__(self):
        return self._url
    def __call__(self,url):
        '''
        __call__()方法，直接对实例进行调用。
        :param url:
        :return:
        '''
        return chain("%s=%s" % (self._url, url))

print chain().status11('2').timeline111
#chain().status.user.timeline 执行过程
#首先在chain()中找不到timeline这个方法，执行__getattr__(chain()，status)
#然后在__getattr__(/status,user.timeline)