#coding=utf-8
import socket,threading,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1',9999))
s.listen(5)
print "waiting ..."
def tcplink(sock,addr):
    print "accept new connection from %s:%s" % addr
    sock.send('welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send("hello,%s"%data)
    sock.close()
while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

print "connection from %s:%s closed"% addr

