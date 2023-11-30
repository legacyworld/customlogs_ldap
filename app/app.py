#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
import ldap
import logging                                                                  

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view =  "login"
login_manager.init_app(app)

app.config['SECRET_KEY'] = "secret"
app.config['LDAP_URL'] = 'ldap://ldap:389'
app.config['LDAP_DN_FORMAT'] = 'uid=%s,ou=people,dc=example,dc=com'

l = logging.getLogger()
l.addHandler(logging.FileHandler("/log/flask.log"))

class User(object):
    def __init__(self, username, data=None):
        self.username = username
        self.data = data
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.username

    @classmethod
    def auth(cls, username, password):
        l = ldap.initialize(app.config['LDAP_URL'])
        dn = app.config['LDAP_DN_FORMAT'] % (username)
        try:
            print(dn,password)
            l.simple_bind_s(dn, password)
        except:
            return None
        return User(username)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])

    def __str__(self):
        return '''
<form action="/login" method="POST">
<p>%s: %s</p>
<p>%s: %s</p>
%s
<p><input type="submit" name="submit" /></p>
</form>
''' % (self.username.label, self.username,
       self.password.label, self.password,
       self.csrf_token)


@login_manager.user_loader
def load_user(username):
    return User(username)

@app.route('/')
@login_required
def index():
    return u'Hello! %s.' % (current_user.username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    #form = LoginForm()
    if form.validate_on_submit():
        user = User.auth(form.username.data, form.password.data)
        if user:
            login_user(user)
            print('Login successfully.')
            return redirect(request.args.get('next', '/'))
        else:
            print('Login failed.')
    return str(form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect('/login')

if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)
