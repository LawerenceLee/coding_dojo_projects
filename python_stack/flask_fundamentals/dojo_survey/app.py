from flask import (Flask, render_template, request)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", form=request.form)


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
