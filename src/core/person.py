class Person:
    def __init__(self, id, first_name, surname, prefered_drink = None):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.full_name = first_name + " " + surname
        self.prefered_drink = prefered_drink