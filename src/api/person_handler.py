import src.core.db as database
from http.server import BaseHTTPRequestHandler
from src.core.person import Person
import json
from src.core.accessor import Accessor
from src.api.encoder import MyEncoder

class PersonHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        acc = Accessor()
        people = acc.get_people_dict()
        json_encoded = json.dumps(people, cls=MyEncoder)
        self.wfile.write(json_encoded.encode("utf-8"))

