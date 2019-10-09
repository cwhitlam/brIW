class Round:
    def __init__(self, maker, round_duration, orders = []):
        self.maker  = maker
        self.orders = orders
        self.minutes_remaining = round_duration

class Order:
    def __init__(self, person, drink, special_requests = ""):
        self.person = person
        self.drink  = drink
        self.special_requests = special_requests
    