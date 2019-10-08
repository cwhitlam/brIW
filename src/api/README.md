# BrIW API

## Setup
```bash
workon briw
cd ~/repos/miniproject
python3 -m src.api.app
```

## /people
### GET
Returns all the people stored in the database along with their prefered drink. 
```bash
curl localhost:8081/people | jq
```

### POST
Used to add a new person to the database

Data is expected in the following JSON format:

```json
{
    "first_name": "John",
    "surname": "Smith",
    "preferred_drink_id": "1"
}
```

So the full request would be:

```bash
curl -X POST localhost:8081/people -H "Content-Type: application/json" -d '{"first_name": "John", "surname": "Smith", "preferred_drink_id": "1"}'
```

### PATCH
Used to update a person's drink preference. Data passed is expected in the following JSON format:

```json
{
    "person_id": 1,
    "preferred_drink_id": 2
}
```

An example request would be:
```bash
curl -X PATCH localhost:8081/people -H "Content-Type: application/json" -d '{"person_id": 1, "preferred_drink_id": 2}'
```

## /drinks
### GET
Returns a list of all the drinks in the database
```bash
curl localhost:8081/drinks
```
### POST
Used to add a drink to the database. Data is expected in the following JSON format:

```json
{
    "drink_name": "Mocha"
}
```

An example request would be:

```bash
curl -X POST localhost:8081/drinks -H "Content-Type: application/json" -d '{"drink_name": "Mocha"}'
```

## /rounds
### GET
Used to get a list of all currently unexpired rounds and their orders
```
curl localhost:8081/rounds
```

### POST
Creates a new round without any orders

JSON request data is expected in the following format:

```json
{
    "maker_id": 1,
    "round_duration": 30
}
```

A full request would look like this:

```bash
curl -X POST localhost:8081/rounds -H "Content-Type: application/json" -d '{"maker_id": 1, "round_duration" 30}'

```

## /rounds/\<int:round_id\>/orders
### GET
Gets all the orders assigned to the round with id given by \<int:round_id\>

```bash
curl localhost:8081/rounds/18/orders
```

### POST
Used to add an order to a round.

JSON request data is expected in the following format:

```json
{
    "person_id": 1,
    "drink_id": 2,
    "special_requests": "2 sugars"
}
```