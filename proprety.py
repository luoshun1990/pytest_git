#!/usr/bin/env python3

__author__ = 'luoshun'

class Student(object):
#可读属性
	@property
	def score(self):
		return self.__score
#可写属性
	@score.setter
	def score(self,value):
		self.__score = value
#可读属性
	@property
	def age(self):
		return 2015-self.__score

s = Student()
print('input your score')
s1=input()
s.score = int(s1)
print(s.age)
