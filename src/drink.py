class Drink():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.name

    def get_json_representation(self):
        return [self.id, self.name]