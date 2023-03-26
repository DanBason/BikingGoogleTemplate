from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Recipe, Comment
from app.classes.forms import RecipeForm, CommentForm
from flask_login import login_required
import datetime as dt

#  @app.route('/recipe/new', methods=['GET', 'POST'])