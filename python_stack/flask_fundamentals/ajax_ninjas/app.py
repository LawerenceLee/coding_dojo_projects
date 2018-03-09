from flask import (Flask, request, url_for, render_template, flash, redirect,
                   jsonify)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data_return', methods=['POST'])
def data_return():
    ninja_dict = {
        'blue': {
            "name": "Leonardo",
            "url": url_for('static', filename='img/leonardo.jpg')},
        'purple': {
            "name": "Donatello",
            "url": url_for('static', filename='img/donatello.jpg')},
        'orange': {
            "name": "Michelangelo",
            "url": url_for('static', filename='img/michelangelo.jpg')},
        'red': {
            "name": "Rapheal",
            "url": url_for('static', filename='img/raphael.jpg')}
    }
    color = request.form['color']
    try:
        name_and_url = ninja_dict[color]
    except KeyError:
        return jsonify(
            {"april_url": url_for("static", filename="img/notapril.jpg")})
    else:
        return jsonify(name_and_url)


# Ajax works, just need to set up logic to take a color and return a turtle's img and name

# learned info from : https://www.youtube.com/watch?v=IZWtHsM3Y5A

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)