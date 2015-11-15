# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return '<h1>Hello World!</h1>'
if __name__ == '__main__':
	app.run()
#def index():
#	return 'Index Page'
#@app.route('/hello')
#def hello():
#	return 'Hello World'
