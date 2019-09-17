import unittest
import sys
sys.path.insert(1, "/home/chris/repos/miniproject/src/")
from drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink(0, "Coffee")

    def test__init__(self):
        self.assertEqual(self.drink.id, 0)
        self.assertEqual(self.drink.name, "Coffee")

    def test_get_json_representation(self):
        expected = {
            "id": 0,
            "name": "Coffee"
        }

        actual = self.drink.get_json_representation()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()