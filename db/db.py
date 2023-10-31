import pymysql

from playhouse.db_url import connect
from fastapi import FastAPI

pymysql.install_as_MySQLdb()

db = connect("mysql://root:Mjy123456~@localhost:3306/zhangdapeng")
app=FastAPI()


db.connect()
