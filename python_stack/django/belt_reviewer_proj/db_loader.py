import os

from django.core.wsgi import get_wsgi_application

'''THIS FILE NEEDS TO BE IN THE SAME DIR AS manage.py

All users created by this file have a password of 'Password1"
'''

# project_name_settings = "<project_name's>.settings"
# project_name_settings = "dojo_ninjas_main.settings"
project_name_settings = "belt_reviewer_main.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_name_settings)
application = get_wsgi_application()

# Example: from <location of models.py in relation to manage.py> import <model names>
from log_reg_app.models import User

users = [
    ['Barty', "Crouch", "barty_couch@gmail.com"],
    ["Jelly", "Bean", "jb@gmail.com"],
    ['Jackdon', "Brown", "jackB@gmail.com"]
]


def create_some_users():
    '''Create some user based on the data in users list'''
    for usr in users:
        user = User()
        user.first_name = usr[0]
        user.last_name = usr[1]
        user.email = usr[2]
        user.password = "$2b$12$XapAGj/42QCzYcgXBoiHG.3MohH0RsQ2IYQAHOGaPUg80KbteB2Ga"
        user.save()


def delete_users():
    '''Delete users created by script'''
    for usr in users:
        try:
            User.objects.get(email=usr[2]).delete()
        except User.DoesNotExist:
            print("USER {} {} is NOT in this database".format(usr[0], usr[1]))
        else:
            print("Deleted {} {}".format(usr[0], usr[1]))
    print("\n")


def see_users():
    '''See Users in database'''
    for user in User.objects.all():
        print(user)
        print("\n")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    see_users()
