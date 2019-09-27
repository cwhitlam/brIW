import src.core.db as database
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.core.person import Person
import json
from src.core.accessor import Accessor
from src.api.encoder import MyEncoder

class PersonHandler():
    def get(self):
        acc = Accessor()
        people = acc.get_people()
        json_encoded = json.dumps(people, cls=MyEncoder)
        return json_encoded

    def post(self, data):
        database.add_new_person(
            data["first_name"], 
            data["surname"],
            data["preferred_drink_id"]
        )      

        

