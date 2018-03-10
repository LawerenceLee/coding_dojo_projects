import random

from flask import (Flask, render_template, session, request)


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "asd;fvy[a48(*^7776798_(Up8y;kgs;oihvb'jfpgj'sdfjgsd'fposd"


@app.route('/', methods=['GET', 'POST'])
def index():
    '''The variable inner refers to code to go inside the div tag that is to
    be inserted into html doc, and outer refers to the code to go outside the
    div tag. Color variable is for the stying color of the div tag.
    '''
    inner = ""
    outer = '<form action="/" method="post"><input type="text" name="guess">'
    outer += '<button type="submit">Submit</button></form>'
    color = "red"

    try:
        random_num = int(session['random_num'])
        guess = int(request.form['guess'])
        print(guess, random_num)
    except ValueError:
        guess = 0
    except KeyError:
        pass

    if "random_num" not in session:
        session['random_num'] = random.randrange(0, 101)
        color = ""
    elif random_num > guess:
        inner = "<h1 style='color:white'>Too Low</h1>"
    elif random_num < guess:
        inner = "<h1 style='color:white'>Too High</h1>"
    elif random_num == guess:
        inner = '<h1 style="color:white">' + str(random_num)
        inner += " was the number!</h1>" + '<form method="post" action="/">'
        inner += "<button>Play Again</button></form>"
        color = "green"
        outer = ""
        session.clear()

    session['guess_box'] = '<div style="background-color:' + color + '">'
    session['guess_box'] += inner + '</div>' + outer
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
