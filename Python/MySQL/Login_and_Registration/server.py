#DEPENDENCIES
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

# APP, DB, CONSTANTS
app = Flask(__name__)
mysql = MySQLConnector(app,'login_and_registration')
app.secret_key = "SuperSecretKey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
bcrypt = Bcrypt(app)

# SQL QUERIES - JUST FOR REFERENCE
    # query = queries['create']
queries = {
    'create': "",  # "INSERT INTO table (column, created_at, updated_at) VALUES (:key, NOW(), NOW())",
    'read': "",    # "SELECT * FROM table",
    'update': "",  # "UPDATE table SET column = :key WHERE column = :key",
    'delete': ""   # "DELETE FROM table WHERE column = :key"
}

# VALIDATORS
def validateEmail(email):
    # Return whether or not the email passed in is valid
    return EMAIL_REGEX.match(email)
# if(validateEmail(request.form['email'])):
    # query = queries['create']
    # data = {'email': request.form['email']}
    # mysql.query_db(query, data)
    # flash('Successfully created email record!')
    # return redirect('/success')
# else:
    # flash('Invalid email!')

# CLEAR SESSION FOR TESTING
@app.route('/clear')
def clear():
    session.clear()
    return redirect ('/')

# @app.route('/') GET
# index()
#     Display login and registration forms on the index.html page
@app.route('/')
def index():
    if 'registration' not in session:
        session['registration'] = {}
    query = "SELECT * FROM users"                           # define your query
    users = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_users=users) # pass data to our template

# @app.route('/register') POST
# create()
#     Handle the register form submit and create the user in the DB
@app.route('/register', methods=['POST'])
def create():
    session['registration'] = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    errors = []
    if len(request.form['first_name']) < 1:
        errors.append(flash('First name cannot be blank!'))
    elif len(request.form['first_name']) < 2:
        errors.append(flash('First name should be 2 or more characters!'))
    elif not request.form['first_name'].isalpha():
        errors.append(flash('First name should only have letters!'))
    if len(request.form['last_name']) < 1:
        errors.append(flash('Last name cannot be blank!'))
    elif len(request.form['last_name']) < 2:
        errors.append(flash('Last name should be 2 or more characters!'))
    elif not request.form['last_name'].isalpha():
        errors.append(flash('Last name should only have letters!'))
    if not validateEmail(request.form['email']):
        errors.append(flash('Invalid email!'))
    if len(request.form['password']) < 8:
        errors.append(flash('Password must be at least 8 characters!'))
    elif request.form['password'] != request.form['password_confirmation']:
        errors.append(flash("Passwords didn't match!"))
    if errors:
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "pw_hash": pw_hash
        }
        new_user_id = mysql.query_db(query, data)
        print "new_user_id:", new_user_id
        errors.append(flash("REGISTRATION SUCCESSFUL!"))
        return redirect('/success')

# @app.route('/login') POST
# login()
#     Handle the login form submit and login the user
@app.route('/login', methods=['POST'])
def login():
    errors = []
    session['registration'] = {
        'login_email':request.form['email']
    }
    if not validateEmail(request.form['email']):
        errors.append(flash("Invalid email!"))
    else:
        if len(request.form['password']) < 8:
            errors.append(flash("Password must be at least 8 characters!"))
    if errors:
        return redirect('/')
    else:
        try:
            email_match = False
            query = "SELECT * FROM users WHERE email = :email"
            data = {
                "email": request.form['email']
            }
            user = mysql.query_db(query, data)
            pw_hash = user[0]['pw_hash']
            # exception if user is empty, which means incorrect email
            email_match = True
            password = request.form['password']
            print "<<<testing password against hash>>>"
            pw_match = bcrypt.check_password_hash(pw_hash, password)
            # pw_match True or False?
        except:
            if email_match == False:
                errors.append(flash('Invalid email!'))
                return redirect('/')
            pw_match = False
        if pw_match:
            session['id'] = user[0]['id']
            print "user[0]['id'] saving to session['id']:", session['id']
            errors.append(flash('LOGIN SUCCESSFUL!'))
            return redirect('/success')
        else:
            errors.append(flash('Invalid password!'))
        return redirect('/')

# @app.route('/success') GET
# success()
#     Display the success.html page after a successful login/registration
@app.route('/success')
def success():
    return render_template('success.html')

# @app.route('/users/<id>/edit') GET
# edit(id)
#     Display the edit.html page for the particular user
@app.route('/users/<user_id>/edit')
def edit(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    user = mysql.query_db(query)
    return render_template('edit.html', user=user[0])

# @app.route('/users/<id>') POST
# update(id)
#     Handle the edit user form submit and update the user in the DB
@app.route('/users/<user_id>', methods=['POST'])
def update(user_id):
    errors = []
    if len(request.form['first_name']) < 1:
        errors.append(flash('First name cannot be blank!'))
    elif len(request.form['first_name']) < 2:
        errors.append(flash('First name should be 2 or more characters!'))
    elif not request.form['first_name'].isalpha():
        errors.append(flash('First name should only have letters!'))
    if len(request.form['last_name']) < 1:
        errors.append(flash('Last name cannot be blank!'))
    elif len(request.form['last_name']) < 2:
        errors.append(flash('Last name should be 2 or more characters!'))
    elif not request.form['last_name'].isalpha():
        errors.append(flash('Last name should only have letters!'))
    if not validateEmail(request.form['email']):
        errors.append(flash('Invalid email!'))
    if errors:
        query = "SELECT * FROM users WHERE id = " + user_id
        user = mysql.query_db(query)
        return render_template('edit.html', user=user[0])
    else:
        query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :user_id"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "user_id": user_id
        }
        mysql.query_db(query, data)
        return redirect('/')

# @app.route('/users/<id>/delete') POST
# delete(id)
#     Delete the user from the DB
@app.route('/users/<user_id>/delete', methods=['POST'])
def delete(user_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {
        "id": user_id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)

# Assignment: Login and Registration
# We've learned about how we can connect to the database, insert records posted from a form, retrieve records from a database and set a session/flash for any error or success messages that we get along the way. One of the major components to every website is a login and registration.
#
# Registration
# The user inputs their information, we verify that the information is correct, insert it into the database and return back with a success message. If the information is not valid, redirect to the registration page and show the following requirements:
#
# Validations and Fields to Include
#
# First Name - letters only, at least 2 characters and that it was submitted
# Last Name - letters only, at least 2 characters and that it was submitted
# Email - Valid Email format, and that it was submitted
# Password - at least 8 characters, and that it was submitted
# Password Confirmation - matches password
# Login
# When the user initially registers we would log them in automatically, but the process of "logging in" is simply just verifying that the email and password the user is providing matches up with one of the records that we have in our database table for users.
#
# But how do we keep track of them once they've logged in? I think you might already know... It's using session! We can create a session variable that holds the user's id. From our study in Database Design, we know that if we have the id of any table we can gather the rest of the information that is associated with that id. Storing a single session variable with the user's id is all we need to access all the information associated with that user.
#
# Once we have already identified the places on our site that we wish to be dynamic for users that are logged in, then we just need to check to see if that session variable has been set and display the content accordingly.
