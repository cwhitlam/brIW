class Person:
    def __init__(self, id, name, prefered_drink, last_order = None):
        self.id = id
        self.name = name
        self.prefered_drink = prefered_drink
        self.last_order = last_order

    def set_prefered_drink(self, prefered_drink):
        self.prefered_drink = prefered_drink

    def get_json_representation(self):
        return {
                    "id": self.id, 
                    "name": self.name, 
                    "prefered_drink_id": self.prefered_drink.id
        }

    #def __repr__(self):
        #return self.name