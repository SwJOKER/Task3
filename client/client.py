import logging
import threading
import requests

SERVER_IP = '127.0.0.1'
MSG = 'Minion\'s message'

def post_connect(ID):
   try:
      first_request = requests.post(f'http://{SERVER_IP}:8000/', json={"id": ID})
      uuid = first_request.text
      second_request = requests.post(f'http://{SERVER_IP}:8001/', json={'id': ID, 'uuid':uuid, 'message': MSG})
      print(second_request.text)
   except:
      logging.error('Something went wrong')

if __name__ == '__main__':
   for i in range(50):
      threading.Thread(target=post_connect(f'Nick{i}'))