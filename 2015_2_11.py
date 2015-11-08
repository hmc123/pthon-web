#!usr/bin/env python
# -*- coding: utf-8 -*-


__anthor__ = 'HMC'

import os


def search(s):

	for x in os.listdir('.'): 
		if os.path.isfile(x) and x.find(s) != -1:
			print os.path.abspath(x)

	for x in os.listdir('.'): 
		if os.path.isdir(x):
			for y in os.listdir(y): 
				if os.path.isfile(y) and y.find(s) != -1:
					print os.path.abspath(y)
	

