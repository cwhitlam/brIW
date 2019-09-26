import os
from abc import ABC, ABCMeta, abstractmethod
from src.json_file_manager import File_Manager
from src.ui.table import Table
from src.core.person import Person
from src.core.drink import Drink
from src.core.round import Round, Order
from src.ui.ui import UI
import src.core.db as queries 

class AbstractMenu(ABC):
    @abstractmethod
    def __init__(self, accessor, file_man):
        self.accessor = accessor
        
        self.file_man = file_man
        self.ui = UI(self.accessor)

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def handle_menu_choice(self):
        pass

    def run(self):
        stay_on_menu = True
        while stay_on_menu:
            self.show_menu()
            user_choice = self.get_user_number("What would you like to do?: ")
            self.clear_terminal()
            stay_on_menu = self.handle_menu_choice(user_choice)

    def print_error_message(self, message):
        print("\033[91m" + message + "\033[0m")

    def clear_terminal(self):
        os.system("clear")

    def ask_to_return_to_menu(self):
        user_input = input("Return to previous menu? (Y/N): ")
        while user_input.upper() != "Y" and user_input.upper() != "N":
            user_input = input("Please enter either Y or N: ").upper()
        if user_input.upper() == "N":
            self.exit_program()
        os.system("clear")

    def exit_program(self):
        print("Exiting program...")
        exit()

    def get_user_string(self, message):
        user_input = input(message)
        valid_user_input = user_input.isalpha()
        while not valid_user_input:
            user_input = input("Please enter a valid string: ")
            valid_user_input = user_input.isalpha() 
        return str(user_input)

    def get_user_number(self, message, allow_blank = False):
        user_input = input(message).strip()
        if user_input == "" and allow_blank:
            return user_input
        valid_user_input = user_input.isdigit()
        while not valid_user_input:
            user_input = input("Please enter a number: ").strip()
            if user_input == "" and allow_blank:
                return user_input
            valid_user_input = user_input.isdigit() 
        return int(user_input)

class MainMenu(AbstractMenu):
    def __init__(self, accessor):
        super().__init__(accessor, None)

    def show_menu(self):
        menu_text = """
    Please select an option:

        [1] Manage People
        [2] Manage Drinks
        [3] Manage Preferences
        [4] Manage Rounds
        [5] Exit
        """
        print(menu_text)

    def handle_menu_choice(self, user_choice):
        sub_menu = MenuFactory.create(self, self.accessor, user_choice)
        sub_menu.run() 

    def run(self):
        print("\nWelcome to BrIW v0.1")
        while True:
            self.show_menu()
            user_choice = self.get_user_number("What would you like to do?: ")
            self.clear_terminal()
            self.handle_menu_choice(user_choice)

class PeopleMenu(AbstractMenu):
    def __init__(self, accessor, file_man):
        super().__init__(accessor, file_man)

    def add_person_menu(self):
        first_name = self.get_user_string("What is their first name?: ")
        first_name = first_name.capitalize()
        surname = self.get_user_string("What is their surname?: ")
        surname = surname.capitalize()
        drink_id = self.get_user_number("What is the id of thier prefered drink? (leave blank if no preference): ", True)
        queries.add_new_person(first_name, surname, drink_id)
        print(f"{first_name} {surname} was successfully added")

    def show_menu(self):
        menu_text = """
    Please select an option:

        [1] List people
        [2] Add people
        [3] Return to main menu

        """
        print(menu_text)

    def handle_menu_choice(self, user_choice):
        if user_choice == 1:
            self.ui.display_people_table()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 2:
            self.add_person_menu() 
            self.ask_to_return_to_menu()
            return True       
        elif user_choice == 3:
            return False        
        else:
            self.print_error_message("Please enter a valid option!")
            return True

class DrinksMenu(AbstractMenu):
    def __init__(self, accessor, file_man):
        super().__init__(accessor, file_man)

    def show_menu(self):
        menu_text = """
    Please select an option:

        [1] List drinks
        [2] Add drinks
        [3] Return to main menu

        """
        print(menu_text)

    def add_drink_menu(self):
        drink_name = self.get_user_string("What drink would you like to add?: ")
        drink_name = drink_name.capitalize()
        queries.add_new_drink(drink_name)
        print(f"{drink_name} was successfully added")

    def handle_menu_choice(self, user_choice):
        if user_choice == 1:
            self.ui.display_drinks_table()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 2:
            self.add_drink_menu()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 3:
            return False
        else:
            self.print_error_message("Please enter a valid option!")
            return True

