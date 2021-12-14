import threading
from flask import Flask
import hashlib
import logging

# My typical setup for a Flask App.
# ./media is a folder that holds my JS, Imgs, CSS, etc.
app1 = Flask(__name__)
app2 = Flask(__name__)
names = dict()
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app1.route('/<username>')
def index1(username):
    md5 = hashlib.md5(username.encode('utf-8')).hexdigest()
    names[md5] = username
    return md5


@app2.route('/<md5>/<name>/<message>')
def index2(md5, name, message):
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='log.log')
    try:
        if (name == names[md5]):
            return f'Имя: {names[md5]} md5: {md5} Сообщение:{message}'
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