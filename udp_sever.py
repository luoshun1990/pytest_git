#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))

#UDP不需要listen

print('bind udp to 9999')

while True:
	#接收数据
	data,addr = s.recvfrom(1024)
	print('Receved from %s:%s'%addr)
	s.sendto(b'hello,%s'%data,addr)

s.colse()
