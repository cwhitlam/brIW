def get_all_people():
    return [
        {
            "person_id": 1,
            "first_name": "Chris",
            "surname": "Smoooth",
            "full_name": "Chris Smooth",
            "drink_id": 1,
            "drink_name": "Coffee"
        }
    ]

def get_all_drinks():
    return [
        {
            "drink_id": 1,
            "name": "Coffee"
        }
    ]

def add_new_person(first_name, surname, preferred_drink_id):
    return 

def add_new_drink(drink_name):
    return 

def update_drink_preference(person_id, drink_id):
    return

def get_person_by_id(person_id):
    return 1

def get_drink_by_id(drink_id):
    return 1

def create_round_with_orders(round):
    return

def create_orders(orders, round_id):
    return

def get_current_round():
    return {
            "maker_id": 1,
            "round_id": 1,
            "first_name": "Chris",
            "surname": "Smoooth",
            "expiry_datetime": "01-01-2020 00:00:00",
            "minutes_remaining": 10
        }

def get_num_of_orders_for_round(round_id):
    return 1

def get_current_rounds():
    return [
        {
            "maker_fullname": "Chris Smoooth",
            "round_id": 1,
            "expiry_datetime": "01-01-2020 00:00:00",
            "minutes_remaining": 10,
            "num_of_orders": 1
        }
    ]


def get_past_rounds(num_of_rounds):
    return [
        {
            "maker_fullname": "Chris Test",
            "round_id": 2,
            "expiry_datetime": "01-01-2019 00:00:00",
            "minutes_remaining": -10,
            "num_of_orders": 2
        }
    ]

   
def get_orders_by_round_id(round_id):
    return [
        {
            "person_id": 1,
            "first_name": "Chris",
            "surname": "Smoooth",
            "fullname": "Chris Smoooth",
            "drink_id": 1,
            "drink_name": "Coffee"   
        } 
    ]

def get_round_by_round_id(round_id):
    result = {
        "maker_fullname": "Chris Smoooth",
        "round_id": 1,
        "minutes_remaining": 10
    }

    result["orders"] = get_orders_by_round_id(result["round_id"])
    return result   

def create_round(maker_id, round_duration):
    return 