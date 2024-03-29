from flask import Flask, request, Response, render_template, redirect
import src.core.db as database
from src.core.accessor import Accessor
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homepage():
    if request.method != "GET":
        return "Invalid HTTP method"

    return render_template("index.html")

@app.route('/drinks', methods=["GET", "POST"])
def drinks_page():
    
    if request.method == "POST":
        drink_name = request.form.get("drink_name").strip()
        if (drink_name != ""):
            database.add_new_drink(drink_name)
        return redirect("/drinks")
    elif request.method != "GET":
        return "Invalid HTTP method"

    drinks = database.get_all_drinks()
    return render_template('drinks_view.html', drinks=drinks)

@app.route('/rounds', methods=["GET", "POST"])
def rounds_page():
    if request.method == "POST":
        maker_id = int(request.form.get("maker_id"))
        round_duration = int(request.form.get("round_duration"))
        database.create_round(maker_id, round_duration) 
        return redirect("/rounds")
    elif request.method != "GET":
        return "Invalid HTTP method"
    
    current_rounds = database.get_current_rounds()
    past_rounds = database.get_past_rounds(3)
    people = database.get_all_people()
    return render_template('rounds_view.html', current_rounds=current_rounds, past_rounds=past_rounds, people=people)

@app.route('/rounds/<int:round_id>/orders', methods=["GET", "POST"])
def round_info(round_id):
    print(request.method)
    if request.method == "POST":
        person_id = request.form.get("person_id")
        drink_id = request.form.get("drink_id")
        special_requests = request.form.get("special_requests")
        database.add_order_to_round(round_id, person_id, drink_id, special_requests)
        return redirect('/rounds/' + str(round_id) + '/orders')
    elif request.method != "GET":
        return "Invalid HTTP method"
    
    round = database.get_round_by_round_id(round_id)
    people = database.get_all_people()
    drinks = database.get_all_drinks()
    drink_orders = {}
    for order in round["orders"]:
        drink_name = order["drink_name"]
        if drink_name not in drink_orders:
            drink_orders[drink_name] = [order]
        else:
            drink_orders[drink_name].append(order)
    round["orders"] = drink_orders
    return render_template("orders_view.html", round=round, people=people, drinks=drinks, testing="testing1")

@app.route("/people", methods=["GET", "POST"])
def people_page():
    people = database.get_all_people()
    drinks = database.get_all_drinks()

    if request.method == "POST":
        first_name = request.form.get("first_name")
        surname = request.form.get("surname")
        drink_id = request.form.get("preferred_drink_id")

        database.add_new_person(first_name, surname, drink_id)
        return redirect("/people")
    elif request.method != "GET":
        return "Invalid HTTP method"
    
    return render_template("people_view.html", people=people, drinks=drinks)

@app.route("/people/edit", methods=["POST"])
def update_person():
    if request.method != "POST":
        return "Invalid HTTP Method"
    preferred_drink_id = request.form.get("preferred_drink_id")
    person_id = request.form.get("person_id")
    database.update_drink_preference(person_id, preferred_drink_id)

    return redirect("/people")

@app.route("/people/<int:person_id>/drink", methods=["GET"])
def get_drink_preference_info(person_id):
    if request.method != "GET":
        return "Invalid HTTP Method"
    
    result = database.get_drink_preference_by_person_id(person_id)
    json_encoded = json.dumps(result) 
    return json_encoded

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)