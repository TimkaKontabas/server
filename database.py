import sqlalchemy as db

engine = db.create_engine('sqlite:///database/mail_database.db')

connection = engine.connect()

metadata = db.MetaData()

# Код отделения, Адрес, Телефон, Время открытия, Время закрытия
mail_otdels = db.Table('Почтовые отделения', metadata,
    db.Column('Код отделения', db.Integer, primary_key=True),
    db.Column('Адрес', db.String),
    db.Column('Телефон', db.String),
    db.Column('Время открытия', db.String),
    db.Column('Время закрытия', db.String)
)

metadata.create_all(engine)

select_all = mail_otdels.select()

result = connection.execute(select_all).fetchall()

for row in result:
    print(row)