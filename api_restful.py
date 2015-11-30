# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    { 'id' : 1,
     'title' : 'Buy Bug Bug!!!',
     'description' : 'Apple, Pear',
     'done' : False
    },

    {'id' : 2,
     'title' : 'Learn Python',
     'description' : 'on the web',
     'done' : False
    }]

@app.route('/v1.0/meeting/342/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks' : tasks})
if __name__ == '__main__':
    app.run(debug = True)
