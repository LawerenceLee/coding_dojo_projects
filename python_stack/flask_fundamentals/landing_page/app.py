from flask import (Flask, render_template)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")


@app.route('/dojos/new', methods=["GET", "POST"])
def dojo():
    return render_template("new_dojo_form.html")


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
