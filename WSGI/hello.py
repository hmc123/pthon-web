# -*- coding: cp936 -*-
#hello.py

def application(environ,start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    #return '<h1>Hello, %s</h1>' % (x['PATH_INFO'][1:] or 'Web')
    return '''<h1>Hello, Welcome to HMC Zone</h1>'''
            
