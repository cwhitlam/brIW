import unittest
import sys
sys.path.insert(1, "/home/chris/repos/miniproject/src/")
from person import Person
from drink import Drink

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.drink = Drink(0, "Coffee")
        self.person = Person(0, "Chris", self.drink)

    def test__init__(self):
        self.assertEqual(self.person.id, 0)
        self.assertEqual(self.person.name, "Chris")
        self.assertEqual(self.person.prefered_drink, self.drink)

    def test_set_drink(self):
        new_drink = Drink(1, "Tea")
        
        self.person.set_prefered_drink(new_drink)

        self.assertEqual(self.person.prefered_drink, new_drink)

    def test_get_json_representation(self):
        expected = {
            "id": 0,
            "name": "Chris",
            "prefered_drink_id": self.drink.id
        }  

        actual = self.person.get_json_representation()

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()