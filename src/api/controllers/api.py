from flask_restful import Resource, reqparse
import joblib
import traceback
import pandas as pd
import numpy as np

class LoginApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(LoginApi, self).__init__()

    def post(self):
        return None

class ModelFormApi(Resource):

    def __init__(self):
        self.model = joblib.load("./data/model.pkl")
        self.reqparse = reqparse.RequestParser()
        super(ModelFormApi, self).__init__()

    def post(self):
        return None
