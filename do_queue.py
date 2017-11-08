#!/usr/bin/env python3

from multiprocessing import Process,Queue

import os,time,random,time

#写数据进程执行代码

def write(q):
	print('Processing to write:%s'% os.getpid())
	while True:
		for value in ['A','B','C']:
			print('Put %s to queue...'%value)
			q.put(value)
			time.sleep(random.random())

#读数据执行代码
def read(q):
	print('Processing to read:%s'%os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.'%value)

if __name__=='__main__':
	q=Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	#启动子进程
	pw.start()
	#启动子进程，读取
	pr.start()
	#等待结束
	pw.join()

	pr.terminate()



