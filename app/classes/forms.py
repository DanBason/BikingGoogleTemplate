# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])
    submit = SubmitField('Post')
   

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class RecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired()])
    genre = SelectField('Recipe Genre',choices=[("Breakfast","Breakfast"),("Brunch","Brunch"),("Lunch","Lunch"),("Dinner","Dinner"),("Dessert","Dessert")])
    author = StringField('Author', validators=[DataRequired()])
    image = FileField()
    summary = StringField('Recipe summary', validators=[DataRequired()])
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    recipe = StringField('Recipe', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    submit = SubmitField('Post')
   