from flask import (Flask, render_template, redirect, request, url_for)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/process", methods=['POST'])
def process():
    print(request.form['your-name'])
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)