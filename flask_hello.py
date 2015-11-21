# -*- coding: utf-8 -*-
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#	return '<h1>Hello World!</h1>'
#if __name__ == '__main__':
#	app.run()
#def index():
#	return 'Index Page'
#@app.route('/hello')
#def hello():
#	return 'Hello World'
#
#
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)



