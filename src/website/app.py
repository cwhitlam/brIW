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
        people = database.get_all_people()
        print(people)
        return render_template('rounds_view.html', rounds=rounds, people=people)
    else:
        return "Invalid HTTP method"

@app.route('/rounds/<int:round_id>', methods=["GET"])
def round_info(round_id):
    if request.method == "GET":
        round = database.get_round_by_round_id(round_id)
        drink_orders = {}
        for order in round["orders"]:
            drink_name = order["drink_name"]
            if drink_name not in drink_orders:
                drink_orders[drink_name] = [order]
            else:
                drink_orders[drink_name].append(order)
        round["orders"] = drink_orders
        print(round)
        return render_template("orders_view.html", round=round)
    else:
        return "Invalid HTTP method"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)