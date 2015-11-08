#!usr/bin/env python
# -*- coding: utf-8 -*-

'a test class'
__author__ = 'HMC'


class test2(object):
	def __init__(self,name, score):
		self.__name=name
		self.__score=score

	def print_score(self):
        print 'your name and score is:%s,%d' % (self.__name,self.__score)


class animal(object):
	def run(self):
		print 'animal is running'


 