from flask import Flask, request, redirect, render_template_string
import re

app = Flask(_name_)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def index():

    title = 'Signup'
    username = ''
    username_error =''
    password = ''
    password_error = ''
    varify_password_error = ''
    email = '(optional)'
    email_error = ''


@app.route('/usercheck')
def usercheck():
    title = "Welcome"
    username = request.args.get('username')
    return render_template('usercheck.html', title = title, username = username)
    



if _name_ == '_main_':
    app.run()
