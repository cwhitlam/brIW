from json import JSONEncoder
from person import Person
from drink import Drink

class PersonEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Person) or isinstance(object, Drink):
            #return object.get_json_state()
            return object.__dict__

        else:
            # call base class implementation which takes care of

            # raising exceptions for unsupported types

            return JSONEncoder.default(self, object)

class DrinkEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Drink):
            #return object.get_json_state()
            return object.__dict__

        else:
            # call base class implementation which takes care of

            # raising exceptions for unsupported types

            return JSONEncoder.default(self, object)


 

 