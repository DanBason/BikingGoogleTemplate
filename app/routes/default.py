from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')