import src.core.db as database
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.core.person import Person
import json
from src.core.accessor import Accessor
from src.api.encoder import MyEncoder

class DrinkHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        acc = Accessor()
        people = acc.get_drinks_dict()
        json_encoded = json.dumps(people, cls=MyEncoder)
        self.wfile.write(json_encoded.encode("utf-8"))
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))


        database.add_new_person(
            data["first_name"], 
            data["surname"],
            data["preferred_drink_id"]
        )       

        self.send_response(201)
        self.end_headers()

if __name__ == "__main__":
    #Drink Server
    server_address = ("", 8081)
    httpd = HTTPServer(server_address, DrinkHandler)
    print("Starting drink server...")
    httpd.serve_forever()
