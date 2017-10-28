#DEPENDENCIES
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

# APP, DB, CONSTANTS
app = Flask(__name__)
mysql = MySQLConnector(app,'the_wall')
app.secret_key = "SuperSecretKey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
bcrypt = Bcrypt(app)

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

# SQL QUERIES - FOR REFERENCE
    # 'create': "INSERT INTO table (column, created_at, updated_at) VALUES (:key, NOW(), NOW())"
    # 'read': "SELECT * FROM table"
    # 'update': "UPDATE table SET column = :key WHERE column = :key"
    # 'delete': "DELETE FROM table WHERE column = :key"
    
# CLEAR SESSION
@app.route('/logoff')
def clear():
    session.clear()
    return redirect ('/')

@app.route('/')
def index():
    if 'registration' not in session:
        session['registration'] = {}
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

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
        session['id'] = new_user_id # remember that "INSERT" returns the id
        print "user['id'] saving to session['id']:", session['id']
        # errors.append(flash("Registration successful! Welcome {}!".format(request.form['first_name']), category='flash_success'))
        session['user_first_name'] = request.form['first_name']
        return redirect('/wall')

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
            # errors.append(flash("Login successful! Welcome {}!".format(user[0]['first_name']), category='flash_success'))
            session['user_first_name'] = user[0]['first_name']
            return redirect('/wall')
        else:
            errors.append(flash('Invalid password!'))
        return redirect('/')

@app.route('/wall')
def success():
    messages_query = "SELECT messages.id, messages.user_id, messages.message, DATE_FORMAT(messages.created_at, '%M %D %Y') AS message_created_at, users.first_name, users.last_name FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"

    comments_query = "SELECT comments.message_id, comments.comment, DATE_FORMAT(comments.created_at, '%M %D %Y') AS comment_created_at, users.first_name, users.last_name FROM comments JOIN messages ON messages.id = comments.message_id JOIN users ON comments.user_id = users.id ORDER BY comments.created_at"

    messages = mysql.query_db(messages_query)
    comments = mysql.query_db(comments_query)
    return render_template('success.html', messages=messages, comments=comments)

@app.route('/users/<user_id>/edit')
def edit(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    user = mysql.query_db(query)
    return render_template('edit.html', user=user[0])

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

@app.route('/users/<user_id>/delete', methods=['POST'])
def delete(user_id):
    # Deleted comments and messages before users due to foreign key references
    query = "DELETE FROM comments WHERE comments.user_id = :id; DELETE FROM messages WHERE messages.user_id = :id; DELETE FROM users WHERE users.id = :id;"
    data = {
        'id': user_id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/wall/message', methods=['POST'])
def post_message():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:id, :message, NOW(), NOW());"
    data = {
        'id': int(session['id']),
        'message': request.form['message']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall/<message_id>/comment', methods=['POST'])
def post_comment(message_id):
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:id, :message_id, :comment, NOW(), NOW());"
    data = {
        'id': int(session['id']),
        'message_id': message_id,
        'comment': request.form['comment']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

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
