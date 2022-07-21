from flask import render_template,flash,redirect,request
from app import app
from app import pep

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Smile')

@app.route("/peppy", methods=['GET'])
def peppy():
    message = pep.pep()
    return render_template('home.html', message=message)
