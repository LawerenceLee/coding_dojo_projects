from flask import (Flask, render_template, request)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    colors = {
        "red": 255,
        "green": 255,
        "blue": 255,
    }
    if request.form:
        print(request.values)
        colors['red'] = request.values["red"]
        colors['green'] = request.values["green"]
        colors['blue'] = request.values["blue"]
        print(colors)
    return render_template('index.html', colors=colors)


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)