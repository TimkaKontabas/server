from collections import namedtuple


User = namedtuple('User', 'id username password permission_level')


import sqlalchemy as db
from werkzeug.security import generate_password_hash, check_password_hash
from Permission_level import PermissionLevel

engine = db.create_engine('sqlite:///database/users.db')

connection = engine.connect()

metadata = db.MetaData()

users = db.Table('users', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('username', db.String),
    db.Column('password', db.String),
    db.Column('permission_level', db.Integer)
)

def get_users():
    select_all = users.select()
    result = connection.execute(select_all).fetchall()
    return result

def get_user(user_id):
    select = users.select().where(users.c.id == user_id)
    row = connection.execute(select).fetchone()
    return row_to_user(row)

def row_to_user(row):
    return User(id=row[0], username=row[1], password=row[2], permission_level=PermissionLevel(row[3]))

def get_user_by_username(username):
    select = users.select().where(users.c.username == username)
    row = connection.execute(select).fetchone()
    return row_to_user(row)

def add_user(username, password):
    try:
        password_hash = generate_password_hash(password)
        insert = users.insert().values(username=username, password=password_hash, permission_level=PermissionLevel.USER.value)
        connection.execute(insert)
        return get_user_by_username(username)
        
    except db.exc.IntegrityError:
        return False

def set_permission_level(user_id:int, permission_level:PermissionLevel):
    update = users.update().where(users.c.id == user_id).values(permission_level=permission_level.value)
    connection.execute(update)

def remove_user(username):
    delete = users.delete().where(users.c.username == username)
    connection.execute(delete)

def check_user(username, password):
    user = get_user_by_username(username)
    if user:
        return check_password_hash(user[2], password)
    else:
        return False

def finalize():
    connection.commit()
    connection.close()

def is_admin(user):
    try:
        return user.is_admin()
    except:
        return False
