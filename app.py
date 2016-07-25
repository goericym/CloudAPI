from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask import render_template

application = Flask(__name__)
api = Api(application)


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


@application.route('/index/')
def index():
    return render_template('index.html')

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':

    application.run(debug=True)
