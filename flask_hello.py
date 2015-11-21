# -*- coding: utf-8 -*-

'''
elinks --dump http://ip:5000 
        &
elinks --dump http://ip:5000/user/xxxxxx

/user/ 后面输入什么 页面就显示什么
'''

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



#方法二
#from flask import request

#@app.reoute("/")
#def index():
#    user_agent = request.headers.get("User-Agent")
#    return 'your browser is {0} .format(user_agent)

