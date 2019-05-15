from flask import Flask, request, jsonify
from flask_restful import Api, Resource
app = Flask(__name__)

api=Api(app)

def checkposted(posted, function):
    if(function == "add" or function == "subtract"):
        if "x" not in posted or "y" not in posted:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        posted = request.get_json()
        status = checkposted(posted, "add")
        if(status != 200):
            retJ = {
                "Message": "An error happened",
                "Status code": status
            }
            return jsonify(retJ)
        x = posted["x"]
        y = posted["y"]
        x = int(x)
        y = int(y)
        sum = x+y
        ret = {
            'Message': sum,
            'Status code': 200
        }
        return jsonify(ret)

class Subtract(Resource):
    def post(self):
        posted = request.get_json()
        status = checkposted(posted, "subtract")
        if(status != 200):
            retJ = {
                "Message": "An error happened",
                "Status code": status
            }
            return jsonify(retJ)
        x = posted["x"]
        y = posted["y"]
        x = int(x)
        y = int(y)
        diff = x-y
        ret = {
            'Message': diff,
            'Status code': 200
        }
        return jsonify(ret)

api.add_resource(Add, "/add")
api.add_resource(Subtract,"/subtract")
if __name__ == "__main__":
    app.run(debug=True)