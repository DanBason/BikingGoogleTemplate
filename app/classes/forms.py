# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, SelectMultipleField

from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField
from wtforms.validators import DataRequired

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image")
    role = SelectField('Role', choices=[("Teacher", "Teacher"), ("College Student", "College Student"), ("Parent", "Parent"), ("K-12 Student", "K-12 Student")], validators=[DataRequired()])
    college_roles = SelectField('College Roles', choices=[("Freshman", "Freshman"), ("Sophomore", "Sophomore"), ("Junior", "Junior"), ("Senior", "Senior")], validators=[DataRequired()])
    college = StringField('College')
    major = StringField('Major')
    state = SelectField('State', choices=[("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"), ("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"), ("FL", "Florida"), ("GA", "Georgia"), ("HI", "Hawaii"), ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"), ("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"), ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"), ("MS", "Mississippi"), ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"), ("NV", "Nevada"), ("NH", "New Hampshire"), ("NJ", "New Jersey"), ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"), ("ND", "North Dakota"), ("OH", "Ohio"), ("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"), ("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"), ("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"), ("WV", "West Virginia"), ("WI", "Wisconsin"), ("WY", "Wyoming")])

    submit = SubmitField('Post')

    #  def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.role.choices = [("Teacher", "Teacher"), ("College Student", "College Student"), ("Parent", "Parent"), ("K-12 Student", "K-12 Student")]

    #  def validate(self):
    #     if not super(ProfileForm, self).validate():
    #         return False

    #     if self.role.data == 'College Student':
    #         self.college_roles.validators = [DataRequired()]
    #         self.college.validators = [DataRequired()]
    #         self.major.validators = [DataRequired()]
    #         self.state.validators = [DataRequired()]
    #     else:
    #         self.college_roles.validators = []

# need to figure this out


   

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
    state = StringField('College Statte',validators=[DataRequired()])
    owner = StringField('Author', validators=[DataRequired()])
    image = FileField()
    summary = StringField("Summary", validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    tech_grad_year = IntegerField('Tech Graduation Year', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    submit = SubmitField('Post')
   