class PreferencesMenu(AbstractMenu):
    def __init__(self, accessor, file_man):
        super().__init__(accessor, file_man)

    def show_menu(self):
        menu_text = """
    Please select an option:

        [1] Display preferences
        [2] Change someone's drink preference
        [3] Return to main menu   
        """
        print(menu_text)

    def change_preference(self):
        user_input = ""
        while user_input == "":
            user_input = self.get_user_number("Please enter the person's ID or press enter to display current preferences: ", True)
            if user_input == "":
                self.ui.display_preferences_table()

        person_id = int(user_input)
        user_input = ""
        while user_input == "":
            user_input = self.get_user_number("Please enter the drinks's ID or press enter to display current preferences: ", True)
            if user_input == "":
                self.ui.display_drinks_table()

        drink_id = int(user_input)
        queries.update_drink_preference(person_id, drink_id)
        print("Preference updated")

    def handle_menu_choice(self, user_choice):
        if user_choice == 1:
            self.ui.display_preferences_table()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 2:
            self.change_preference()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 3:
            return False
        else:
            self.print_error_message("Please enter a valid option")
            return True

class RoundMenu(AbstractMenu):
    def __init__(self, accessor, file_man):
        super().__init__(accessor, file_man)

    def show_menu(self):
        self.ui.display_current_round()
        menu_text = """
    Please select an option:

        [1] Create a round
        [2] Create round from previous round
        [3] Display current round
        [4] Return to main menu
        """
        print(menu_text)
    
    def create_new_round(self):
        self.ui.display_people_table()
        maker_id = self.get_user_number("Who is serving the round (please enter their id): ")
        maker, maker_drink = self.accessor.get_person(maker_id)
        round_duration = self.get_user_number("How long until you make the drinks (in minutes)?: ")
        orders = []
        while True:
            person_id = self.get_user_number("Enter ID of drinker. Press enter when you want to stop: ", True)
            if person_id  == "":
                break
            person, drink = self.accessor.get_person(person_id)
            user_input = input(f"{person.first_name} usually has {person.prefered_drink}. Continue with this drink? (Y/N): ")
            order = Order(person, person.prefered_drink)
            if user_input.upper() == "N":
                drink_id = input("Please enter the drink id: ")
                drink = self.accessor.get_drink(drink_id)
                order = Order(person, drink)
            orders.append(order)
        new_round = Round(maker, round_duration, orders)
        queries.create_round_with_orders(new_round)
        

    def create_new_round_from_previous(self):
        people = self.accessor.get_people()
        drinks = self.accessor.get_drinks()
        round = self.file_man.load_from_file("./src/stored_data/round.json")
        maker = people[round["maker_id"]]
        orders = []
        for order in round["orders"]:
            person = people[order["person_id"]]
            if order["drink_id"] in list(drinks.keys()):
                drink  = drinks[order["drink_id"]]
            else:
                drink = None
            orders.append(Order(person, drink))
        current_round = Round(maker, orders)
        self.accessor.set_current_round(current_round)
        self.ui.display_current_round()

    def handle_menu_choice(self, user_choice):
        if user_choice == 1:
            self.create_new_round()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 2:
            self.create_new_round_from_previous()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 3:
            self.ui.display_current_round()
            self.ask_to_return_to_menu()
            return True
        elif user_choice == 4:
            return False
        else:
            self.print_error_message("Please enter a valid option")
            return True
  
class MenuFactory:
    def create(self, accessor, key):
        file_man = File_Manager()
        sub_menu = {
            1: PeopleMenu(accessor, file_man),
            2: DrinksMenu(accessor, file_man),
            3: PreferencesMenu(accessor, file_man),
            4: RoundMenu(accessor, file_man)
        }

        if key == len(sub_menu) + 1:
            print("Exiting program...")
            exit()
        
        return sub_menu[key]
        