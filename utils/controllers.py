from flask_restful import Resource
from flask import jsonify, make_response
from .tasks import *


class MinimalAPI(Resource):
    def get(self,station):
        try:
            station = station.lower()
            # check if city correct then get data
            if(is_station(station)):
                data = get_daily(station)
                return make_response(jsonify(data), 200)
            else:
                if(len(closest_station(station))!= 0):
                    msg = 'Did you mean any of these: '+', '.join(i for i in closest_station(station))
                    return make_response(jsonify(msg=msg),400)
                else:
                    return make_response(jsonify(msg="The Resource was not Found on this Server"),404)
        except:
            return make_response(jsonify(msg="Internal Server Error Occurred"), 500)

class DetailedAPI(Resource):
    def get(self,station):
        try:
            station = station.lower()
            # check if city correct then get data
            if(is_station(station)):
                data = get_daily(station, detailed=True)
                return make_response(jsonify(data), 200)
            else:
                
                if(len(closest_station(station))!= 0):
                    msg = 'Did you mean any of these: '+', '.join(i for i in closest_station(station))
                    return make_response(jsonify(msg=msg),400)
                else:
                    return make_response(jsonify(msg="The Resource was not Found on this Server"),404)
        except:
            return make_response(jsonify(msg="Internal Server Error Occurred"), 500)

class ForecastAPI(Resource):
    def get(self,station):
        try:
            station = station.lower()
            # check if city correct then get data
            if(is_station(station)):
                data = get_forecast(station)
                return make_response(jsonify(data), 200)
            else:
                if(len(closest_station(station))!= 0):
                    msg = 'Did you mean any of these: '+', '.join(i for i in closest_station(station))
                    return make_response(jsonify(msg=msg),400)
                else:
                    return make_response(jsonify(msg="The Resource was not Found on this Server"),404)
        except:
            return make_response(jsonify(msg="Internal Server Error Occurred"), 500)