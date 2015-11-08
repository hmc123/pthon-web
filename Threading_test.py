#Threading_test.py
#! usr\bin\env python
# -*- coding: utf-8 -*-

__anthor__='HMC'

'This is a threading test'



import time, threading

def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n=0
	while n<5:
		n=n+1
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
p=threading.Thread(target=loop,name='LoopThread')
p.start()
p.join()
print('thread %s ended.' % threading.current_thread().name)