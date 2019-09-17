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
        self.assertListEqual(list(self.drinks.values()), list(table.table_contents))

    def test__init__with_list(self):
        table_title = "People"

        coffee = Drink(0, "Coffee")
        tea    = Drink(1, "Tea")

        drinks = [coffee, tea]

        table = Table("People", ["id", "name"], drinks)

        self.assertEqual(table_title.upper(), table.table_title)
        self.assertListEqual(drinks, table.table_contents)
"""
    def test_calculate_table_width(self):
        
        table = Table("Drinks", ["id", "name"], drinks)
        table._calculate_table_width()

    def test_calculate_column_widths(self):
"""

if __name__ == "__main__":
    unittest.main()