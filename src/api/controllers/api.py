from flask_restful import Resource

class ThresholdApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(TaskListAPI, self).__init__()

    def get(self):
        return None

    def put(self):
        return None

class LoginApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(TaskListAPI, self).__init__()

    def post(self):
        return None

class ModelFormApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(TaskListAPI, self).__init__()

    def post(self):
        return None
