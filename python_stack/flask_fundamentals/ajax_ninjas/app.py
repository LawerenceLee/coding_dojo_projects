from flask import (Flask, request, url_for, render_template, jsonify)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form:
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
                "name": "Raphael",
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
    else:
        return render_template('index.html')


# learned info from : https://www.youtube.com/watch?v=IZWtHsM3Y5A

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)