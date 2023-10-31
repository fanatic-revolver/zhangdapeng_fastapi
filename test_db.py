import db
user=db.get_user("majingyu","majingyu")
print(user.username,user.password,user.role_name)