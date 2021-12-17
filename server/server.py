import threading
from flask import Flask, request
import logging
import uuid

app1 = Flask(__name__)
app2 = Flask(__name__)
HOST_IP = '127.0.0.1'
LOG_PATH = 'log.log'
names = dict()
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app1.route('/', methods=['POST'])
def fetch_id():
    try:
        user_uuid = str(uuid.uuid4())
        names[user_uuid] = request.get_json()['id']
        return user_uuid
    except:
        return None, 403

@app2.route('/', methods=['POST'])
def fetch_message():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename=LOG_PATH)
    try:
        answer = request.get_json()
        id = answer['id']
        uuid = answer['uuid']
        message = answer['message']
        if id == names[uuid]:
            logging.info(f'Name: {names[uuid]} uuid: {uuid} Message:{message}')
            return f'Name: {names[uuid]} uuid: {uuid} Message:{message}'
    except:
        return None, 403


def runFlaskApp1():
    app1.run(host=HOST_IP, port=8000, debug=False, threaded=True)

def runFlaskApp2():
    app2.run(host=HOST_IP, port=8001, debug=False, threaded=True)


if __name__ == '__main__':
    t1 = threading.Thread(target=runFlaskApp1)
    t2 = threading.Thread(target=runFlaskApp2)
    t1.start()
    t2.start()