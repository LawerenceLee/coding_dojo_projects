from flask import (Flask, flash, render_template, request)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = ";alsj;akvp8wfoa973878ph&*&P*Hyfi7h;jBO^T^&Y&T&^R&Y*&YO*R*&TI"


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result", methods=["POST"])
def result():
    error = False

    if not request.form['name'] or not request.form['comment']:
        flash("Your form contains empty fields")
        error = True
    if len(request.form['comment']) > 120:
        flash("The comment field has exceeded the 120 character limit")
        error = True

    if error:
        return render_template("index.html")
    return render_template("result.html", form=request.form)


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
