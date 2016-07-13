#-*- coding=utf-8 -*-
'''
实现带优先级的队列，并且在这个队列上面每次pop操作总是返回优先级最高的那个元素

'''

import  heapq
class priorityqueue:
    def __init__(self):
        self._queue=[]
        self._index=0


    def push(self,item,prioity):
        heapq.heappush(self._queue,(-prioity,self._index,item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q=priorityqueue()
q.push(item('foo'), 1)
q.push(item('bar'), 5)
q.push(item('spam'), 4)
q.push(item('grok'), 1)
m=q.pop()
print m
