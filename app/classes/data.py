from sys import getprofile
from tokenize import String
from typing import KeysView
from xmlrpc.client import Boolean
from setuptools import SetuptoolsDeprecationWarning
from app import app
from flask import flash
from flask_login import UserMixin
from mongoengine import FileField, EmailField, StringField, IntField, ReferenceField, DateTimeField, BooleanField, CASCADE
from flask_mongoengine import Document
import datetime as dt
import jwt
from time import time
from bson.objectid import ObjectId
import mongoengine
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'default': 'mydatabase',
    'host': 'localhost',
    'port': 27017
}
mongoengine.connect(db="my_db", alias="my_alias")
default = mongoengine.connection.get_db(alias="my_alias")


class College(UserMixin, Document):
    college_name = StringField()
    college_size = IntField()
    location = StringField()
    picture = FileField()
    state = StringField()
    town = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'order_by': ['-create_date']
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
    another_role = StringField()

    meta = {
        'order_by': ['lname', 'fname']
    }


class Blog(Document):
    author = ReferenceField('User', reverse_delete_rule=CASCADE) 
    subject = StringField()
    content = StringField()
    tag = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()
    new_field = StringField()

    meta = {
        'order_by': ['-create_date']
    }


class Comment(Document):
    author = ReferenceField('User', reverse_delete_rule=CASCADE) 
    blog = ReferenceField('Blog', reverse_delete_rule=CASCADE)
    comment = ReferenceField('Comment', reverse_delete_rule=CASCADE)
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'order_by': ['-create_date']
    }


class Question(Document):
    title = StringField(required=True, max_length=100)
    content = StringField(required=True)
    date_posted = DateTimeField(default=dt.datetime.utcnow)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    answers = ReferenceField('Answer')

    meta = {
        'order_by': ['-date_posted']
    }


class Answer(Document):
    content = StringField(required=True)
    date_posted = DateTimeField(default=dt.datetime.utcnow)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    question = ReferenceField(Question)
