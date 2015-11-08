# Process_pool.py
#! usr\bin\env python
# -*- coding: utf-8 -*-

__anthor__='HMC'

'This is a multiprocessing test'

from multiprocessing import Pool
import os, time, random

def pool_time(name):
	print('Run task %s (%s)' % (name,os.getpid()))
	start=time.time()
	time.sleep(random.random() * 3)
	end=time.time()
	print('\nTask %s runs %f seconds.' % (name,end - start))


if __name__=='__main__':
	print('Parent process %s will produce subprocess' % os.getpid())
	p=Pool(5)
	for i in range(5):
		p.apply_async(pool_time,args=(i,))
	print('Waiting for all subprocess done')
	p.close()
	p.join()
	print('All subprocess done.')
