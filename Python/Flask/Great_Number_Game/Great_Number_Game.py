from flask import Flask, render_template, request, session, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'SecretKey'
import random

@app.route('/')
def main():
    if 'target' not in session:
        session['target'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/result', methods=['post'])
def result():
   if session['target'] == int(request.form['guess']):
       session['result'] = 'correct'
   elif session['target'] > int(request.form['guess']):
       session['result'] = 'low'
   elif session['target'] < int(request.form['guess']):
       session['result'] = 'high'
   print session['result']
   return redirect('/')

@app.route('/reset')
def reset():
   session.pop('target')
   session.pop('result')
   return redirect('/')
app.run(debug=True)     # Run the app in debug mode.

# Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.
