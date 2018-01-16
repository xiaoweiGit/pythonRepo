from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>hello,web!</h>']

httpd=make_server('',8888,application)
print('Serveing HTTP on port 8000...')

httpd.serve_forever()
