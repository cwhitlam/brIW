import unittest
import unittest.mock
from src.api.app import app
import json
import tempfile
import os
from src.core.person import Person
from src.core.drink import Drink

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.content_type = "application/json"     
        self.client = app.test_client()

    @unittest.mock.patch("src.api.request_handlers.PersonHandler.get")
    def test_people_GET(self, get):
        response = app.test_client().get("/people")
        get.assert_called_once_with()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, self.content_type)
    
    @unittest.mock.patch("src.api.request_handlers.PersonHandler.post")
    def test_people_POST(self, post):
        payload = {
            "first_name": "John",
            "surname": "Smith",
            "preferred_drink_id": 1
        }
      
        response = self.client.post(
            "/people",
            data = json.dumps(payload),
            content_type=self.content_type
        )
        
        post.assert_called_once_with(payload)
        self.assertEqual(response.status_code, 201)

    @unittest.mock.patch("src.api.request_handlers.PersonHandler.patch")
    def test_people_PATCH(self, post):
        payload = {
            "person_id": 1,
            "preferred_drink_id": 1
        }
      
        response = self.client.patch(
            "/people",
            data = json.dumps(payload),
            content_type=self.content_type
        )
        
        post.assert_called_once_with(payload)
        self.assertEqual(response.status_code, 200)

    @unittest.mock.patch("src.core.db.add_new_person")
    def test_person_integration_POST(self, add_new_person):
        payload = {
            "first_name": "John",
            "surname": "Smith",
            "preferred_drink_id": 1
        }
      
        response = self.client.post(
            "/people",
            data = json.dumps(payload),
            content_type=self.content_type
        )

        add_new_person.assert_called_once_with("John", "Smith", 1)
        self.assertEqual(response.status_code, 201)

    @unittest.mock.patch("src.core.accessor.Accessor.get_people")
    def test_person_integration_GET(self, get_people):
        payload = {
            "first_name": "John",
            "surname": "Smith",
            "preferred_drink_id": 1
        }

        drink = Drink(1, "Coffee")
        person = Person(1, "John", "Smith", drink)

        get_people.return_value = [person]

        response = self.client.get(
            "/people",
            data = json.dumps(payload),
            content_type=self.content_type
        )
        self.assertEqual(response.status_code, 200)

    @unittest.mock.patch("src.api.request_handlers.DrinkHandler.get")
    def test_drink_GET(self, get):
        response = app.test_client().get("/drinks")
        get.assert_called_once_with()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, self.content_type)
    
    @unittest.mock.patch("src.api.request_handlers.DrinkHandler.post")
    def test_drink_POST(self, post):
        payload = {
            "drink_name": "Coffee"
        }
      
        response = self.client.post(
            "/drinks",
            data = json.dumps(payload),
            content_type=self.content_type
        )
        
        post.assert_called_once_with(payload)
        self.assertEqual(response.status_code, 201)

    @unittest.mock.patch("src.api.request_handlers.RoundHandler.get")
    def test_round_GET(self, get):
        response = app.test_client().get("/rounds")
        get.assert_called_once_with()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, self.content_type)
    
    @unittest.mock.patch("src.api.request_handlers.RoundHandler.post")
    def test_round_POST(self, post):
        payload = {
            "maker_id": 1,
            "round_duration": 30
        }
      
        response = self.client.post(
            "/rounds",
            data = json.dumps(payload),
            content_type=self.content_type
        )
        
        post.assert_called_once_with(payload)
        self.assertEqual(response.status_code, 201)

    

if __name__ == "__main__":
    unittest.main()