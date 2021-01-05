from flask import Flask, jsonify
from flask_cors import CORS
import sqlalchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Sequence
from random import choice
import string
from library import book
from customers import customer
from transactions import transaction
import base
from base import Session, Base, engine
import json
from LibrarySystemProject import main
import queries

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


if __name__ == '__main__':
    app.run()



#https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
#http://localhost:5000/ping
