from flask import Flask, render_template

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)
app.secret_key = "a;skdfa.dfskqn23rqaus08g35iybpweb[asjdf;asasdfasdasdfqwerd"


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
