from flask import Flask
from flask import Response

flask_app=Flask('flaskapp')

def hello_world():
    return Response(
            'Hello world from Flask!\n',
            mimetype='text/plain'
            )

app=flask_app.wsgi_app


