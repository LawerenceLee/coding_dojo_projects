from flask import (Flask, render_template, flash, redirect, request)

from models import User, initialize, db


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "ahpsvhpih78y986yG&T*Y(^R*YI(&&F*OY*^OUB*T*GHBUTF"


@app.before_request
def _db_connect():
    db.connect()


@app.teardown_request
def _db_close(exe):
    if not db.is_closed():
        db.close()


@app.route('/users')
def index():
    users = User.select()
    return render_template('index.html', users=users)


@app.route('/users/create', methods=["POST"])
@app.route('/users/new')
def new_user():
    if request.method == "POST":
        User.create(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
        )
        user = User.get(
            User.email == request.form['email']
            )
        flash("Successfully Created User")
        return redirect("/users/{}".format(user.id))
    return render_template('create_user.html')


@app.route('/users/<int:id>/edit', methods=["GET", "POST"])
def update(id):
    user = User.get_by_id(id)
    return render_template('update.html', user=user)


@app.route('/users/update', methods=['POST'])
@app.route('/users/<int:id>/delete')
def alter_user(id=None):
    if request.method == "POST":
        user = User.get_by_id(request.form["user_id"])
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        user.save()
        flash("Successfully Made the Changes You asked for")
        return redirect("/users/{}".format(request.form["user_id"]))

    user = User.get_by_id(id)
    user.delete_instance()
    flash("Deleted User")
    return redirect("/users")


@app.route('/users/<int:id>')
def user_by_id(id):
    user = User.get_by_id(id)
    return render_template("user.html", user=user)


if __name__ == "__main__":
    initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
