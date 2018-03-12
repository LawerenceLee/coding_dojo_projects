from flask import (Flask, render_template, flash, redirect, request)

from form import FormValidation


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', old_form=None)


@app.route('/validate', methods=["GET", "POST"])
def validate():
    old_form = request.form
    error = False
    form = FormValidation(dict(request.form))
    if not form.is_email_valid():
        print("Email Not Valid")
        error = True
    if not form.is_fullname_valid():
        print("Names are not valid")
        error = True
    if not form.is_valid_birthdate():
        print("birthdate is not valid")
        error = True
    if not form.is_password_valid():
        print("Password is not valid")
        error = True

    if error:
        return render_template("index.html", old_form=old_form)
    return "<h1>All is validated</h1>"



if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)