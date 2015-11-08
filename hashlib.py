#hashlib.py
#!usr\bin\env python
# -*- coding: utf-8 -*-

__anthor__ = 'HMC'

'This is a test about hashlib, test environment is Python 3.4'

import hashlib

def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password)
	return md5.hexdigest()

db = {}

def login(username,password):
	kk = calc_md5(password + username + 'The_salt_hmc')
	count=0  # 'query count'
	for i in db:
		if i == username:
			if kk == db[username]:
				print('Success!!!\n\n')
			else:
				print('your password is wrong\n\n')
			break
		else:
			count = count + 1

	if count == len(db):
		print ('your user name is inexistence\n\n')
	

def register(username,password):
	db[username]=calc_md5(password + username + 'The_salt_hmc')


if __name__ == '__main__':
	
	while True:
		print ('please shoose login or regirster? L/R: ')
		pp = raw_input()
		if pp == 'R' or pp == 'r':
			register(raw_input('please input your username: '),raw_input('please input your password: '))
		elif pp == 'L' or pp == 'l':	
			login(raw_input('please input your username: '),raw_input('please input your password: '))
			
		else:
			break
