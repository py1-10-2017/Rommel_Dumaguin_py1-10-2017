import random
from flask import Flask, render_template, request, session, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'SecretKey'
# @app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
#                          # function to the '/' route. This means that whenever we send a request to
#                          # localhost:5000/ we will run the following "hello_world" function.

@app.route('/')
def counter():
  # session['count'] += 1
  session['count'] = random.randrange(0,101) # random number between 0-100
  return render_template('index.html')

@app.route('/plus2')
def plus2():
   session['count'] += 1
   return redirect('/')

@app.route('/reset')
def reset():
   session['count'] = -1
   return redirect('/')
app.run(debug=True)      # Run the app in debug mode.
