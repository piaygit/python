#coding=utf-8
import socket,threading,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print "创建udp连接于端口：9999"
while True:
    data,addr=s.recvfrom(1024)
    #recvfrom()方法返回数据和客户端的地址与端口
    print '连接来自 %s:%s' % addr
    s.sendto('hello,%s' % data, addr)

