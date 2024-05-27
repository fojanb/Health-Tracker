# importing Flask and other modules
from flask import Flask,request,render_template
from requests import get
import json

# We need a Flask object to setup a server:
app = Flask(__name__)

# ----------------------------------------------
#set route for /repositories 
@app.route('/repositories',methods =["GET"])
def get_data():
    username = request.args.get('username')
    resposne = get(f"https://api.github.com/users/{username}/repos")
    data = json.dumps(resposne.json())
    return render_template('repositories.html',data=data,username=username)

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