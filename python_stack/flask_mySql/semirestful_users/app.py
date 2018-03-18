from flask import (Flask, render_template, flash, redirect, request)

from models import User, initialize, db


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)


@app.before_request
def _db_connect():
    db.connect()


@app.teardown_request
def _db_close(exe):
    if not db.is_closed():
        db.close()


@app.route('/users')
def index():
    return render_template('index.html')


@app.route('/users/create', method="POST")
@app.route('/users/new')
def new_user():
    if request.method == "POST":
        User.create(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
        )
        user_id = User.select(User.id).where(
            User.email == request.form['email']
            )
        return redirect("/users/{}".format(user_id))
    return render_template('create_user.html')


@app.route('/users/update')
def update():
    return render_template('update.html')


@app.route('/users/<id>/edit', methods=["GET", "POST"])
@app.route('/users/<id>/destroy')
def alter_user(id):
    user = User.get_by_id(id)
    if request.method == "POST":
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        user.save()
        return redirect("/users/{}".format(id))
    
    user.delete_instance()
    return redirect("/users")


@app.route('/users/<id>')
def user_by_id(id):
    user = User.get_by_id(id)
    return render_template("user.html", user=user)


if __name__ == "__main__":
    initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
