import os
import sys
from ui import UI
import file_manager
from json_file_manager import File_Manager
from round import Round, Order
from person import Person
from drink import Drink
from menus import MainMenu
from accessor import Accessor

def change_preference():
    user_input = ""
    while user_input == "":
        user_input = get_user_number("Please enter the person's ID or press enter to display current preferences: ", True)
        if user_input == "":
            ui.display_preferences_table(people)

    person_id = int(user_input)
    user_input = ""
    while user_input == "":
        user_input = get_user_number("Please enter the drinks's ID or press enter to display current preferences: ", True)
        if user_input == "":
            ui.display_preferences_table(people)

    drink_id = int(user_input)
    prefered_drink = drinks[drink_id]
    people[person_id].set_prefered_drink(prefered_drink)

def preferences_menu():
    while True:
        ui.display_preferences_menu()
        user_choice = get_user_number("What would you like to do?: ")
        os.system("clear")
        if user_choice == 1:
            ui.display_preferences_table(people)
            ask_to_return_to_menu()
        elif user_choice == 2:
            change_preference()
            ask_to_return_to_menu()
        elif user_choice == 3:
            break
        else:
            ui.print_error_message("Please enter a valid option")

def create_new_round():
    ui.display_people_table(people)
    maker_id = get_user_number("Who is serving the round (please enter their id): ")
    maker = people[int(maker_id)]
    drinkers = []
    orders = []
    while True:
        person_id = get_user_number("Enter ID of drinker. Press enter when you want to stop: ", True)
        if person_id  == "":
            break
        person = people[int(person_id)]
        drinkers.append(person)
        user_input = input(f"{person.name} usually has {person.prefered_drink}. Continue with this drink? (Y/N): ")
        if user_input.upper() == "Y":
            order = Order(person, person.prefered_drink)
        elif user_input.upper() == "N":
            drink_id = input("Please enter the drink id: ")
            drink = drinks[drink_id]
            order = Order(person, drink)
        else:
            print()
        orders.append(order)
    current_round = Round(maker, orders)
    current_round.save_round(file_man)

def create_new_round_from_previous():
    round = file_man.load_from_file("./src/stored_data/round.json")
    maker = people[round["maker_id"]]
    orders = []
    for order in round["orders"]:
        person = people[order["person_id"]]
        drink  = drinks[order["drink_id"]]
        orders.append(Order(person, drink))
    current_round = Round(maker, orders)
    ui.display_current_round(current_round)

def show_current_round():
    if current_round == None:
        print ("Currently no round")
        return
    
    ui.display_current_round(current_round)

def rounds_menu():
    ui.display_rounds_menu()
    user_choice = get_user_number("What would you like to do?: ")
    os.system("clear")
    if user_choice == 1:
        create_new_round()
        ask_to_return_to_menu()
    if user_choice == 2:
        create_new_round_from_previous()
        ask_to_return_to_menu()
    if user_choice == 3:
        show_current_round()
        ask_to_return_to_menu()

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

def run_command(command):
    if command == "get-people":
        ui.display_people_table(people)
    elif command == "get-drinks":
        ui.display_drinks_table(drinks)
    elif command == "get-preferences":
        ui.display_preferences_table(people)        
 
def main():
    file_man = File_Manager()
    accessor = Accessor(file_man)

    if len(sys.argv) == 1:
        main_menu = MainMenu(accessor)
        main_menu.run()
    else:
        command = sys.argv[1]
        check_if_valid_command(command)
        run_command(command)
    
        
if __name__ == "__main__":
    main()
    