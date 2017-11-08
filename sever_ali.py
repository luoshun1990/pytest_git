#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#注意，connect只接收一个参数
s.connect(('127.0.0.1',9999))

#接收欢迎消息

print(s.recv(1024).decode('utf-8'))

for data in [b'Michael',b'Tracy',b'Sarah']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

