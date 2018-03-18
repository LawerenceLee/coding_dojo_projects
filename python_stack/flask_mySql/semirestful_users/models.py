from datetime import datetime
import subprocess

from peewee import (DateTimeField, CharField, MySQLDatabase, Model,
                    OperationalError)

db_name = "semi_restful_api_db"
db = MySQLDatabase("semi_restful_api_db", user="root", password="root",
                   host="localhost", port=3306)


class User(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = CharField(max_length=255)
    created_at = DateTimeField(default=datetime.now)
    modified_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        schema = db_name


def initialize():
    try:
        db.connect()
    except OperationalError:
        cmdline = ['mysql', '-u', 'root', '-p']
        p = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
        p.communicate(
            "CREATE SCHEMA {} DEFAULT CHARACTER SET utf8;".format(db_name))
        db.connect()
    finally:
        db.create_tables([User], safe=True)
        db.close()


if __name__ == '__main__':
    initialize()
