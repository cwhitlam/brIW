from flask import Flask, request, Response
from src.api.person_handler import PersonHandler
from src.api.drink_handler import DrinkHandler
app = Flask(__name__)

@app.route('/people', methods=["GET", "POST"])
def people():
    handler = PersonHandler()
    if request.method == "GET":
        return handler.get()
    elif request.method == "POST":
        content = request.json
        try:
            post(content)
            return Response(status=201)
        except Exception as e:
            return Response(status=422)
    else:
        return "Invalid HTTP method"

@app.route('/drinks', methods=["GET", "POST"])
def drinks():
    handler = DrinkHandler()
    if request.method == "GET":
        return handler.get()
    elif request.method == "POST":
        content = request.json
        try:
            post(content)
            return Response(status=201)
        except Exception as e:
            return Response(status=422)
    else:
        return "Invalid HTTP method"


if __name__ == "__main__":
    host="0.0.0.0"
    port="8000"

    app.run(host=host, port=port, debug=True)