from flask import Flask, request, Response, json
from src.api.request_handlers import PersonHandler, DrinkHandler, RoundHandler, OrderHandler
app = Flask(__name__)

@app.route('/people', methods=["GET", "POST", "PATCH"])
def people():
    handler = PersonHandler()
    if request.method == "GET":
        data = handler.get()
        response = app.response_class(
            response=data,
            status=200,
            mimetype="application/json"
        )
        return response

    elif request.method == "POST":
        try:
            content = request.json
            handler.post(content)
            return Response(status=201)

        except Exception as e:
            print(e)
            return Response(status=422)

    elif request.method == "PATCH":
        try:
            content = request.json
            handler.patch(content)
            return Response(status=200)

        except Exception as e:
            print(e)
            return Response(status=422)
    else:
        return "Invalid HTTP method"

@app.route('/drinks', methods=["GET", "POST"])
def drinks():
    handler = DrinkHandler()
    if request.method == "GET":
        data = handler.get()
        response = app.response_class(
            response=data,
            status=200,
            mimetype="application/json"
        )
        return response

    elif request.method == "POST":
        try:
            content = request.json
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
        data = handler.get()
        response = app.response_class(
            response=data,
            status=200,
            mimetype="application/json"
        )
        return response

    elif request.method == "POST":
        try:
            content = request.json
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
        data = handler.get(round_id)
        response = app.response_class(
            response=data,
            status=200,
            mimetype="application/json"
        )
        return response

    elif request.method == "POST":
        try:
            content = request.json
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