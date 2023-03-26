from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/aboutus')
def AboutUs():
    return render_template('aboutus.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question')
def questionpage():
    return render_template('questions.html')
    
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/college')
def recipe():
    return render_template('college.html')