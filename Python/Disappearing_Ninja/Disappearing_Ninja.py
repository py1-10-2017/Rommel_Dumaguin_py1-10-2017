from flask import Flask, render_template, request, session, redirect, flash
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def display():
    print "/ninja"
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def which_ninja(color):
    print color
    if color.lower() == 'blue':
        ninja = 'leonardo'
    elif color.lower() == 'orange':
        ninja = 'michelangelo'
    elif color.lower() == 'red':
        ninja = 'raphael'
    elif color.lower() == 'purple':
        ninja = 'donatello'
    else:
        ninja = 'notapril'
    return render_template('ninja.html', ninja=ninja)

app.run(debug=True)      # Run the app in debug mode.

# This exercise will help you practice URL routing, using views, and rendering static content. Start by creating a new project called disappearing_ninjas.
#
# These are the routes that you need to set up:
#
# On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
# When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
# /ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL)
# If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
# /ninja/orange - Ninja Turtle Michelangelo.
# /ninja/red - Ninja Turtle Raphael
# /ninja/purple - Ninja Turtle Donatello
# If a user tries to hack into your web app by specifying a color or string combination other than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then display Megan Fox who was April O'Neil in the most recent ninja turtles movie.
# You'll need to remember how to use static files for this assignment. Take a minute to refresh your memory back to the static files section if you need to :)
