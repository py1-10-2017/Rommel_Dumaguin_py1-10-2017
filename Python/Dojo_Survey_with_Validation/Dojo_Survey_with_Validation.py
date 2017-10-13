from flask import Flask, render_template, request, session, redirect, flash
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def survey():
    # session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
       flash("Name cannot be empty!")
    if len(request.form['comment']) < 1:
       flash("Comment cannot be empty!")
    elif len(request.form['comment']) > 120:
       flash("Comment cannot be longer than 120 characters!")
    return render_template('process.html', x=request.form['name'], y=request.form['dojo_location'], z=request.form['favorite_language'],c=request.form['comment'])
    return redirect('/')
app.run(debug=True)      # Run the app in debug mode.
