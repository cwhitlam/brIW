import unittest
import sys
from src.core.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink(0, "Coffee")

    def test__init__(self):
        self.assertEqual(self.drink.id, 0)
        self.assertEqual(self.drink.name, "Coffee")

if __name__ == "__main__":
    unittest.main()