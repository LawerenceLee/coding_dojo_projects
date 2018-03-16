import binascii
from hashlib import md5
import os

from flask import (Flask, render_template, flash, session, request, redirect)

from form_validation import FormValidation
from model import initialize, User


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "ariqpw008^(*%(^TUHUGTUDFOITFI&&oy69up9(*^obiyVI-oju"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form = FormValidation(dict(request.form))

        if form.flash_messages:
            for message, category in form.flash_messages:
                flash(message, category)
            return render_template("index.html", old_form=request.form)
        else:
            salt = binascii.b2a_hex(os.urandom(15))
            hashed_pw = md5(request.form['password'] + salt).hexdigest()
            User.create(
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                birthdate=request.form['birthdate'],
                email=request.form["email"],
                password=hashed_pw,
                salt=salt,
            )
            flash("Your user info was successfully submitted", "success")
            return redirect("/login")

    return render_template('index.html', old_form=None)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.get_or_none(User.email == request.form["email"])
        if user:
            crypt_passwd = md5(request.form['password'] + user.salt).hexdigest()
            if user.password == crypt_passwd:
                session['is_logged_in'] = True
                flash("Successful Login", "success")
                return redirect("/login")
        flash("Either Email or Password is not correct", "error")
        redirect("/login")

    return render_template("/login.html")


if __name__ == "__main__":
    initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
