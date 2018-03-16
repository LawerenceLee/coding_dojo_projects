from flask import (Flask, g, render_template, flash, redirect, url_for,
                   abort)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)