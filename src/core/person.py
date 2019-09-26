class Person:
    def __init__(self, id, first_name, surname, prefered_drink = None):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.full_name = first_name + " " + surname
        self.prefered_drink = prefered_drink

    def __repr__(self):
        return self.full_name

    def set_prefered_drink(self, prefered_drink):
        self.prefered_drink = prefered_drink

    def get_json_representation(self):
        drink_id = self.prefered_drink.id if self.prefered_drink != None else None 
        return {
            "id": self.id, 
            "first_name": self.first_name,
            "surname": self.surname, 
            "prefered_drink_id": drink_id
        }