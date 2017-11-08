#!/usr/bin/env python3

'test class'

__author__ = 'luoshun'

class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s %s'%(self.__name,self.__score))

	def get_grade(self):
		if self.__score>=90:
			return 'A'
		elif self.__score>=60:
			return 'B'
		else :
			return 'C'

bart=Student('luo',75)
bart.print_score()
print(bart.get_grade())
