#server.py
#!usr\bin\env python
# -*- coding: gb18030 -*-


__anthor__ = 'HMC'
'this is test about web server gateway interface'

from hello import application
from wsgiref.simple_server import make_server

myhttp = make_server('', 8001, application)
print 'Serving myhttp on port 8001'

myhttp.serve_forever()
