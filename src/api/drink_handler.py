import src.core.db as database
import json
from src.core.accessor import Accessor
from src.api.encoder import MyEncoder

class DrinkHandler():
    def get(self):
        acc = Accessor()
        people = acc.get_drinks()
        json_encoded = json.dumps(people, cls=MyEncoder)
        return json_encoded

    def post(self, data):
        print(data)
        database.add_new_drink(data["name"])