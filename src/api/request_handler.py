from flask import Flask, request
from src.api.person_handler import PersonHandler
app = Flask(__name__)

@app.route('/people', methods=["GET", "POST"])
def people_route():
    person_handler = PersonHandler()
    if request.method == "GET":
        return person_handler.get()
    elif request.method == "POST":
        return person_handler.post(request.data)
    else:
        return "Invalid HTTP method"

if __name__ == "__main__":
    host="localhost"
    port="8000"

    app.run(host=host, port=port)