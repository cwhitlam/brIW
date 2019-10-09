import unittest
from src.core.round import Round, Order
from src.core.person import Person
from src.core.drink import Drink

class TestRound(unittest.TestCase):
    def setUp(self):
        drink_pref = Drink(1, "Coffee")
        self.maker = Person(1, "Chris", "Smith", drink_pref)
        self.round_duration = 30
        person = Person(2, "Bob", "Bobson", drink_pref)
        drink_order = Drink(2, "Tea")
        order = Order (
           person,
           drink_order 
        )
        self.orders = [
            order
        ]
        self.round = Round(self.maker, self.round_duration, self.orders)

    def test__init__(self):
        self.assertIsInstance(self.round, Round)
        self.assertEqual(self.round.orders, self.orders)
        self.assertEqual(self.round.maker, self.maker)
        self.assertEqual(self.round.minutes_remaining, self.round_duration)

if __name__ == "__main__":
    unittest.main()