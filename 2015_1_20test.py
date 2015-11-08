#!usr/bin/env python
# -*- coding: utf-8 -*-


__anthor__='HMC'

import random
secret=random.randint(1,10)
print('------------------------------------------')
temp=input('请输入一个我想要的数字：')
while temp!=secret:
	temp=input('请输入一个我想要的数字：')
	if temp==secret:
		print('你真聪明，一下就知道我想要什么——————恭喜发财啊！！！')
	else:
		print('No 我跟我真的很不搭诶！！！')
print('OK,我不跟你们玩了')