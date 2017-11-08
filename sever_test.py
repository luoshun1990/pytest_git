#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time,threading
#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ADDR = ('127.0.0.1',9999)
#监听端口
s.bind(ADDR)
#5表示等待链接的最大数量为5
s.listen(5)

print('waiting for connection...')

def tcplink(sock,addr):
	print('Accept new connection from %s:%s'% addr)
	sock.send(b'Welcome')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		#如果客户端发送了'exit'字符串，直接关闭
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s!'% data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connection from %s:%s closed'% addr)

while True:
	#接受一个新链接
	sock,addr=s.accept()
	#创建一个线程来处理tcp链接
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()




