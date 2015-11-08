#Threadlocal.py

#! usr\bin\env python
# -*- coding: utf-8 -*-

__anthor__='HMC'

'This is a test about Threadlocal'

import threading

local_school=threading.local()

def process_student():
	print('hello, %s (in %s)' % (local_school.student, threading.current_thread().name))

def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target = process_thread, args = ['HHH'], name='Thread-A')
t2 = threading.Thread(target = process_thread, args = ['KKK'], name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
