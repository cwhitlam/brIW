from flask import Flask, request, Response, render_template
from src.api.person_handler import PersonHandler
from src.api.drink_handler import DrinkHandler
import src.core.db as database

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homepage():
    if request.method != "GET":
        return "Invalid HTTP method"

    return render_template("index.html")

@app.route('/drinks', methods=["GET", "POST"])
def drinks_page():
    if request.method == "GET":
        return render_template('drinks_view.html')
    elif request.method == "POST":
        drink_name = request.form.get("drink_name").strip()
        #if (drink_name != ""):
            #database.add_new_drink(drink_name)
        return render_template('drinks_view.html', drink_name=drink_name)
    else:
        return "Invalid HTTP method"

@app.route('/rounds', methods=["GET"])
def rounds_page():
    if request.method == "GET":
        rounds = database.get_rounds()
        """
        rounds = [
            {
                "maker_fullname": "Greg Ford",
                "num_of_orders": 3,
                "minutes_remaining": 10
            },
            {
                "maker_fullname": "Chris Whitlam",
                "num_of_orders": 5,
                "minutes_remaining": 20
            }
        ]
        """
        return render_template('rounds_view.html', rounds=rounds)
    else:
        return "Invalid HTTP method"

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)