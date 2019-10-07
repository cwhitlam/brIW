from flask import Flask, request, Response
from src.api.request_handlers import PersonHandler, DrinkHandler, RoundHandler, OrderHandler
app = Flask(__name__)

@app.route('/people', methods=["GET", "POST", "PATCH"])
def people():
    handler = PersonHandler()
    if request.method == "GET":
        return handler.get()
    elif request.method == "POST":
        content = request.json
        try:
            handler.post(content)
            return Response(status=201)
        except Exception as e:
            print(e)
            return Response(status=422)
    elif request.method == "PATCH":
        content = request.json
        try:
            handler.patch(content)
            return Response(status=201)
        except Exception as e:
            print(e)
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
            handler.post(content)
            return Response(status=201)
        except Exception as e:
            print(e)
            return Response(status=422)
    else:
        return "Invalid HTTP method"

@app.route('/rounds', methods=["GET", "POST"])
def rounds():
    handler = RoundHandler()
    if request.method == "GET":
        return handler.get()
    elif request.method == "POST":
        content = request.json
        try:
            handler.post(content)
            return Response(status=201)
        except Exception as e:
            print(e)
            return Response(status=422)
    else:
        return "Invalid HTTP method"

@app.route('/rounds/<int:round_id>/orders', methods=["GET", "POST"])
def orders(round_id):
    handler = OrderHandler()
    if request.method == "GET":
        return handler.get(round_id)
    elif request.method == "POST":
        content = request.json
        try:
            handler.post(round_id, content)
            return Response(status=201)
        except Exception as e:
            print(e)
            return Response(status=422)
    else:
        return "Invalid HTTP method"


   
if __name__ == "__main__":
    host="0.0.0.0"
    port="8081"

    app.run(host=host, port=port, debug=True)