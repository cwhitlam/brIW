import json

class File_Manager:
    def convert_to_json(self, data):
        array = []
        for entry in data.values():
            array.append(entry.get_json_representation())
        return array

    def save_to_file(self, data, file_path):
        try:
            file = open(file_path, "w")
            json.dump(data, file)
        except Exception as e:
            print(f"{e}: Couldn't save to file {file_path}")
   
    def load_from_file(self, file_path):
        try:
            file = open(file_path, "r")
        except Exception as e:
            print(e)
            return {}
        return json.load(file)