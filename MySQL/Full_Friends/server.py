#DEPENDENCIES
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

# APP, DB, CONSTANTS
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
app.secret_key = "SuperSecretKey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

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
    # flash('Not a valid email!')

# TO-DO:
# @app.route('/') GET
# index()
#     Display all of the friends on the index.html page
# @app.route('/friends') POST
# create()
#     Handle the add friend form submit and create the friend in the DB
# @app.route('/friends/<id>/edit') GET
# edit(id)
#     Display the edit.html page for the particular friend
# @app.route('/friends/<id>') POST
# update(id)
#     Handle the edit friend form submit and update the friend in the DB
# @app.route('/friends/<id>/delete') POST
# destroy(id)
#     Delete the friend from the DB

# CLEAR SESSION FOR TESTING
@app.route('/clear')
def clear():
    session.clear()
    return redirect ('/')

# @app.route('/') GET
# index()
#     Display all of the friends on the index.html page
@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

# @app.route('/friends') POST
# create()
#     Handle the add friend form submit and create the friend in the DB
@app.route('/friends', methods=['POST'])
def create():
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
        errors.append(flash('Not a valid email!'))
    if errors:
        return redirect('/')
    else:
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/')

# @app.route('/friends/<id>/edit') GET
# edit(id)
#     Display the edit.html page for the particular friend
@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    query = "SELECT * FROM friends WHERE id = " + friend_id
    user = mysql.query_db(query)
    return render_template('edit.html', user=user[0])

# @app.route('/friends/<id>') POST
# update(id)
#     Handle the edit friend form submit and update the friend in the DB
@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
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
        errors.append(flash('Not a valid email!'))
    if errors:
        query = "SELECT * FROM friends WHERE id = " + friend_id
        user = mysql.query_db(query)
        return render_template('edit.html', user=user[0])
    else:
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :friend_id"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "friend_id": friend_id
        }
        mysql.query_db(query, data)
        return redirect('/')

# @app.route('/friends/<id>/delete') POST
# destroy(id)
#     Delete the friend from the DB
@app.route('/friends/<friend_id>/delete', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        "id": friend_id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)

# Assignment: Full Friends
# Create an application that will perform all the CRUD operations on the friends resource:
#
# In Index.html, each friend should have an "edit" button that will take the user to the '/friends/<id>/edit' URL which should display the edit page for that particular user
# The edit page form should send a POST request to '/friends/<id>' which will actually update the user in the database with the new inputs
# In Index.html, each friend should have a "delete" button (part of a form) that should POST to '/friends/<id>/delete'
# This route should delete the user from the database
# At this point, you should have 2 pages and 5 routes which should be handled by the routes and methods below
#
# Method	URL	Route Handler Function	Purpose
# GET	'/'	index()	Display all of the friends on the index.html page
# POST	'/friends'	create()	Handle the add friend form submit and create the friend in the DB
# GET	'/friends/<id>/edit'	edit(id)	Display the edit friend page for the particular friend
# POST
# '/friends/<id>'	update(id)	Handle the edit friend form submit and update the friend in the DB
# POST	'/friends/<id>/delete'	destroy(id)	Delete the friend from the DB
# Make sure that your application uses the structure above. A Friend should have First Name, Last Name, Email, and a time stamp when the friend was created.
