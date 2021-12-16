import logging
import threading

import requests

SERVER_IP = '192.168.0.110'
MSG = 'Minion\'s message'



def client_connect(ID):
   try:
      name = ID
      first_request = requests.get(f'http://{SERVER_IP}:8000/{name}')
      uuid = first_request.text
      message = MSG
      second_request = requests.get(f'http://{SERVER_IP}:8001/{uuid}/{name}/{message}')
      print(second_request.text)
   except:
      logging.error('Something went wrong')

if __name__ == '__main__':
   for i in range(50):
      threading.Thread(target=client_connect(f'Nick{i}'))