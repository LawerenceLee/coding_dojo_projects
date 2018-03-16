from peewee import CharField, DateField, MySQLDatabase, Model


db = MySQLDatabase("registration_login", user="root", password="root",
                   host="localhost", port=3306)


class User(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    birthdate = DateField()
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    salt = CharField(max_length=255)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()


if __name__ == "__main__":
    initialize()
    # User.create(
    #     first_name="Zach",
    #     last_name="Owens",
    #     birthdate="2012-02-12",
    #     email="fakeEmail@email.com",
    #     password="gibberish",
    # )
    print(User.get_by_id(1).first_name)
