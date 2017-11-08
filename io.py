#!/usr/bin/env python3
with open('./test.txt','w') as f:
		f.write('hello,luoshun')

with open('./test.txt','r') as f:
		for line in f.readlines():
			print(line.strip())

#with open('./test.jpg','rb') as f1:
#	print(f1.read())

