from flask import (Flask, render_template)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
