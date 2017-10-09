#!/usr/bin/env python
# -*- coding:utf-8 -*-

#测试模板页面

from flask import Flask,render_template
from model import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
#练习调用模板

@app.route('/user')
def hello_user():
    user = User('1','jikexueyuan')
    return render_template("user_index.html",user=user)
#练习模板中传入参数

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User('1','jikexueyuan')
    return render_template("query_user.html",user=user)
#练习模板判断        
    
@app.route('/users')
def user_list():
    users = []
    for i in range(1,11):
        user = User(i, 'jikexueyuan'+str(i))
        users.append(user)
    return render_template('user_list.html',users = users)
#循环练习

@app.route('/one')
def one_base():
    return render_template('one_base.html')   

@app.route('/two')
def two_base():
    return render_template('two_base2.html')       
#模板继承  将定义后的html模板使用在其他页面中

if __name__ =='__main__':
    app.run()