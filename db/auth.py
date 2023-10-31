from peewee import *
from .db import db
class User(Model):
    username = CharField()
    password = CharField()
    role_id=IntegerField()
    role_name=CharField()

    class Meta:
        database = db




class Auth(Model):
    name = CharField()
    menus = TextField()
    auths=TextField()


    class Meta:
        database = db

def get_user(username,password):
    return User.get(User.username==username,password==password)