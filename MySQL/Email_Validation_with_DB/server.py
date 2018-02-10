from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "SuperSecretKey"
mysql = MySQLConnector(app,'Email_Validation_with_DB')

@app.route('/')
def index():
    # session.clear()
    if 'email_valid' in session:
        if session['email_valid'] == True:
            session.pop('email_valid')
    else:
        print 'session email_valid:'
    query = "SELECT email, DATE_FORMAT(created_at, '%m/%d/%y') AS date, TIME_FORMAT(created_at, '%l:%i%p') AS time FROM users"                           # define your query
    email = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_email=email) # pass data to our template

@app.route('/email', methods=['POST'])
def create():
    session['email_valid'] = True
    if len(request.form['email_address']) < 1:
        session['email_valid'] = False
        flash("Email cannot be blank!")
        session['style'] = "background-color: red"
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email_address']):
        session['email_valid'] = False
        flash("Invalid email address!")
        session['style'] = "background-color: red"
        return redirect('/')
    else:
        session['inputted_email'] = request.form['email_address']
        session['style'] = "background-color: green"
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
                 'email': request.form['email_address']
               }
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    if 'email_valid' in session:
        if session['email_valid'] == False:
            print "False"
        else:
            print "True"
    query = "SELECT email, DATE_FORMAT(created_at, '%m/%d/%y') AS date, TIME_FORMAT(created_at, '%l:%i%p') AS time FROM users"                           # define your query
    email = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_email=email) # pass data to our template

app.run(debug=True)

# Assignment: Email Validation with DB
# Create an application that asks a user to enter an email address.
# If the email address is not valid, have a notification "Email is not valid!" to display on the homepage.
# Once a valid email address is entered, save to the database the email address the user entered.
# On the success page, display all the email addresses entered along with the date and the time (e.g. June 24th, 2013, 6:00 PM) when the email addresses were entered
