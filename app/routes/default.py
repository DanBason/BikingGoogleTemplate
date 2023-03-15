from app import app
from flask import render_template

# This is for rendering the home page

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profilemy')
def profile():
    return render_template('profilemy.html')