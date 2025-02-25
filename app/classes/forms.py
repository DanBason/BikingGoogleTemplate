# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, SelectMultipleField
from app.classes.data import User
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField
from wtforms.validators import DataRequired
from bson import ObjectId

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image")
    role = SelectField('Role', choices=[("Teacher", "Teacher"), ("College Student", "College Student"), ("Parent", "Parent"), ("K-12 Student", "K-12 Student")], validators=[DataRequired()])
    submit = SubmitField('Post')

    

# need to figure this 


class SearchForm(FlaskForm):
	searched = StringField("Searched", validators=[DataRequired()])
	submit = SubmitField("Submit")  

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class QuestionForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Question', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Ask')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class CollegeForm(FlaskForm):
    
    name = StringField('College Name', validators=[DataRequired()])
    state = StringField('College State',validators=[DataRequired()])
    image = FileField()
    major = StringField('Major', validators=[DataRequired()])
    tech_grad_year = IntegerField('Tech Graduation Year', validators=[DataRequired()])
    tech_academy = SelectField('Academy', choices=[("Health", "Health"), ("Computer Science", "Computer Science"), ("FADA", "FADA"), ("RPL", "RPL"), ("Engineering", "Engineering")], validators=[DataRequired()] )
    tags = StringField('Tags', validators=[DataRequired()])
    
    submit = SubmitField('Post')

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    
    recipient = SelectField('Recipient', choices=[], validators=[DataRequired()])
    
   