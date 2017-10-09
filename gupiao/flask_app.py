#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,flash,render_template,request,abort
from model import User

app = Flask(__name__)
app.secret_key = '123'

@app.route("/")
def hello_world():
    flash("hello jikexueyuan")
    return render_template("login.html")

@app.route('/login',methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    
    if not username:
        flash("Please input username!")
        return render_template('login.html')
    if not password:
        flash("Please input password!")
        return render_template('login.html')
    
    if username == 'zhangyage' and password == '123456':
        flash("login success!")
        return render_template('login.html')
    else:
        flash("username and password is worng!")
        return render_template('login.html')
    
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/query_user/<user_id>')
def query_user(user_id):
    if int(user_id) == 1:
        user = User('1','jikexueyuan')
        return render_template("query_user.html",user=user)
    else:
        abort(404)    #主动抛出404异常
    
    
    
if __name__ =='__main__':
    app.run()