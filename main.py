import pymysql
from peewee import *
from playhouse.db_url import connect
from fastapi import FastAPI
pymysql.install_as_MySQLdb()

db = connect("mysql://root:Mjy123456~@localhost:3306/zhangdapeng")


app=FastAPI()

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
# db.create_tables([User,Auth])
# User(username="majingyu",password="majingyu",role_id=1,role_name="超级管理员").save()
# Auth(name="超级管理员",menus="首页:/,登录:/login",auths="POST:/auth/login,POST:/auth/register,GET:/auth/userinfo").save()
# Auth(name="普通用户",menus="首页:/,登录:/login",auths="POST:/auth/login,POST:/auth/register").save()

@app.post("/auth/login")
async def login():
    return {"token":"xxx"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app")

