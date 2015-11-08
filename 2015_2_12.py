#!usr/bin/env python
# -*- coding: utf-8 -*-

__anthor__='HMC'

import os
from multiprocessing import Process

# subprocess will process 
def subprocess(name):
	print 'Run childprocess %s:%s...' % (name,os.getpid())


# mainprocess process

if __name__=='__main__':
	print 'Parent process is %s' % os.getpid()
	p = Process(name = subprocess, args = ('hmctest',))
	print 'Process will start...'
	p.start()
	p.join()
	print  'Process end'