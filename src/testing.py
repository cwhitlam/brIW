from file_manager import File_Manager

file_man = File_Manager()

people = file_man.load_from_file("./src/stored_data/people.json")
print(people)