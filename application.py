from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask import render_template
application = Flask(__name__, static_url_path='')
api = Api(application)


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


class index(Resource):

    def get(self):
        return render_template('index.html')

api.add_resource(HelloWorld, '/')
api.add_resource(index, '/index')
if __name__ == '__main__':
    application.run(debug=True)
