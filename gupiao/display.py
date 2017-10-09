#!/usr/bin/env python
# -*- coding:utf-8 -*-

#flask演示demo
from flask import Flask,request,url_for


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>hello World!</h1>'

@app.route("/user",methods=['POST'])
def hello_user():    
    return 'hello  user'

@app.route("/user/<id>")
def user_id(id):
    return 'user:' +id
#访问模板http://127.0.0.1:5000/user/1234

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query_user' +id
#访问模板：http://127.0.0.1:5000/query_user?id=12345

@app.route('/query_url')
def query_url():
    return 'query url:' + url_for('query_user')
#反向路由  比较常用  访问模板 http://127.0.0.1:5000/query_url

if __name__ == '__main__':
    app.run()