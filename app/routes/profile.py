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




