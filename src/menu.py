import os

class Menu:
    def ask_to_return_to_menu(self):
        user_input = input("Return to previous menu? (Y/N): ")
        while user_input.upper() != "Y" and user_input.upper() != "N":
            user_input = input("Please enter either Y or N: ").upper()
        if user_input.upper() == "N":
            self.exit_program()
        os.system("clear")

    def santitize_user_string(self, user_input):
        valid_user_input = user_input.isalpha()
        while not valid_user_input:
            user_input = input("Please enter a valid string: ")
            valid_user_input = user_input.isalpha() 
        return str(user_input)

    def sanitize_user_number(self, user_input):
        valid_user_input = user_input.isdigit()
        while not valid_user_input:
            user_input = input("Please enter a number: ")
            valid_user_input = user_input.isdigit() 
        return int(user_input)

    def exit_program(self):
        print("Exiting program...")
        exit()

    def get_user_string(self, message):
        user_input = input(message)
        valid_user_input = user_input.isalpha()
        while not valid_user_input:
            user_input = input("Please enter a valid string: ")
            valid_user_input = user_input.isalpha() 
        return str(user_input)

    def get_user_number(self, message, allow_blank = False):
        user_input = input(message).strip()
        if user_input == "" and allow_blank:
            return user_input
        valid_user_input = user_input.isdigit()
        while not valid_user_input:
            user_input = input("Please enter a number: ").strip()
            if user_input == "" and allow_blank:
                return user_input
            valid_user_input = user_input.isdigit() 
        return int(user_input)
