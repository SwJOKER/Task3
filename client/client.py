import logging

import requests

ID = 'Minion'
MSG = 'Minion\'s message'

def client_connect():
   try:
      name = ID
      first_request = requests.get(f'http://127.0.0.1:8000/{name}')
      md5 = first_request.text
      message = MSG
      second_request = requests.get(f'http://127.0.0.1:8001/{md5}/{name}/{message}')
      print(second_request.text)
   except:
      logging.error('Something went wrong')

if __name__ == '__main__':
   client_connect()