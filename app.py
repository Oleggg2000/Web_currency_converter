from flask import Flask, render_template
from cur_conv import *

app = Flask(__name__)

@app.route('/')
def index():
    values = [check_currency(DOLLAR_RUB), check_currency(EURO_RUB), check_currency(JPY_RUB)]
    for value in values:
        print(value)
    return render_template("index.html", cur_value=values)

if __name__ == "__main__":
    app.run()
