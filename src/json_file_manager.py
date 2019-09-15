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

    def save_to_file_w_encoder(self, data, encoder, file_path):
        try:
            file = open(file_path, "w")
        except Exception as e:
            print(f"{e}: Couldn't save to file {file_path}")
        json_string = json.dumps(data, cls=PersonEncoder)
        file.write(json_string)
        """
        drink_encoder = DrinkEncoder()
        encoded_drink = drink_encoder.encode(data[0].prefered_drink)
        data[0].prefered_drink = encoded_drink
        encoded = encoder.encode(data[0])
        json.dump(encoded, file)
        """
    
    def load_from_file(self, file_path):
        try:
            file = open(file_path, "r")
        except Exception as e:
            print(e)
            return {}
        return json.load(file)

    def order_list_to_text(self, data, file_path):
        try:
            file = open(file_path, "w")
        except Exception as e:
            print(f"{e}: Couldn't save to file {file_path}")
        for order_object in data:
            person_id = order_object.person.id
            drink_id = order_object.drink.id
            line = str(person_id) + "," + str(drink_id) + "\n"
            file.write(line)
