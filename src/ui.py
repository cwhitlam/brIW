from table import Table
class UI:
    def __init__(self):
        pass

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
        [3] Remove people
        [4] Return to main menu

        """
        print(menu_text)

    def display_drinks_menu(self):
        menu_text = """
    Please select an option:

        [1] List drinks
        [2] Add drinks
        [3] Remove drinks
        [4] Return to main menu

        """
        print(menu_text)

    def display_preferences_menu(self):
        menu_text = """
    Please select an option:

        [1] Display preferences
        [2] Add person's preferences
        [3] Exit   
        """
        print(menu_text)

    def display_rounds_menu(self):
        menu_text = """
    Please select an option:

        [1] Create a round
        [2] Cancel a round
        [3] Exit
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