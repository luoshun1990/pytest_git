#!/usr/bin/env python3

from multiprocessing import Pool

import os,time,random

def long_time_task(name):
	print('run task %s (%s)...'%(name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('task %s runs %0.2f seconds.'%(name,(end-start)))

if __name__ == '__main__':
	print('Parent process %s.'% os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('wait al subprocss done...')
	p.close()
	#等待所有进程执行完毕
	p.join()
	print('All subprocess done.')
