import datetime

from flask import (Flask, render_template, request)

from mysqlconnection import MySQLConnector

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
mysql = MySQLConnector(app, "new_friends_db")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "name": request.form['name'],
            "age": request.form["age"],
            "friends_since": datetime.date.today(),
        }
        insert = "INSERT INTO friends (name, age, friends_since) VALUES (:name, :age, :friends_since)"
        mysql.query_db(insert, data)

    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    for friend in friends:
        friend['year'] = friend['friends_since'].strftime("%Y")
    return render_template('index.html', friends=friends)


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)