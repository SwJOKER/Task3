import threading
from flask import Flask
import hashlib
import logging
import uuid

app1 = Flask(__name__)
app2 = Flask(__name__)
names = dict()
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app1.route('/<username>')
def index1(username):
    #md5 = hashlib.md5(username.encode('utf-8')).hexdigest()
    user_uuid = str(uuid.uuid4())
    names[user_uuid] = username
    return user_uuid


@app2.route('/<uuid>/<name>/<message>')
def index2(uuid, name, message):
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='log.log')
    try:
        if (name == names[uuid]):
            logging.info(f'Имя: {names[uuid]} uuid: {uuid} Сообщение:{message}')
            return f'Имя: {names[uuid]} uuid: {uuid} Сообщение:{message}'
        else:
            raise Exception
    except:
        return 'Неверный идентификатор'


def runFlaskApp1():
    app1.run(host='127.0.0.1', port=8000, debug=False, threaded=True)

def runFlaskApp2():
    app2.run(host='127.0.0.1', port=8001, debug=False, threaded=True)


if __name__ == '__main__':
    t1 = threading.Thread(target=runFlaskApp1)
    t2 = threading.Thread(target=runFlaskApp2)
    t1.start()
    t2.start()