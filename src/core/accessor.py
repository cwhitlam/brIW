from src.core.person import Person
from src.core.drink import Drink

class Accessor:
    def __init__(self, file_man):
        drinks = file_man.load_from_file("./src/stored_data/drinks.json")
        self.drinks = self.create_drinks_dict(drinks)
        people = file_man.load_from_file("./src/stored_data/people.json")
        self.people = self.create_people_dict(people, self.drinks)
        self.current_round = None
        self.file_man = file_man

    def get_people(self):
        return self.people

    def get_drinks(self):
        return self.drinks

    def set_people(self, people):
        self.people = people

    def set_drinks(self, drinks):
        self.drinks = drinks

    def get_current_round(self):
        return self.current_round

    def set_current_round(self, current_round):
        self.current_round = current_round

    def create_people_dict(self, people, drinks):
        people_dict = {}
        for person in people:
            if person["prefered_drink_id"] == None:
                prefered_drink = None
            else:
                prefered_drink = drinks[person["prefered_drink_id"]]
            people_dict[person["id"]] = Person(person["id"], person["name"], prefered_drink)
        return people_dict

    def create_drinks_dict(self, drinks):
        drinks_dict = {}
        for drink in drinks:
            drinks_dict[drink["id"]] = Drink(drink["id"], drink["name"])
        return drinks_dict

    def get_new_id(self, table):
        #if table is false. dictionary is empty, return 0 id for first item
        if bool(table):
            current_highest_id = list(table.keys())[-1]
            return current_highest_id + 1
        else:
            return 0

    def get_person_name_by_id(self, id):
        
        try:
            return self.people[id]
        except:
            print(f"No person has the id {id}")
            quit()

    def get_drink_name_by_id(self, id):
        try:
            return self.drinks[id]
        except:
            print(f"No drink with id: {id}")
            quit()

    def save_people(self):
        json_rep = self.file_man.convert_to_json(self.get_people())
        self.file_man.save_to_file(json_rep, "src/stored_data/people.json")
