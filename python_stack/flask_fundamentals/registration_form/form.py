from datetime import datetime
import re


class FormValidation(object):
    def __init__(self, form):
        self.email = form['email'][0]
        self.first_name = form["first_name"][0]
        self.last_name = form["last_name"][0]
        self.birthdate = form["birthdate"][0] + " 00:00"
        self.password = form["password"][0]
        self.confirm_password = form["confirm_password"][0]

    def is_email_valid(self):
        if re.findall(
                r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                self.email):
            return True
        return False

    def is_fullname_valid(self):
        if re.findall(r"[0-9]+", self.first_name) or re.findall(
                r"[0-9]+", self.last_name):
            return False
        return True

    def is_valid_birthdate(self):
        try:
            if datetime.strptime(
                    self.birthdate, "%Y/%m/%d %H:%M") < datetime.today():
                return True
            return False
        except ValueError:
            return False

    def is_password_valid(self):
        if self.password == self.confirm_password:
            if re.findall(r"[A-Z]+", self.password):
                if re.findall(r"[0-9]+", self.password):
                    return True
        return False


if __name__ == "__main__":
    form = {
        "email": "extraToppings@yahoo.com",
        "first_name": "Laurie",
        "last_name": "Hubert",
        "birthdate": "1990/12/05",
        "password": "Jibberish1",
        "confirm_password": "Jibberish1",
    }
    bad_form = {
        "email": "",
        "first_name": "Laurie",
        "last_name": "Hube1rt",
        "birthdate": "31900/12/05",
        "password": "jibberish",
        "confirm_password": "jibberishh",
    }
    check = FormValidation(form)
    bad = FormValidation(bad_form)
    print("Check's Email: {}".format(check.is_email_valid()))
    print("Bad's Email: {}\n".format(bad.is_email_valid()))

    print("Check's Fullname: {}".format(check.is_fullname_valid()))
    print("Bad's Fullname: {}\n".format(bad.is_fullname_valid()))

    print("Check's Birthdate: {}".format(check.is_valid_birthdate()))
    print("Bad's Birthdate: {}\n".format(bad.is_valid_birthdate()))

    print("Check's Password: {}".format(check.is_password_valid()))
    print("Bad's Password: {}\n".format(bad.is_password_valid()))
    
