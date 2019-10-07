import src.core.db as database
from src.core.person import Person
import json
from src.core.accessor import Accessor
from src.api.encoder import MyEncoder

class PersonHandler():
    def get(self):
        acc = Accessor()
        people = acc.get_people()
        json_encoded = json.dumps(people, cls=MyEncoder)
        return json_encoded

    def post(self, data):
        database.add_new_person(
            data["first_name"], 
            data["surname"],
            data["preferred_drink_id"]
        )     

    def patch(self, data):
        database.update_drink_preference(
            data["person_id"],
            data["preferred_drink_id"]
        )

class DrinkHandler():
    def get(self):
        acc = Accessor()
        people = acc.get_drinks()
        json_encoded = json.dumps(people, cls=MyEncoder)
        return json_encoded

    def post(self, data):
        database.add_new_drink(data["drink_name"])
    
class RoundHandler():
    def get(self):
        acc = Accessor()
        rounds = acc.get_current_rounds()
        json_encoded = json.dumps(rounds, cls=MyEncoder)
        return json_encoded

    def post(self, data):
        database.create_round(
            data["maker_id"],
            data["round_duration"]
        )

class OrderHandler():
    def get(self, round_id):
        acc = Accessor()
        orders = acc.get_round_orders(round_id)
        json_encoded = json.dumps(orders, cls=MyEncoder)
        return json_encoded

    def post(self, round_id, data):
        database.add_order_to_round(
            round_id,
            data["person_id"],
            data["drink_id"],
            data["special_requests"]
        )


