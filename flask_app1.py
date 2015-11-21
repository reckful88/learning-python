#-*- coding: utf-8 -*-


from flask import request
  
@app.reoute("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return 'your browser is {0} .format(user_agent)'

