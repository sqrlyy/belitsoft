import requests

URL = 'https://petstore.swagger.io/v2/'


def create_user():
    user = {
        "id": 999999,
        "username": "sqrlyy",
        "firstName": "unknown",
        "lastName": "unknown",
        "email": "unknown",
        "password": "unknown",
        "phone": "unknown",
        "userStatus": 0
    }
    request = requests.post(f'{URL}user', json=user)
    assert request.status_code == 200


def get_user():
    username = 'sqrlyy'
    request = requests.get(f'{URL}user/{username}')
    assert request.status_code == 200


def update_user():
    username = 'sqrlyy'
    user = {
        "id": 999999,
        "username": "sqrl",
        "firstName": "Maks",
        "lastName": "Posokhov",
        "email": "unknown",
        "password": "unknown",
        "phone": "unknown",
        "userStatus": 0
    }
    request = requests.put(f'{URL}user/{username}', json=user)
    assert request.status_code == 200


def delete_user():
    username = 'sqrl'
    request = requests.delete(f'{URL}user/{username}')
    assert request.status_code == 200
