import datetime

from peewee import SqliteDatabase, DateTimeField, CharField, Model


db = SqliteDatabase('emails.db')


class Email(Model):
    email = CharField(max_length=50)
    timestamp = DateTimeField()

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Email], safe=True)


if __name__ == "__main__":
    initialize()
