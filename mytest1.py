#test1.py
#!usr\bin\env python
# -*- coding: utf-8 -*-

__anthor__='HMC'
'using this model to evaluate score'

import os
N = int(input('please input how many row will be display: '))
F = input('please input path of file: ')
fp = open(F,'r+')
count = len(fp.readlines())
if N>count:
	N = count
a = ''
fp.seek(0)
while N>0:
	a += fp.readline()
	N = N-1

print(a)