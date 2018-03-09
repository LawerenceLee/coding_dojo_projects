from flask import (Flask, render_template)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja')
@app.route('/ninja/<color>')
def ninja(color=None):
    if color:
        if color == "blue":
            return render_template("blue.html")
        elif color == "purple":
            return render_template("purple.html")
        elif color == "red":
            return render_template("red.html")
        elif color == "orange":
            return render_template("orange.html")
        else:
            return render_template("april.html")

    return render_template("ninja.html")


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
