from datetime import datetime
import re


class FormValidation(object):
    flash_messages = []

    def __init__(self, form):
        self.email = form['email'][0]
        self.first_name = form["first_name"][0]
        self.last_name = form["last_name"][0]
        self.birthdate = form["birthdate"][0] + " 00:00"
        self.password = form["password"][0]
        self.confirm_password = form["confirm_password"][0]

        self.is_email_valid()
        self.is_fullname_valid()
        self.is_birthdate_valid()
        self.is_password_valid()

    def is_email_valid(self):
        if not re.findall(
                r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                self.email):
            self.flash_messages.append(
                ("Email is not in the correct format", "error")
            )

    def is_fullname_valid(self):
        if re.findall(r"[0-9]+", self.first_name):
            self.flash_messages.append(
                ("First name contains numbers", "error")
            )
        if re.findall(r"[0-9]+", self.last_name):
            self.flash_messages.append(("Last name contains numbers", "error"))

    def is_birthdate_valid(self):
        try:
            if not datetime.strptime(
                    self.birthdate, "%Y/%m/%d %H:%M") < datetime.today():
                self.flash_messages.append(
                    ("Birthdate cannot be in the present, nor future", "error")
                )
        except ValueError:
            self.flash_messages.append(
                ("Birthdate is not in the correct format", "error")
            )

    def is_password_valid(self):
        if self.password != self.confirm_password:
            self.flash_messages.append(
                ("Passwords do not match", "error")
            )
        if not re.findall(r"[A-Z]+", self.password):
            self.flash_messages.append(
                ("Password must contain at least one upper case character",
                    "error")
            )
        if not re.findall(r"[0-9]+", self.password):
            self.flash_messages.append(
                ("Password must contain at least one numerical character",
                 "error")
            )
