#!/usr/bin/env python3
#注意，文件名不能命名为socket.py
import socket
#创建一个socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立链接
s.connect(('www.sina.com.cn',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据

buffer=[]
while True:
	#每次最多接收1k字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
#关闭socket
s.close()

header,html = data.split(b'\r\n\r\n',1)

print(header.decode('utf-8'))
#with将自动调用f.colse()方法
with open('sina.html','wb') as f:
	f.write(html)
