# -*- coding: UTF-8 -*-
import flask
from random import randint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/world', methods=['GET'])
def generate_random_json():
    rand_id = randint(0, 100)
    dict = {
        'id': rand_id,
        'message': 'Hello World'
    }
    return dict

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)