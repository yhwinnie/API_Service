#from flask import json
import app as server
import unittest
import requests
import json

class FlaskServerTest(unittest.TestCase):
    # Has to be implemented
    def setUp(self):
        # Run app in testing mode to retrieve exceptions and stack traces
        # Unfold stack traces
        server.app.testing = True
        # Make an instance of server to make it accessible to other methods
        self.app = server.app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        assert response.status_code == 200, "status_code was not OK"
        #assert response.content_type == "application/json"
        #reponse_data = json.loads(response.data)
        assert response.data == "Hello, world"


    def test_hello_to_person(self):
        response = self.app.get('/hello/Julia')
        assert response.data == "Hello, Julia!"

    def test_post_pets(self):
        pet_dictionary = {'name': 'Pluto','age': '3','species': 'dog'}
        pet_json_string = json.dumps(pet_dictionary)
        # response = requests.post('http://0.0.0.0:5000/pets',
        #                  data=pet_json_string)
        response = self.app.post('/pets', data=pet_json_string, content_type='application/json')
        # response = self.app.get('/pets')
        assert response.status_code == 200
        response_dict = json.loads(response.data)
        self.assertEqual(response_dict, pet_dictionary)

        response = self.app.post('/pets', data=pet_json_string, content_type='application/json')
        response_dict = json.loads(response.data)

        assert response_dict == {"HTTP status": "409", "message": "Pet name already exists"}

        pet_dictionary = {'name': 'Pluto','age': '3','speci': 'dog'}
        pet_json_string = json.dumps(pet_dictionary)
        response = self.app.post('/pets', data=pet_json_string, content_type='application/json')
        response_dict = json.loads(response.data)
        assert response_dict == {"HTTP status": "400", "message": "key not find"}

        pet_dictionary = None
        pet_json_string = json.dumps(pet_dictionary)
        response = self.app.post('/pets', data=pet_json_string, content_type='application/json')
        response_dict = json.loads(response.data)
        assert response_dict == {"HTTP status": "400", "message": "dictionary is empty"}


    def test_get_pets(self):
        pluto_dictionary = {'name': 'Lulu','age': '3','species': 'dog'}
        kenny_dictionary = {'name': 'Kenny','age': '3','species': 'dog'}
        mimi_dictionary = {'name': 'Mimi','age': '10','species': 'cat'}

        all_dictionary = [pluto_dictionary, kenny_dictionary, mimi_dictionary]

        pet_json_string = json.dumps(pluto_dictionary)
        # response = requests.post('http://0.0.0.0:5000/pets',
        #                  data=pet_json_string)
        response = self.app.post('/pets', data=pet_json_string, content_type='application/json')
        # response = self.app.get('/pets')
        response_dict = json.loads(response.data)
        assert response.status_code == 200

        pet_json_string = json.dumps(kenny_dictionary)
        response = self.app.post('/pets', data=pet_json_string, content_type='application/json')
        response_dict = json.loads(response.data)

        pet_json_string = json.dumps(mimi_dictionary)
        response = self.app.post('/pets', data=pet_json_string, content_type='application/json')

        response_dict = json.loads(response.data)

        response = self.app.get('/pets')
        response_dict = json.loads(response.data)
        print(response_dict)
        print(all_dictionary)
        assert response_dict == all_dictionary



    def test_put_request(self):
        pet_dictionary = {'name': 'Pluto','age': '3','species': 'dog'}
        pluto_dictionary = {'name': 'Lulu','age': '3','species': 'dog'}
        kenny_dictionary = {'name': 'Kenny','age': '3','species': 'dog'}
        mimi_dictionary = {'name': 'Mimi','age': '10','species': 'cat'}

        pluto_json_string = json.dumps(pluto_dictionary)
        kenny_json_string = json.dumps(kenny_dictionary)
        mimi_json_string = json.dumps(mimi_dictionary)


        response = self.app.post('/pets', data=pluto_json_string, content_type='application/json')
        #response_dict = json.loads(response.data)

        response = self.app.post('/pets', data=kenny_json_string, content_type='application/json')
        #response_dict = json.loads(response.data)

        response = self.app.post('/pets', data=mimi_json_string, content_type='application/json')
        #response_dict = json.loads(response.data)

        kenny_update_dictionary = {'name': 'Kenny','age': '2','species': 'dog'}

        kenny_updated_json_string = json.dumps(kenny_update_dictionary)
        response = self.app.put('/pets/Kenny', data=kenny_updated_json_string, content_type='application/json')

        #print(response.data)
        all_dictionary = [pluto_dictionary, kenny_update_dictionary, mimi_dictionary, pet_dictionary]
        response_dict = json.loads(response.data)

        self.assertEqual(all_dictionary, response_dict)

        response = self.app.put('/pets/Charlie', data=kenny_updated_json_string, content_type='application/json')
        response_dict = json.loads(response.data)
        error_dict = {"HTTP status": "400", "message": "Key does not exist"}
        self.assertEqual(response_dict, error_dict)

        kenny_update_dictionary = {'nam': 'Kenny','ag': '2','spcies': 'dog'}

        kenny_updated_json_string = json.dumps(kenny_update_dictionary)
        response = self.app.put('/pets/Kenny', data=kenny_updated_json_string, content_type='application/json')
        response_dict = json.loads(response.data)
        error_dict = {"HTTP status": "400", "message": "ERROR"}

        self.assertEqual(response_dict, error_dict)


    def test_delete_pet(self):
        print("AAA")
        response_get = self.app.get('/pets')
        print(response_get.data)
        response = self.app.delete('/pets/Kenny')

        pet_dictionary = {'name': 'Pluto','age': '3','species': 'dog'}
        pluto_dictionary = {'name': 'Lulu','age': '3','species': 'dog'}
        kenny_dictionary = {'name': 'Kenny','age': '3','species': 'dog'}
        mimi_dictionary = {'name': 'Mimi','age': '10','species': 'cat'}

        all_dictionary = [pet_dictionary, pluto_dictionary, mimi_dictionary]

        response_dict = json.loads(response.data)

        self.assertEqual(all_dictionary, response_dict)




    # def test_check_pet_exist(self):
    #     response = self.app.get('/pets/Charlie')








# entry name for you test
if __name__ == '__main__':
    unittest.main()
