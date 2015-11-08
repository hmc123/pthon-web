#regularexpression1.py

#! usr\bin\env python
# -*- coding: utf-8 -*-

__anthor__='HMC'

'This is a test about regular expression'

import re
mail=raw_input('please input your E-mail address: ')
m = re.match(r'^\<([a-zA-Z]+[a-zA-Z\s]+[a-zA-Z])\>\s+([0-9a-zA-Z]+\@[0-9a-z]+\.[a-z]+)$',mail)
if m != None:
	print('it\'s ok')
	print('your name is : %s' % m.group(1))
	print('your E-mail address is: %s' % m.group(2))

else:
	print('error')