import os
import random
import socket
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)
UUID = random.randint(100000, 100000000)


@app.route('/')
def show():
    return jsonify('Hello from web app')


@app.route('/hostname')
def get_hostname():
    return jsonify({'hostname' : socket.gethostname()})


@app.route('/author', methods=['GET'])
def get_author():
    author = os.getenv('AUTHOR')
    if author is None:
        # Если переменная окружения AUTHOR не задана, вернуть ошибку 404
        abort(404)
    return jsonify({'author': author})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'author': 'Переменная среды $AUTHOR, не найдена'}), 404)


@app.route('/id', methods=['GET'])
def get_id():
    return jsonify({'id': UUID})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
