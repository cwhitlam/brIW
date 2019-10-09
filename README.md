# BrIW
## Prerequisites
This application assumes you already have the following installed:

- python3
- pip3
- virtualenv & virtualenvwrapper *(Recommended)*

## Setup
It's recommended that a new virtual environment is create for this application:
```
mkvirtualenv briw
workon briw
```
To install dependencies:
- Navigate to `miniproject` folder
- `pip3 install -r requirements.txt`

For GDPR reasons, you'll need to create `person.json` and `drinks.json` files in the `src/stored_data/` folder. The contents of both files should be the following:
`[]`

## Run
- Navigate to the `miniproject` directory
- run `python3 briw.py`

## Contributing
To contribute you can fork the repository and make any changes. Make sure you run all tests.  

To run tests navigate to the project directory and run:
```
python3 -m test.run_tests
```

Test coverage can be checked with where <user> is your user:
```
coverage report -m --omit="/home/<user>/.*"
```