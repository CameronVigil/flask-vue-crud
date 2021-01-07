from flask import Flask, jsonify, redirect, url_for, request, render_template
from flask_cors import CORS
from LibrarySystemProject import main
import sqlalchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Sequence
from random import choice
import string
from library import book
from customers import customer
from transactions import transaction
from base import Session, Base, engine

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#starts database instance
Base.metadata.create_all(engine)
session = Session()


# sanity check route
@app.route('/')
def hello():
    return render_template('MainMenu.html')

@app.route('/MainMenu', methods = ['POST', 'GET'])
def hi():
    if request.method == 'POST':
        if request.form['menu'] == 'Library':
            pass
        elif request.form['menu'] == 'Customers':
            pass
        elif request.form['menu'] == 'Transactions':
            pass
        elif request.form['menu'] == 'Save and Exit':
            pass
    return 

if __name__ == '__main__':
    app.run()



#https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
#http://localhost:5000/ping
