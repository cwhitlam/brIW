import time
from json_file_manager import File_Manager
class Round:
    def __init__(self, maker, orders = []):
        self.maker  = maker
        self.orders = orders
        self.creation_time = time.clock 

    def display_round_orders(self):
        print(self.orders) 

    def save_order(self):
        fm = File_Manager()
        fm.save_to_file(self.orders, "src/stored_data/round.json")
        #fm.order_list_to_text(self.orders, "src/stored_data/round.txt")

class Order:
    def __init__(self, person, drink):
        self.person = person
        self.drink  = drink
    