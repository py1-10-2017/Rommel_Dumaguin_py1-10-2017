from flask import Flask, render_template, request, session, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'SecretKey'
import random
from datetime import datetime

@app.route('/')
def main():
    # session.clear()
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session['win_lose'] = ''
    # print session.keys()
    # print session['activities']

    return render_template('index.html', activities=session['activities'])

@app.route('/process_money', methods=['post'])
def result():
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    if request.form['building'] == 'farm':
        print "farm"
        temp = random.randrange(10,20+1)
        session['gold'] += temp
        session['activities'].append({'activity':"Earned {} gold from the farm! ({})".format(temp,time), 'class':'win'})
        # session['win_lose'] = 'win'
    elif request.form['building'] == 'cave':
        print "cave"
        temp = random.randrange(5,10+1)
        session['gold'] += temp
        session['activities'].append({'activity':"Earned {} gold from the cave! ({})".format(temp,time), 'class':'win'})
        # session['win_lose'] = 'win'
    elif request.form['building'] == 'house':
        print "house"
        temp = random.randrange(2,5+1)
        session['gold'] += temp
        session['activities'].append({'activity':"Earned {} gold from the house! ({})".format(temp,time), 'class':'win'})
        # session['win_lose'] = 'win'
    elif request.form['building'] == 'casino':
        print "casino"
        temp = random.randrange(-50,50+1)
        if temp < 0:
            session['activities'].append({'activity':"Earned {} gold from the casino! ({})".format(temp,time), 'class':'lose'})
            # session['win_lose'] = 'lose'
        else:
            session['activities'].append({'activity':"Earned {} gold from the casino! ({})".format(temp,time), 'class':'win'})
            # session['win_lose'] = 'win'
        session['gold'] += temp



   # if session['target'] == int(request.form['guess']):
   #     session['result'] = 'correct'
   # elif session['target'] > int(request.form['guess']):
   #     session['result'] = 'low'
   # elif session['target'] < int(request.form['guess']):
   #     session['result'] = 'high'
   # print session['result']
    return redirect('/')

@app.route('/reset')
def reset():
   session.pop('target')
   session.pop('result')
   return redirect('/')
app.run(debug=True)     # Run the app in debug mode.

# Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.
