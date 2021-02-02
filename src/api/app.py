import os
from flask import Flask, jsonify
from flask_restful import Api
from helpers.setup import bootstrap

app = Flask(__name__)
api = Api(app)

bootstrap(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
