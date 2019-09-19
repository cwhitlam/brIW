import os
import sys
from src.ui.ui import UI
from src.json_file_manager import File_Manager
from src.core.round import Round, Order
from src.core.person import Person
from src.core.drink import Drink
from src.menus import MainMenu
from src.core.accessor import Accessor

def create_people_dict(people, drinks):
    people_dict = {}
    for person in people:
        if person["prefered_drink_id"] == None:
            prefered_drink = None
        else:
            prefered_drink = drinks[person["prefered_drink_id"]]
        people_dict[person["id"]] = Person(person["id"], person["name"], prefered_drink)
    return people_dict

def create_drinks_dict(drinks):
    drinks_dict = {}
    for drink in drinks:
        drinks_dict[drink["id"]] = Drink(drink["id"], drink["name"])
    return drinks_dict

def check_if_valid_command(command):
    valid_commands = ["get-people", "get-drinks", "get-preferences"]
    if command not in valid_commands:
        raise Exception("Command not found, type -h for list of commands") 

def main():
    file_man = File_Manager()
    accessor = Accessor(file_man)

    main_menu = MainMenu(accessor)
    main_menu.run()
   
if __name__ == "__main__":
    main()
    
