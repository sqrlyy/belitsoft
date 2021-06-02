import requests
import unittest


class SwaggerCrudTest(unittest.TestCase):
    URL = 'https://petstore.swagger.io/v2/'

    def test_create_user(self):
        user = {
            "id": 9999912,
            "username": "sqrlyy",
            "firstName": "unknown",
            "lastName": "unknown",
            "email": "unknown",
            "password": "unknown",
            "phone": "unknown",
            "userStatus": 0
        }
        request = requests.post(f'{self.URL}user', json=user)
        self.assertEqual(request.status_code, 200)

    def test_get_user(self):
        username = 'sqrlyy'
        request = requests.get(f'{self.URL}user/{username}')
        self.assertEqual(request.status_code, 200)

    def test_update_user(self):
        username = 'sqrlyy'
        user = {
            "id": 9999912,
            "username": "sqrl",
            "firstName": "Maks",
            "lastName": "Posokhov",
            "email": "unknown",
            "password": "unknown",
            "phone": "unknown",
            "userStatus": 0
        }
        request = requests.put(f'{self.URL}user/{username}', json=user)
        self.assertEqual(request.status_code, 200)

    def test_delete_user(self):
        username = 'sqrl'
        request = requests.delete(f'{self.URL}user/{username}')
        self.assertEqual(request.status_code, 200)


if __name__ == '__main__':
    unittest.main()
