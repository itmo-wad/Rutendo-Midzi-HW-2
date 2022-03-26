from flask import Flask, render_template, request, flash, redirect, send_from_directory
import pymongo
from pymongo import MongoClient

client = MongoClient ('localhost', 27017)
db = client


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/authorization', methods=['GET' , 'POST'])
def authorization():
    if request.method == 'GET':
        return render_template('sigin.html')

@app.route('/signup', methods=['GET' , 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')



app.run(host="localhost", port=5000, debug=True)