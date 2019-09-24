from http.server import HTTPServer 
from src.api.person_handler import PersonHandler

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, PersonHandler)
    print("Starting server...")
    httpd.serve_forever()
