#regularexpression.py

#! usr\bin\env python
# -*- coding: utf-8 -*-

__anthor__='HMC'

'This is a test about regular expression'

import re
mail=raw_input('please input your E-mail address: ')
m = re.match(r'^[0-9a-zA-Z]+\.?[0-9a-zA-Z]+\@[0-9a-z]+\.[a-z]+$',mail)
if m != None:
	print('it\'s ok')
	print m.group(0)

else:
	print('error')