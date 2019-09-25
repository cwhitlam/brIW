from src.core.person import Person
from src.core.drink import Drink
import src.core.db as queries

class Accessor:
    def __init__(self, file_man =None):
        self.current_round = None
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

    def set_people(self, people):
        self.people = people

    def set_drinks(self, drinks):
        self.drinks = drinks

    def get_current_round(self):
        return self.current_round

    def set_current_round(self, current_round):
        self.current_round = current_round

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