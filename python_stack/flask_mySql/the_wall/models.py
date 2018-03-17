import datetime

from peewee import (CharField, MySQLDatabase, Model, DateTimeField,
                    TextField, ForeignKeyField, DateField, RawQuery)


db = MySQLDatabase("the_wall.db", user="root", password="root",
                   host="localhost", port=3306)


class BaseModel(Model):
    class Meta:
        schema = "the_wall.db"
        database = db


class User(BaseModel):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    birthdate = DateField()
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    salt = CharField(max_length=255)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)


class Message(BaseModel):
    user_id = ForeignKeyField(User, backref="messages")
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)


class Comment(BaseModel):
    user_id = ForeignKeyField(User, backref="comments")
    message_id = ForeignKeyField(Message, backref="comments")
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)


@db.connection_context()
def initialize():
    db.create_tables([User, Message, Comment], safe=True)


if __name__ == "__main__":
    initialize()
