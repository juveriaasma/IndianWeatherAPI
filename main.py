from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from utils.controllers import *


app = None
api = None


def createapp():
    # currdir=os.path.abspath(os.path.dirname(__file__))
    app = Flask('__name__')

    api = Api(app)

    app.app_context().push()

    return(app, api)

app, api = createapp()
CORS(app, resources={r'/*': {'origins': '*'}})

 
api.add_resource(MinimalAPI, "/<string:station>/weather")
api.add_resource(DetailedAPI, "/<string:station>/detailed_weather")
api.add_resource(ForecastAPI, "/<string:station>/forecast")


if(__name__ == '__main__'):
    app.debug=True
    app.run(host='0.0.0.0')