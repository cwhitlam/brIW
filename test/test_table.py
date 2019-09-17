import sys
import unittest
sys.path.insert(1, "/home/chris/repos/miniproject/src/")
from table import Table
from drink import Drink

class TestTable(unittest.TestCase):

    def setUp(self):
        coffee = Drink(0, "Coffee")
        tea    = Drink(1, "Tea")

        self.drinks = {
            "0": coffee,
            "1": tea
        }

    def test__init__with_dict(self):
        table_title = "People"

        table = Table("People", ["id", "name"], self.drinks)

        self.assertEqual(table_title.upper(), table.table_title)
        self.assertEqual(self.drinks.values(), table.table_contents)

"""
    def test__init__with_list(self):

    def test_calculate_table_width(self):


    def test_calculate_column_widths(self):
"""

if __name__ == "__main__":
    unittest.main()