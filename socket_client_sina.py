#Socket_client.py
#!usr\bin\env python
# -*- coding: gb18030 -*-
__anthor__ = 'HMC'

'this is test about Socket'

#import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #create socket
s.connect(('www.sina.com.cn', 80))				#create connection

#send data
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#receive data
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)

# close connect
s.close()



header, html = data.split('\r\n\r\n', 1)
print header
# 
with open(r'c:\users\administrator\desktop\sina.html', 'wb') as f:
	f.write(html)

