from flask import (Flask, render_template, flash, request)

from form import FormValidation


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "ariqpw008^(*%(^TUHUGTUDFOITFI&&oy69up9(*^obiyVI-oju"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form = FormValidation(dict(request.form))
        if form.flash_messages:
            for message, category in form.flash_messages:
                flash(message, category)
            return render_template("index.html", old_form=request.form)
        flash("Your form was successfully submitted", "success")
    return render_template('index.html', old_form=None)


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)