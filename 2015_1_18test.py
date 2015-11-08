#!usr/bin/env python
#-*- coding: utf-8 -*-

'2015/1/18 test class'
__anthor__='HMC'

class hmc1(object):
	"""docstring for hmc1"""
	def __init__(self, arg):
		super(hmc1, self).__init__()
		self.arg = arg

	def get():
		print 'hmc1 is drived'

class hmc2(object):
	"""docstring for hmc2"""
	def __init__(self, arg):
		super(hmc2, self).__init__()
		self.arg = arg

	def set():
		print 'hmc2 is drived'
		

class hmc3(hmc1,hmc2mixin):
	"""docstring for hmc3"""
	def __init__(self, arg):
		super(hmc3, self).__init__()
		self.arg = arg
		