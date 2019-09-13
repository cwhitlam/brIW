import os
import sys
from ui import UI
import file_manager
from json_file_manager import File_Manager
from rounds import Round, Order
from person import Person
from drink import Drink
from encoders import PersonEncoder

def get_new_id(table):
    current_highest_id = list(table.keys())[-1]
    return current_highest_id + 1

def add_to_table(table, row_to_add):
    id = get_new_id(people)
    row_to_add = row_to_add.capitalize()
    table[id] = row_to_add
    
def ask_to_return_to_menu():
    user_input = input("Return to main menu? (Y/N): ")
    while user_input.upper() != "Y" and user_input.upper() != "N":
        user_input = input("Please enter either Y or N: ").upper()
    if user_input.upper() == "N":
        exit_program()
    os.system("clear")
def santitize_user_string(user_input):
    valid_user_input = user_input.isalpha()
    while not valid_user_input:
        user_input = input("Please enter a valid string: ")
        valid_user_input = user_input.isalpha() 
    return str(user_input)

def sanitize_user_number(user_input):
    valid_user_input = user_input.isdigit()
    while not valid_user_input:
        user_input = input("Please enter a number: ")
        valid_user_input = user_input.isdigit() 
    return int(user_input)

def exit_program():
    print("Exiting program...")
    exit()

def add_person_menu():
    user_input = input("Who would you like to add?: ")
    person_name = santitize_user_string(user_input)
    person_name = person_name.capitalize()
    user_input = input("What is the id of thier prefered drink? (leave blank if no preferece): ")
    prefered_drink = None
    if user_input != "":
        drink_id = sanitize_user_number(user_input)
        prefered_drink = drinks[drink_id]
    person_id = get_new_id(people)
    person = Person(person_id, person_name, prefered_drink)
    people[person_id] = person
    file_man = File_Manager()

    file_man.save_to_file(people, "src/stored_data/bork.json")
    """
    json_people = []
    for person in people.values():
        drink_id = person.prefered_drink.id
        dic = {"id": person.id, "name": person.name, "prefered_drink_id": drink_id}
        json_people.append(dic)
    file_man.save_to_file(json_people, "./src/stored_data/bork.json")
    """
    print(f"{person_name} was successfully added")

def add_drink():
    not_valid_drink = True
    while not_valid_drink:
        user_input = input("What drink would you like to add?: ")
        drink = santitize_user_string(user_input)
        drink = drink.capitalize()
        if drink not in drinks.values():
            not_valid_drink = False
        else:
            print("Drink already in database, please enter a different drink or use the existing one")
        add_to_table(drinks, drink)
        file_manager.save_data_to_file("./stored_data/drinks.txt", drinks)
        print(f"{drink} was successfully added")

def people_menu():
    ui.display_people_menu()
    user_input = input("What would you like to do?: ")
    user_choice = sanitize_user_number(user_input)
    os.system("clear")
    if user_choice == 1:
        ui.display_people_table(people)
    elif user_choice == 2:
        add_person_menu()        
    elif user_choice == 3:
        print("Not Implemented")
    
def drinks_menu():
    ui.display_drinks_menu()
    user_input = input("What would you like to do?: ")
    user_choice = sanitize_user_number(user_input)
    os.system("clear")
    if user_choice == 1:
        ui.display_drinks_table(drinks)
    elif user_choice == 2:
    elif user_choice == 3:
        print("Not Implemented")

def get_person_name_by_id(id):
    try:
        return people[id]
    except:
        print(f"No person has the id {id}")
        quit()

def get_drink_name_by_id(id):
    try:
        return drinks[id]
    except:
        print(f"No drink with id: {id}")
        quit() 
   
def add_new_preference():
    user_input = ""
    while user_input == "":
        user_input = input("Please enter the person's ID or press enter to display current preferences: ")
        if user_input == "":
            ui.display_preferences_table(people)

    person_id = int(user_input)
    user_input = ""
    while user_input == "":
        user_input = input("Please enter the drinks's ID or press enter to display current preferences: ")
        if user_input == "":
            ui.display_preferences_table(people)

    drink_id = int(user_input)
    prefered_drink = drinks[drink_id]
    people[person_id].set_prefered_drink(prefered_drink)

def preferences_menu():
    ui.display_preferences_menu()
    user_input = input("What would you like to do?: ")
    user_choice = sanitize_user_number(user_input)
    os.system("clear")
    if user_choice == 1:
        ui.display_preferences_table(people)
    elif user_choice == 2:
        add_new_preference()

def create_round():
    ui.display_people_table(people)
    maker_id = input("Please enter your user id: ")
    drinkers = []
    orders = []
    while True:
        person_id = input("Enter ID of drinker. ")
        if person_id == "":
            break
        drinkers.append(people[int(person_id)])
    for person in drinkers:
        order = Order(person, person.prefered_drink)
        orders.append(order)
    round = Round(maker_id, orders)
    round.save_order()

def rounds_menu():
    ui.display_rounds_menu()
    user_input = input("What would you like to do?: ")
    user_choice = sanitize_user_number(user_input)
    os.system("clear")
    if user_choice == 1:
        create_round()

def create_people_dict(people, drinks):
    people_dict = {}
    for person in people:
        prefered_drink = drinks[person["prefered_drink_id"]]
        people_dict[person["id"]] = Person(person["id"], person["name"], prefered_drink)
    return people_dict

def create_drinks_dict(drinks):
    drinks_dict = {}
    for drink in drinks:
        drinks_dict[drink["id"]] = Drink(drink["id"], drink["name"])
    return drinks_dict

def initialize():
    global drinks
    global people
    global preferences
    global ui

    ui = UI()
    file_man = File_Manager()
    drinks = file_man.load_from_file("./src/stored_data/drinks.json")
    drinks = create_drinks_dict(drinks)
    people = file_man.load_from_file("./src/stored_data/people.json")
    people = create_people_dict(people, drinks)

def main_menu():
    print("\nWelcome to BrIW v0.1")
    while True:
        ui.display_main_menu()
        user_input = input("What would you like to do?: ")
        user_choice = sanitize_user_number(user_input)
        os.system("clear")
        if user_choice == 1:
            people_menu()
            ask_to_return_to_menu()
        elif user_choice == 2:
            drinks_menu()
            ask_to_return_to_menu()
        elif user_choice == 3:
            preferences_menu()
            ask_to_return_to_menu()
        elif user_choice == 4:
            rounds_menu()
            ask_to_return_to_menu()
        elif user_choice == 5:
            exit_program()
        else:
            print("Please enter one of the options")

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
    initialize()
    if len(sys.argv) == 1:  
        main_menu()
    else:
        command = sys.argv[1]
        check_if_valid_command(command)
        run_command(command)
    
        
if __name__ == "__main__":
    main()