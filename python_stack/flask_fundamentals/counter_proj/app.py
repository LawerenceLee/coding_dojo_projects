from flask import (Flask, render_template, redirect, session)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "sdfasdfasdfasdasasdahwteh0835p26190248*65987y87ttabglazuv"


@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('index.html')


@app.route('/add_two')
def add_two():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset')
def reset():
    session['counter'] = 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
