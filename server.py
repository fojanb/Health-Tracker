# importing Flask and other modules
from flask import Flask,request,render_template
from requests import get
import json

# We need a Flask object to setup a server:
app = Flask(__name__)
# ----------------------------------------------
@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')
@app.route('/sign-up/help')
def sign_up_help():
    return render_template('sign-up-help.html')
# ----------------------------------------------
@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')

# ----------------------------------------------
#set route for homepage 
@app.route('/')
def get_home():
    return render_template('index.html')
# ----------------------------------------------
# run the flask app
if __name__ == "__main__":
    app.run()
# Useful
# https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask