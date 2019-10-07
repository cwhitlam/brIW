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