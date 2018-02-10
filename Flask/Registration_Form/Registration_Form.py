from flask import Flask, render_template, request, session, redirect, flash
import re
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[0-9])')

@app.route('/')
def index():
    if 'info' in session.keys():
        email = session['info']['email']
        first_name = session['info']['first_name']
        last_name = session['info']['last_name']
        # password = session['info']['password']
        return render_template('index.html', email=email, first_name=first_name, last_name=last_name)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print "/process"
    valid = True
    if len(request.form['email']) < 1:
        valid = False
        flash("Email cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        valid = False
        flash('Email is not valid')
    if len(request.form['first_name']) < 1:
        valid = False
        flash("First name cannot be empty!")
    elif not request.form['first_name'].isalpha():
        valid = False
        flash('First name cannot contain numbers or special characters')
    if len(request.form['last_name']) < 1:
        valid = False
        flash("Last name cannot be empty!")
    elif not request.form['last_name'].isalpha():
        valid = False
        flash('Last name cannot contain numbers or special characters')
    if (request.form['password']) != (request.form['confirm_password']):
        valid = False
        flash("Passwords must match!")
    if len(request.form['password']) < 1:
        valid = False
        flash("Password cannot be empty!")
    if len(request.form['password']) >= 1 and len(request.form['password']) < 9:
        valid = False
        flash("Password must be more than 8 characters!")
    elif not PASSWORD_REGEX.match(request.form['password']):
        valid = False
        flash('Password must contain at least one uppercase letter and one number')
    if len(request.form['confirm_password']) < 1:
        valid = False
        flash("Password confirmation cannot be empty!")

    session['info'] = {
        "email": request.form['email'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "password": request.form['password'],
    }
    if valid == True:
        return redirect('/display')
    if valid == False:
        return redirect('/')

@app.route('/display')
def display():
    print "/display"
    if 'info' in session.keys():
        email = session['info']['email']
        first_name = session['info']['first_name']
        last_name = session['info']['last_name']
        password = session['info']['password']
        return render_template('display.html', email=email, first_name=first_name, last_name=last_name, password=password)
    return render_template('display.html')

@app.route('/reset')
def reset():
    session.pop('info')
    return redirect('/')

app.run(debug=True)      # Run the app in debug mode.

# Create a simple registration page with the following fields:
#
# email
# first_name
# last_name
# password
# confirm_password
# Here are the validations you must include:
#
# All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match
# When the form is submitted, make sure the user submits appropriate information. If the user did not submit appropriate information, return the error(s) above the form that asks the user to correct the information.
#
# Message Flashing with Categories
# For this, you will need to use flash messages at the very least. You may have to take this one step further and add categories to the flash messages. You can learn that from the flask doc: flash messages with categories
#
# If the form with all the information is submitted properly, simply have it say a message "Thanks for submitting your information."
#
# Ninja Version:
# Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.
