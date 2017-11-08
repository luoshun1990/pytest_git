#!/usr/bin/env python3

from functools import reduce
def is_odd(n):
	return n%2==1
L = list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))

print(L)
#利用filter滤掉非回数
#标准答案: def is_palindrome(n)
#		return str(n)==str(n)[::-1]
def is_paiindrome(n):
	def l2int(ch1,ch2):
		return int(ch1)*10+int(ch2)
	s1 =list( str(n))
#	print(s1)
	s1.reverse()
#	print(s1)
	n2=reduce(l2int,s1)
	return n==n2

print(list(filter(is_paiindrome,range(1,1000))))
