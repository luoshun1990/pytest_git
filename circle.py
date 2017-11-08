#!/usr/bin/env python3
print("test for function")
names=['a','b','c']

for name in names:
	print(name)

print('test while function')
n = 99
sum = 0
while n>0:
	sum=sum+n
	n=n-2

print(sum)

print('small test')

L = ['Bart','Lisa','Adam']

for l_name in L:
	print('hello, '+l_name)
print('test break:')
n=1
sum=0
while n<=100:
	n=n+1
	if n%2==0:
	   continue
	if n>10:
	  break
	print(n)

