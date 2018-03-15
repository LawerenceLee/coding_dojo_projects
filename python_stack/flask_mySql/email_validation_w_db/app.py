import re
import datetime

from flask import (Flask, render_template, flash, request, redirect)

from model import Email, initialize


EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "asjdi0as;o97*(*&)(Uhgpoifpjaspoufasmljdhfoguspd9&%("


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not Email.get_or_none(Email.email == request.form['email']):
            if EMAIL_REGEX.match(request.form["email"]):
            
                Email.create(
                    email=request.form["email"],
                    timestamp=datetime.datetime.now(),
                )

                flash("The email address you entered ({}) \
                \nis a VALID email address! Thank you!".format(
                    request.form['email']))

                return redirect("/success")
            else:
                flash("Email is not valid!")
        else:
            flash("Email already exists!")

    return render_template('index.html')


@app.route("/success")
def success():
    emails = Email.select()
    return render_template("success.html", emails=emails)


if __name__ == "__main__":
    initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
