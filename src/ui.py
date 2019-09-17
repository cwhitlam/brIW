from table import Table
from colours import Colours
class UI:
    def __init__(self):
        self.colours = Colours()

    def display_main_menu(self):
        menu_text = """
    Please select an option:

        [1] Manage People
        [2] Manage Drinks
        [3] Manage Preferences
        [4] Manage Rounds
        [5] Exit
        """
        print(menu_text)

    def display_people_menu(self):
        menu_text = """
    Please select an option:

        [1] List people
        [2] Add people
        [3] Return to main menu

        """
        print(menu_text)

    def display_drinks_menu(self):
        menu_text = """
    Please select an option:

        [1] List drinks
        [2] Add drinks
        [3] Return to main menu

        """
        print(menu_text)

    def display_preferences_menu(self):
        menu_text = """
    Please select an option:

        [1] Display preferences
        [2] Add person's preferences
        [3] Return to main menu   
        """
        print(menu_text)

    def display_rounds_menu(self):
        menu_text = """
    Please select an option:

        [1] Create a round
        [2] Create round from previous round
        [3] Display current round
        [4] Exit
        """
        print(menu_text)

    def display_people_table(self, people):
        table = Table("PEOPLE", ["id", "name"], people)
        table.print_table()

    def display_drinks_table(self, drinks):
        table = Table("DRINKS", ["id", "name"], drinks, ["id", "drink"])
        table.print_table()
    
    def display_preferences_table(self, people):
        table = Table("PREFERENCES", ["name", "prefered_drink"], people, ["name", "prefered_drink"])
        table.print_table()

    def display_current_round(self, current_round):
        table = Table("ROUND STARTED BY: " + current_round.maker.name, ["person", "drink"], current_round.orders)
        table.print_table()

    def print_error_message(self, message):
        print(self.colours.ERROR + message + self.colours.ENDC)
