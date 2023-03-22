from app import app

from flask import Flask, render_template, request, redirect, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import sqlite3


# This is for rendering the home page





@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profilemy')
@login_required
def profile():
    return render_template('profilemy.html')

@app.route('/college')
def college():
    return render_template('college.html')

@app.route('/collegeq')
def collegeq():
    return render_template('collegeq.html')

@app.route('/message')
@login_required
def message():
    
    return render_template('message.html')

@app.route('/collegelist')
def collegelist():
    return render_template('collegelist.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    bio = request.form['bio']
    
    # Handle profile picture upload
    if 'profile_picture' in request.files:
        profile_picture = request.files['profile_picture'].read()
    else:
        profile_picture = None
    
    # Insert user data into the database
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email, bio, profile_picture) VALUES (?, ?, ?, ?)', 
                (name, email, bio, profile_picture))
    conn.commit()
    conn.close()
    
    # Redirect to the user's profile page
    return redirect(url_for('profile', user_id=cur.lastrowid))


@app.route('/profile/<int:user_id>')
def profile_SQL(user_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cur.fetchone()
    conn.close()
    
    return render_template('profile.html', user=user)



