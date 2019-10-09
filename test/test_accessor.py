import unittest
import unittest.mock
import sys
from src.core.accessor import Accessor
from src.core.person import Person
from src.core.drink import Drink
from src.core.round import Round, Order

class TestAccessor(unittest.TestCase):

    def setUp(self):
        self.acc = Accessor()

    @unittest.mock.patch("src.core.db.get_all_people")
    def test_get_people(self, get_all_people):
        #Arrange
        get_all_people.return_value = [
            {
                "person_id": 1,
                "first_name": "Chris",
                "surname": "Smith",
                "drink_id": 1,
                "drink_name": "Coffee"
            }
        ]
        
        #Act
        result = self.acc.get_people()

        #Assert
        for person in result.values():
            self.assertIsInstance(person, Person)
            self.assertEqual(person.id, 1)
            self.assertEqual(person.first_name, "Chris")
            self.assertEqual(person.surname, "Smith")
            self.assertIsInstance(person.prefered_drink, Drink)
            self.assertEqual(person.prefered_drink.id, 1)
            self.assertEqual(person.prefered_drink.name, "Coffee")

    @unittest.mock.patch("src.core.db.get_all_drinks")
    def test_get_drinks(self, get_all_drinks):
        #Arrange
        get_all_drinks.return_value = [
            {
                "drink_id": 1,
                "name": "Coffee",
            }
        ]
        
        #Act
        result = self.acc.get_drinks()

        #Assert
        for drink in result.values():
            self.assertIsInstance(drink, Drink)
            self.assertEqual(drink.id, 1)
            self.assertEqual(drink.name, "Coffee")

    @unittest.mock.patch("src.core.db.get_drink_preference_by_person_id")
    @unittest.mock.patch("src.core.db.get_orders_by_round_id")
    @unittest.mock.patch("src.core.db.get_current_rounds")
    def test_get_current_rounds(
        self, 
        get_current_rounds, 
        get_orders_by_round_id, 
        get_drink_preference_by_person_id):

        #Arrange
        get_current_rounds.return_value = [
            {
                "maker_id": 1,
                "first_name": "Chris",
                "surname": "Smith",
                "drink_name": "Coffee",
                "drink_id": 1,
                "maker_fullname": "Chris Smith",
                "round_id": 1,
                "expiry_datetime": "2019-01-01 12:00:00",
                "minutes_remaining": 30
            }
        ]

        get_orders_by_round_id.return_value = [
            {
                "order_id": 1,
                "person_id": 2,
                "first_name": "Bob",
                "surname": "Bobson",
                "fullname": "Bob Bobson",
                "drink_id": 2,
                "drink_name": "Tea",
                "special_request": "2 sugars"
            }
        ]

        get_drink_preference_by_person_id.return_value = {
            "drink_id": 1,
            "drink_name": "Coffee"
        }   

        #Act
        result = self.acc.get_current_rounds()

        #Assert
        for round in result.values():
            self.assertIsInstance(round, Round)
            self.assertIsInstance(round.maker, Person)
            self.assertIsInstance(round.maker.prefered_drink, Drink)
            self.assertIsInstance(round.orders[0], Order)
            self.assertIsInstance(round.orders[0].drink, Drink)
            self.assertIsInstance(round.orders[0].person, Person)
            self.assertEqual(round.orders[0].drink.id, 2)
            self.assertEqual(round.orders[0].drink.name, "Tea")
            self.assertEqual(round.minutes_remaining, 30)
  
    @unittest.mock.patch("src.core.db.get_drink_preference_by_person_id")
    @unittest.mock.patch("src.core.db.get_orders_by_round_id")
    def test_get_round_orders(
        self, get_orders_by_round_id, 
        get_drink_preference_by_person_id):
        #Arrange
        get_orders_by_round_id.return_value = [
            {
                "order_id": 1,
                "person_id": 2,
                "first_name": "Bob",
                "surname": "Bobson",
                "fullname": "Bob Bobson",
                "drink_id": 2,
                "drink_name": "Tea",
                "special_requests": "2 sugars"
            }
        ]

        get_drink_preference_by_person_id.return_value = {
            "drink_id": 1,
            "drink_name": "Coffee"
        }   

        #Act
        result = self.acc.get_round_orders(1)

        #Assert
        for order in result.values():
            self.assertIsInstance(order, Order)
            self.assertIsInstance(order.person, Person)
            self.assertIsInstance(order.drink, Drink)
            self.assertEqual(order.special_requests, "2 sugars")
            self.assertEqual(order.drink.id, 2)
            self.assertEqual(order.drink.name, "Tea")
            self.assertEqual(order.person.full_name, "Bob Bobson")
            self.assertEqual(order.person.id, 2)

if __name__ == "__main__":
    unittest.main()