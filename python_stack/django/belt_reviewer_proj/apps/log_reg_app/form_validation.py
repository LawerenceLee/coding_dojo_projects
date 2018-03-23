from datetime import date
import re


class FormValidation(object):

    def __init__(self, form):
        self.email = form['email']
        self.first_name = form["first_name"]
        self.last_name = form["last_name"]
        # self.birthdate = form["birthdate"]
        self.password = form["password"]
        self.confirm_password = form["confirm_password"]
        self.errors = []

        self.is_email_valid()
        self.is_fullname_valid()
        # self.is_birthdate_valid
        self.is_password_valid()

    def is_email_valid(self):
        regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        if not regex.match(self.email):
            self.errors.append(
                "Email is not in the correct format"
            )

    def is_fullname_valid(self):
        if not self.first_name:
            self.errors.append(
                "First name is empty"
            )
        elif len(self.first_name) < 2 or len(self.last_name) < 2:
            self.errors.append(
                "Names must be longer than two characters"
            )

        if re.findall(r"[0-9]+", self.first_name):
            self.errors.append(
                "First name contains numbers"
            )

        if not self.last_name:
            self.errors.append(
                "Last name is empty"
            )
        if re.findall(r"[0-9]+", self.last_name):
            self.errors.append("Last name contains numbers")

    def is_birthdate_valid(self):
        try:
            year, month, day = self.birthdate.split("-")
            print(year, month, day)
            birthday = date(int(year), int(month), int(day))
            if not birthday < date.today():
                self.errors.append(
                    "Birthdate cannot be in the present, nor future"
                )
        except ValueError:
            self.errors.append(
                "Birthdate is not in the correct format"
            )

    def is_password_valid(self):
        if self.password != self.confirm_password:
            self.errors.append(
                "Passwords do not match"
            )
        if not re.findall(r"[A-Z]+", self.password):
            self.errors.append(
                "Password must contain at least one upper case character"
            )
        if not re.findall(r"[0-9]+", self.password):
            self.errors.append(
                "Password must contain at least one numerical character"
            )
        if len(self.password) < 8:
            self.errors.append(
                "Password must be eight characters or longer"
            )