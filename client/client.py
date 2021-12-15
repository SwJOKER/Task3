import requests

if __name__ == '__main__':
   name = 'SwJOKER1'
   first_request = requests.get(f'http://127.0.0.1:8000/{name}')
   md5 = first_request.text
   message = input()
   second_request = requests.get(f'http://127.0.0.1:8001/{md5}/{name}/{message}')
   print(second_request.text)