from src.core.person import Person
from src.core.drink import Drink
from src.core.round import Round, Order
import src.core.db as queries

class Accessor:
    def __init__(self, file_man =None):
        self.file_man = file_man

    def get_people(self):
        result = queries.get_all_people()
        people = {}
        for person in result:
            drink_obj = None
            if (person["drink_id"] != None):
                drink_obj = Drink(person["drink_id"], person["drink_name"])
            person_obj = Person(person["person_id"], person["first_name"], person["surname"], drink_obj)
            people[person["person_id"]] = person_obj
        return people

    def get_drinks(self):
        result = queries.get_all_drinks()
        drinks = {}
        for drink in result:
            drink_obj = Drink(drink["drink_id"], drink["name"])
            drinks[drink["drink_id"]] = drink_obj
        return drinks

    def get_person(self, person_id):
        result = queries.get_person_by_id(person_id)
        drink = None
        if (result["preferred_drink_id"] != None):
            drink = Drink(result["preferred_drink_id"], result["drink_name"])
        person = Person(
            result["person_id"], 
            result["first_name"],
            result["surname"], 
            drink
        )
        return person, drink

    def get_drink(self, drink_id):
        result = queries.get_drink_by_id(drink_id)
        return Drink(result["drink_id"], result["drink_name"])

    def get_current_rounds(self):
        round_result = queries.get_current_rounds()
        if (round_result == None):
            return

        rounds = {}
        for round in round_result:
            maker_preferred_drink = None
            if (round["drink_id"] != None):
                maker_preferred_drink = Drink(round["drink_id"], round["drink_name"])
            
            maker = Person(
                round["maker_id"], 
                round["first_name"], 
                round["surname"], 
                maker_preferred_drink
            )

            orders_result = queries.get_orders_by_round_id(round["round_id"])
            orders = []
            for order in orders_result:
                ordered_drink = Drink(
                    order["drink_id"], 
                    order["drink_name"]
                )
                
                preferred_drink_result = queries.get_drink_preference_by_person_id(order['person_id'])
                preferred_drink = None
                if preferred_drink_result != None:
                    preferred_drink = Drink(
                        preferred_drink_result["drink_id"], 
                        preferred_drink_result["drink_name"]
                    )
                
                person = Person(
                    order["person_id"], 
                    order["first_name"], 
                    order["surname"], 
                    preferred_drink
                )

                order_obj = Order(person, ordered_drink)
                orders.append(order_obj)
            
            round_obj = Round(maker, round["minutes_remaining"], orders)
            rounds[round["round_id"]] = round_obj
        return rounds

    def get_round_orders(self, round_id):
        orders_result = queries.get_orders_by_round_id(round_id)

        orders = {}
        for order in orders_result:
            preferred_drink = None
            preferred_drink_result = queries.get_drink_preference_by_person_id(order["person_id"])
            if preferred_drink_result != None:
                preferred_drink = Drink(preferred_drink_result["drink_id"], preferred_drink_result["drink_name"])
            
            person_obj = Person(
                order["person_id"],
                order["first_name"],
                order["surname"],
                preferred_drink
            )
            drink_obj = Drink(
                order["drink_id"],
                order["drink_name"]
            )
            order_obj = Order(person_obj, drink_obj, order["special_requests"])
            orders[order["order_id"]] = order_obj
        return orders