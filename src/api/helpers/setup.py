from controllers.api import ModelFormApi, LoginApi
from flask_restful import Api

def bootstrap(api):
    api.add_resource(ModelFormApi, '/api/form', endpoint='form')
    api.add_resource(LoginApi, '/api/login', endpoint='login')
