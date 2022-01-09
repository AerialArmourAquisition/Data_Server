from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class Home(Resource):

    def home(self):
        return "<b> Hello </b>"


api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



