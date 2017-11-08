#!/usr/bin/env python3

from functools import reduce

#空函数
def nop():
	pass


def str2float(s):
	def fn(x,y):
		return x*10+y
	n = s.index('.')
	s1 = list(map(int,s[:n]))
	s2 = list(map(int,s[n+1:]))
	return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)

print('\'123.456\'=',str2float('123.456'))
