from flask import Flask, render_template, request
import os
from cur_conv import *

app = Flask(__name__)



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
