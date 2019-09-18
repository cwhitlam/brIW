import time

class Round:
    def __init__(self, maker, orders = []):
        self.maker  = maker
        self.orders = orders

    def display_round_orders(self):
        print(self.orders) 

    def save_round(self, file_man):
        json_rep = self.get_json_representation()
        file_man.save_to_file(json_rep, "src/stored_data/round.json")
    
    def get_json_representation(self):
        json_rep = {
            "maker_id": self.maker.id
        }
        orders_array = []
        for order in self.orders:
            orders_array.append({
                "person_id": order.person.id,
                "drink_id": None if order.drink == None else order.drink.id
            })
        json_rep["orders"] = orders_array
        return json_rep

class Order:
    def __init__(self, person, drink):
        self.person = person
        self.drink  = drink
    