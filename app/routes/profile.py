from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import College, Blog, Comment
from app.classes.forms import CollegeForm, BlogForm, CommentForm
from flask_login import login_required
import datetime as dt
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

table_schema = '''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        bio TEXT,
                        profile_picture BLOB
                    )'''
cur.execute(table_schema)
conn.commit()
conn.close()

cur.execute('INSERT INTO users (name, email, bio, profile_picture) VALUES (?, ?, ?, ?)', 
            ('John Doe', 'john.doe@example.com', 'I am a web developer', profile_picture))





