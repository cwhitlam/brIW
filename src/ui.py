from table import Table

class UI:
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
        table = Table("CURRENT ROUND STARTED BY: " + current_round.maker.name, ["person", "drink"], current_round.orders)
        table.print_table()