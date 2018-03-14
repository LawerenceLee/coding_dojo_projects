from flask import (Flask)
from mysqlconnection import MySQLConnector


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')

print mysql.query_db("SELECT * FROM users")

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)