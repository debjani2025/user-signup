from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def def_display_signup():
    return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def validate_input():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == '':
        username_error = "Do not leave the field empty"

    if password == '':
        password_error = "Do not leave the field empty"

    if verify_password == '':
        verify_password_error = "Do not leave the field empty"        

    for char in (username):
        if char ==' ':
            username_error = "No space allowed"
        else:
            if len(username)<3 or len(username)>20:
                username_error = "Must be between 3 and 20 characters"

    for char in password:
        if char == ' ':
            password_error = "No space allowed"
        else:
            if len(password)<3 or len(password)>20:
                password_error = "Must be between 3 and 20 characters"

    if password != verify_password:
        verify_password_error = "Passwords don't match"

    if email !='':
        if "@" and "." not in email:
            email_error = "Email not valid"
        
    if not username_error and not password_error and not verify_password_error and not email_error:
        username=request.form['username']      
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error,
        email_error=email_error, username=username, email=email)    


app.run()