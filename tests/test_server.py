import requests
from client.client import SERVER_IP


def test_first_connection():
    first_request = requests.post(f'http://{SERVER_IP}:8000/', json={"id": "Test"})
    assert (first_request.status_code == 200)

def test_first_connection_failed():
    first_request = requests.post(f'http://{SERVER_IP}:8000/', json={"i": "Test"})
    assert(first_request.status_code == 400)

def test_second_connection_failed():
    #uuid заведомо не верный
    second_request = requests.post(f'http://{SERVER_IP}:8001/', json={'id': 'test', 'uuid': 'test', 'message': 'test'})
    assert(second_request.status_code == 400)

def test_second_connection():
    uuid = requests.post(f'http://{SERVER_IP}:8000/', json={'id': 'test'}).text
    second_request = requests.post(f'http://{SERVER_IP}:8001/', json={'id': 'test', 'uuid': uuid, 'message': 'test passed'})
    assert second_request.status_code == 200