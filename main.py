import pymysql
from peewee import *
from playhouse.db_url import connect

pymysql.install_as_MySQLdb()

db = connect("mysql://root:Mjy123456~@localhost:3306/zhangdapeng")


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


db.connect()
db.create_tables([User,Auth])

