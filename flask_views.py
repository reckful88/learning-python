#encoding:utf-8

'''
在此文件的当前目录下，创建一个template文件夹，里面创建一个index文件
'''

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')

#示例一：if
#def index():
#    user ={ 'nickname': 'Lxf', 'score':88 }
#    return render_template("index.html",
#            title='Engilsh',
#            user=user)


def index():        #示例二：for
    users = [{'nickname':'lxf','score':88},{'nickname':'dc','score':99}]
    return render_template("index.html", title='English', users=users)
if __name__ == '__main__':
    app.run(debug = True)
