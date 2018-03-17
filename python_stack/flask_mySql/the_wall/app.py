import binascii
import datetime
from hashlib import md5
import os

from flask import (Flask, render_template, flash, session, request,
                   redirect, jsonify)

from form_validation import FormValidation
from models import initialize, User, Message, Comment, db


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "ariqpw008^(*%(^TUHUGTUDFOITFI&&oy69up9(*^obiyVI-oju"


@app.route("/delete_message", methods=["GET", "POST"])
def delete_message():
    Message.delete().where(Message.id == request.form['message_id']).execute()
    return jsonify(True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form = FormValidation(dict(request.form))

        if form.flash_messages:
            for message, category in form.flash_messages:
                flash(message, category)
            return render_template("index.html", old_form=request.form)
        else:
            salt = binascii.b2a_hex(os.urandom(15))
            hashed_pw = md5(request.form['password'] + salt).hexdigest()
            User.create(
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                birthdate=request.form['birthdate'],
                email=request.form["email"],
                password=hashed_pw,
                salt=salt,
            )
            flash("Your user info was successfully submitted", "success")
            return redirect("/login")

    return render_template('index.html', old_form=None)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.get_or_none(User.email == request.form["email"])
        if user:
            crypt_passwd = md5(
                request.form['password'] + user.salt).hexdigest()
            if user.password == crypt_passwd:
                session['is_logged_in'] = True
                session['user_id'] = user.id
                session["first_name"] = user.first_name
                session["last_name"] = user.last_name
                session["email"] = user.email
                flash("Successful Login", "success")
                return redirect("/the_wall")
        flash("Either Email or Password is not correct", "error")
        return redirect("/login")

    return render_template("/login.html")


@app.route("/log_off")
def log_off():
    session.clear()
    return redirect("/")


@app.route("/the_wall")
def the_wall():
    messages = []
    # Grab all messages and the users that created them
    tuple_messages = db.execute_sql(
        "SELECT message.id, user.first_name, user.last_name, message.created_at, \
        message.content FROM message JOIN user ON message.user_id = user.id \
        ORDER BY message.created_at DESC;")
    # With each message's tuple create a dictionary of key val pairs
    for message in tuple_messages:
        message_info = "{} {} - {}".format(
            message[1], message[2], message[3].strftime("%B %d %Y"))
        message_dict = {
            "message_id": message[0],
            "message_info": message_info,
            "message_content": message[4],
            "message_deleteable": False,
            "comment_list": []
        }
        # Change "message_deletable value if message is not older that 30min"
        if message[3] > datetime.datetime.now() - datetime.timedelta(minutes=30):
            message_dict["message_deleteable"] = True
        # Grab all the comments made on message and their creators
        tuple_comments = db.execute_sql(
            "SELECT comment.id, user.first_name, user.last_name, \
            comment.message_id, comment.content, comment.created_at FROM \
            comment JOIN user ON user.id = comment.user_id \
            WHERE comment.message_id = {};".format(message[0])
        )
        # With each comment's tuple create a dict of key val pairs
        for comment in tuple_comments:
            comment_info = "{} {} - {}".format(
                comment[1], comment[2], comment[5].strftime("%B %d %Y"))
            comment_dict = {
                "comment_id": comment[0],
                "comment_info": comment_info,
                "comment_content": comment[4]
            }
            message_dict["comment_list"].append(comment_dict)
        # add each message dict to the messages list
        messages.append(message_dict)

    return render_template("the_wall.html", messages=messages)


@app.route("/ajax_comment", methods=["GET", "POST"])
def ajax_comment():
    Comment.create(
        user_id=session["user_id"],
        message_id=int(request.form['message_id']),
        content=request.form['comment_text']
    )
    comment = Comment.get(Comment.content == request.form["comment_text"])
    comment_info = session['first_name'] + " " + session['last_name'] + " - "
    comment_info += comment.created_at.strftime("%B %d %Y")
    comment_dict = {
        "comment": comment.content,
        "comment_info": comment_info,
    }
    return jsonify(comment_dict)


@app.route("/ajax_message", methods=["GET", "POST"])
def ajax_message():
    Message.create(
        user_id=session['user_id'],
        content=request.form["message_text"]
    )
    message = Message.get(Message.content == request.form["message_text"])
    message_info = session['first_name'] + " " + session['last_name'] + " - "
    message_info += message.created_at.strftime("%B %d %Y")
    message_dict = {
        "message": message.content,
        "message_info": message_info,
        "message_id": message.id,
    }
    return jsonify(message_dict)


if __name__ == "__main__":
    initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
