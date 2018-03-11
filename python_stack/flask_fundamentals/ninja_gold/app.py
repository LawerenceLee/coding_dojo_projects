from flask import (Flask, render_template, redirect, request, session)

from classes import Casino, Cave, Farm, House


DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
app = Flask(__name__)
app.secret_key = "as;dfhapy988798^*&OIYI&RGHIYRD#%*T(asU^%^ygaksfitu6e86goyou"


@app.route('/', methods=['GET', "POST"])
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []

    return render_template('index.html')


@app.route('/process_money', methods=["GET", "POST"])
def process_money():
    if request.form['building'] == 'farm':
        farm = Farm()
        session['gold'] += farm.gold_earned
        session['activities'].append(farm.__dict__)
    elif request.form['building'] == 'cave':
        cave = Cave()
        session['gold'] += cave.gold_earned
        session['activities'].append(cave.__dict__)
    elif request.form['building'] == 'house':
        house = House()
        session['gold'] += house.gold_earned
        session['activities'].append(house.__dict__)
    elif request.form['building'] == 'casino':
        casino = Casino()
        session['gold'] += casino.gold_earned
        session['activities'].append(casino.__dict__)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)