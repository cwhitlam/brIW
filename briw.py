import os
import sys
from src.ui.ui import UI
from src.json_file_manager import File_Manager
from src.core.round import Round, Order
from src.core.person import Person
from src.core.drink import Drink
from src.menus import MainMenu
from src.core.accessor import Accessor

def main():
    file_man = File_Manager()
    accessor = Accessor(file_man)

    main_menu = MainMenu(accessor)
    main_menu.run()
   
if __name__ == "__main__":
    main()
    
