import datetime

from peewee import (CharField, DateField, MySQLDatabase, Model, DateTimeField,
                    TextField, ForeignKeyField)


db = MySQLDatabase("registration_login", user="root", password="root",
                   host="localhost", port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    birthdate = DateField()
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    salt = CharField(max_length=255)
    created_at = DateField(default=datetime.date.today)
    updated_at = DateField(default=datetime.date.today)


class Message(BaseModel):
    user = ForeignKeyField(User, backref="messages")
    content = TextField()
    created_at = DateField(default=datetime.date.today)
    updated_at = DateField(default=datetime.date.today)


class Comment(BaseModel):
    user = ForeignKeyField(User, backref="comments")
    message = ForeignKeyField(Message, backref="comments")
    content = TextField()
    created_at = DateField(default=datetime.date.today)
    updated_at = DateField(default=datetime.date.today)


def initialize():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()


if __name__ == "__main__":
    initialize()
