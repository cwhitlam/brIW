import src.core.db as database
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.core.round import Round, Order
import json
from src.core.accessor import Accessor
from src.api.encoder import MyEncoder

class RoundHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        acc = Accessor()
        round = acc.get_current_round()
        json_encoded = json.dumps(round, cls=MyEncoder)
        self.wfile.write(json_encoded.encode("utf-8"))
        
    def do_POST(self):
        acc = Accessor()
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        
        orders = []
        for order in data["orders"]:
            person, preferred_drink = acc.get_person(order["person_id"])
            drink  = acc.get_drink(order["drink_id"])
            order_obj = Order(person, drink)
            orders.append(order_obj)
        
        maker, preferred_drink = acc.get_person(data["maker_id"])
        print(orders)
        round = Round(maker, data["round_duration"], orders)
        
        database.create_round_with_orders(round)       
        
        self.send_response(201)
        self.end_headers()

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, RoundHandler)
    print("Starting round server...")
    httpd.serve_forever()
