from app import app
from flask import flash
from flask_login import UserMixin
from mongoengine import FileField, ObjectIdField, EmailField, StringField, IntField, ReferenceField, DateTimeField, BooleanField, CASCADE
from flask_mongoengine import Document
import datetime as dt
import jwt
from time import time
from wtforms import SelectField


class College(Document):
    name = StringField()
    state = StringField()
    image = FileField()
    major = StringField()
    tech_grad_year = IntField()
    tech_academy = StringField()
    tags = StringField()
    user = ReferenceField('User')
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()
    # user = ReferenceField('User', reverse_delete_rule=CASCADE)
    meta = {
        'ordering': ['-create_date']
    }


class User(UserMixin, Document):
    create_date = DateTimeField(default=dt.datetime.utcnow)
    gid = StringField(sparse=True, unique=True)
    gname = StringField()
    gprofile_pic = StringField()
    username = StringField()
    fname = StringField()
    lname = StringField()
    email = EmailField()
    image = FileField()
    pronouns = StringField()
    role = StringField()
    name = ReferenceField('College', reverse_delete_rule=CASCADE)
    state = ReferenceField('College', reverse_delete_rule=CASCADE)
    major = ReferenceField('College', reverse_delete_rule=CASCADE)
    tech_grad_year = ReferenceField('College', reverse_delete_rule=CASCADE)
    tech_academy = ReferenceField('College', reverse_delete_rule=CASCADE)
    tags = ReferenceField('College', reverse_delete_rule=CASCADE)
    userID = IntField()

    meta = {
        'ordering': ['lname', 'fname']
    }


class Blog(Document):
    author = ReferenceField('User', reverse_delete_rule=CASCADE) 
    subject = StringField()
    content = StringField()
    tag = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-create_date']
    }


class Question(Document):
    author = ReferenceField('User', reverse_delete_rule=CASCADE) 
    subject = StringField()
    content = StringField()
    tag = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-create_date']
    }


class Comment(Document):
    author = ReferenceField('User', reverse_delete_rule=CASCADE) 
    question = ReferenceField('Question', reverse_delete_rule=CASCADE)
    blog = ReferenceField('Blog', reverse_delete_rule=CASCADE)
    comment = ReferenceField('Comment', reverse_delete_rule=CASCADE)
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-create_date']
    }


class Message(Document):
    message = StringField()
    recipient_username = SelectField()
    recipient_id = StringField()
    author = ReferenceField('User', reverse_delete_rule=CASCADE)
    create_date = DateTimeField(default=dt.datetime.utcnow)

    meta = {
        'ordering': ['-create_date']
    }
