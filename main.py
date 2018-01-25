from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def index():

    title = 'Signup'
    username = ''
    username_error =''
    password = ''
    password_error = ''
    verify_password_error = ''
    email = '(optional)'
    email_error = ''
    title = 'Signup'

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']


        for i in username:
            if i.isspace():
                username_error = 'Username need to be 3-20 characters.'
                username = ''

            else:
                if(len(username) <3) or (len(username) > 20):
                    username_error = 'User name should be between 3-20 characters'
                    username = ''
                
        if not username:
            username_error = 'Not a valid username'
            username = ''

        for i in password:
            if i.isspace():
                password_error = 'Password cannot contain spaces.'
            else:
                if (len(password) <3) or (len(password) >20):
                    password_error = 'Password need to be beetween 3-20 characters and contain no spaces.'
        if not len(password):
            password_error = 'Not a valid password'

        if password != verify_password:
            verify_password_error = 'Passwords do not match.'

        if(email !='') and (not re.match('^[a-zA-Z0-9_.+-] +@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$', email)):
            email_error = 'This is not a valid e-mail'
            email=''
            
        

        if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
            return redirect('/confirmation?username={0}'.format(username))

    return render_template('new_user_signup.html', 
                title=title, username=username, 
                email=email, username_error=username_error, 
                password_error=password_error,
                verify_password_error=verify_password_error,
                email_error=email_error)

@app.route('/usercheck')
def usercheck():
    title = "Welcome"
    username = request.args.get('username')
    return render_template('usercheck.html', title = title, username = username)
    



if __name__ == '__main__':
    app.run()
