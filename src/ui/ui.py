from src.ui.table import Table

class UI:
    def __init__(self, accessor):
        self.accessor = accessor

    def display_people_table(self):
        table = Table("PEOPLE", ["id", "name"], self.accessor.get_people())
        table.print_table()

    def display_drinks_table(self):
        table = Table("DRINKS", ["id", "name"], self.accessor.get_drinks(), ["id", "drink"])
        table.print_table()
    
    def display_preferences_table(self):
        table = Table("PREFERENCES", ["name", "prefered_drink"], self.accessor.get_people(), ["name", "prefered_drink"])
        table.print_table()

    def display_current_round(self):
        current_round = self.accessor.get_current_round()
        if current_round == None:
            print ("Currently no round")
            return

        table = Table("CURRENT ROUND STARTED BY: " + current_round.maker.name, ["person", "drink"], current_round.orders)
        table.print_table()