import unittest
from src.core.round import Order
from src.core.person import Person
from src.core.drink import Drink

class TestOrder(unittest.TestCase):
    def setUp(self):
        drink_pref = Drink(1, "Coffee")
        self.person = Person(2, "Bob", "Bobson", drink_pref)
        self.drink_order = Drink(2, "Tea")
        self.order = Order(self.person, self.drink_order)

    def test__init__(self):
        self.assertIsInstance(self.order, Order)
        self.assertEqual(self.order.person, self.person)
        self.assertEqual(self.order.drink, self.drink_order)

if __name__ == "__main__":
    unittest.main()