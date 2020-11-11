from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from cur_conv import *

Postgres_DATABASE_URL = os.environ.get("DATABASE_URL")
app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class CurCalc(db.Model):
    __tablename__= "cur_transactions"
    id = db.Column(db.Integer, primary_key=True)
    cur_from = db.Column(db.String(4))
    amount = db.Column(db.Float)
    cur_to = db.Column(db.String(4))

    def __init__(self, cur_from, amount, cur_to):
        self.cur_from = cur_from
        self.amount = amount
        self.cur_to = cur_to

@app.route('/')
def index():
    values = [check_currency(DOLLAR_RUB), check_currency(EURO_RUB), check_currency(JPY_RUB)]
    for value in values:
        print(value)
    return render_template("index.html", cur_value=values)

@app.route("/submit", methods=["POST"])
def submit():
    values = [check_currency(DOLLAR_RUB), check_currency(EURO_RUB), check_currency(JPY_RUB)]
    if request.method == "POST":
        from_cur = request.form["from"]
        amount = request.form["cash"]
        to_cur = request.form["to"]
        print(from_cur, amount, to_cur)
    return render_template("index.html", cur_value=values)



if __name__ == "__main__":
    app.run()
