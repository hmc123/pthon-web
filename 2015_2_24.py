#!usr/bin/env python
# -*- coding: utf-8 -*-

__anthor__='HMC'

'this is a test about creating file and reading file'

import os
ls = os.linesep

fname = raw_input('please input path: ')

while True:
	if os.path.exists(fname):
		print("Error: '%s' already exists" % fname)
	else:
		break


all = []
print("\nEnter lines '.' by itself to quit\n")


while True:
	entry = raw_input('>>>>>>')
	if entry =='.':
		break
	else:
		all.append(entry)


fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()

print('Done!!!')
