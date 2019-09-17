import sys
import unittest
sys.path.insert(1, "/home/chris/repos/miniproject/src/")
from person import Person
from drink import Drink
import briw 
from json_file_manager import File_Manager


class TestBriw(unittest.TestCase):
    
    def setUp(self):
        briw.people = {}
        briw.file_man = File_Manager()

    def test_add_person(self):
        drink    = Drink(0, "Coffee")  
        person   = Person(0, "Chris", drink)
        expected = {0: person}
        briw.add_person(person)

        self.assertDictEqual(briw.people, expected)
        self.assertEqual(person, briw.people[0])

if __name__ == "__main__":
    unittest.main()