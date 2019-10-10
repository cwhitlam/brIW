class Person:
    def __init__(self, id, first_name, surname, prefered_drink = None):
        self.id = id
        self.first_name = first_name.capitalize()
        self.surname = surname.capitalize()
        self.full_name = self.first_name + " " + self.surname
        self.prefered_drink = prefered_drink