from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
from LibrarySystemProject import main

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=['GET'])
def hello():
    return main()

@app.route('/MainMenu',methods = [])

if __name__ == '__main__':
    app.run()



#https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
#http://localhost:5000/ping
