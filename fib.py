#!/usr/bin/env python3

__author__ = 'luoshun'

class Fib(object):
	def __init__(self):
		self.a = 0
		self.b = 1
	#获取自己属性
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a > 10000:
			raise StopIteration()
		return self.a
	#获取属性
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			#对应Fib[:10]
			if start is None:
				start = 0
			a,b=1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b=b,a+b

			return L


f = Fib()
print(f[:10])
