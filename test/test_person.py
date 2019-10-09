import unittest
import sys
sys.path.insert(1, "/home/chris/repos/miniproject/src/")
from src.core.person import Person
from src.core.drink import Drink

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.drink = Drink(0, "Coffee")
        self.person = Person(0, "Chris", "Smith", self.drink)

    def test__init__(self):
        self.assertEqual(self.person.id, 0)
        self.assertEqual(self.person.first_name, "Chris")
        self.assertEqual(self.person.surname, "Smith")
        self.assertEqual(self.person.full_name, "Chris Smith")
        self.assertIsInstance(self.person.prefered_drink, Drink)
        self.assertEqual(self.person.prefered_drink, self.drink)

if __name__ == "__main__":
    unittest.main()