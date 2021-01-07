from flask import Flask, jsonify, redirect, url_for, request, render_template
from flask_cors import CORS
from LibrarySystemProject import main
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Sequence
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
def menu():
    return render_template('MainMenu.html')
#Main Menu
@app.route('/', methods = ['POST', 'GET'])
def menuResult():
    if request.method == 'POST':
        if request.form['MainMenu'] == 'Library':
            result = request.form
            return render_template("libraryMenu.html", result = result)
        elif request.form['MainMenu'] == 'Customers':
            result = request.form
            return render_template("customerMenu.html", result = result)
        elif request.form['MainMenu'] == 'Transactions':
            result = request.form
            return render_template("transactionsMenu.html", result = result)
        elif request.form['MainMenu'] == 'Save and Exit':
            pass
        elif request.form['menu'] == 'Return to Main Menu':
            result = request.form
            return render_template("MainMenu.html", result = result)
    return 
#Library Sub Menu

#Customer Sub Menu
  
#Transactions Sub Menu

if __name__ == '__main__':
    app.run()



#https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
#http://localhost:5000/ping
