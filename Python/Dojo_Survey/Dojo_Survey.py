from flask import Flask, render_template, request, session, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
# @app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
#                          # function to the '/' route. This means that whenever we send a request to
#                          # localhost:5000/ we will run the following "hello_world" function.
# def hello_world():
#   return 'Hello World!'  # Return 'Hello World!' to the response.
# app.run(debug=True)      # Run the app in debug mode.

@app.route('/')
def survey():
  return render_template('index.html')

# @app.route('/result')
@app.route('/result', methods=['POST'])
def result():
   # print "Got Post Info"
   name = request.form['name']
   dojo_location = request.form['dojo_location']
   favorite_language = request.form['favorite_language']
   comment = request.form['comment']
   return render_template('result.html', x=request.form['name'], y=request.form['dojo_location'], z=request.form['favorite_language'],c=request.form['comment'])
   return redirect('/')
app.run(debug=True)      # Run the app in debug mode.
