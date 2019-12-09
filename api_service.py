import json
from qgis._core import QgsLogger
from qgis.server import (QgsService)

import api.api_calls as calls

class ApiService(QgsService):

    def __init__(self):
        QgsService.__init__(self)

    def name(self):
        return "API"

    def version(self):
        return "0.0.2"

    def allowMethod(method):
        return True

    def executeRequest(self, request, response, project):
        kwargs = request.parameters()
        # make kwargs keys lowercase
        kwargs = {k.lower(): v for k, v in kwargs.items()}

        # remove unused parameters service, map and request
        del(kwargs['service'])
        try:
            # make map uppercase so it does not conflict with python map
            # function
            map_path = kwargs.pop('map')
            kwargs['MAP'] = map_path

            # remove the method to be called from the kwargs
            call = kwargs.pop('request')
        except KeyError:
            error = "REQUEST and MAP parameter are mandatory"
            self.write_500(response, error)
            return False

        QgsLogger.debug('KWARGS: %s' % str(kwargs))
        try:
            # get the API method from the CALL parameter
            api_call = getattr(calls, call)
            # convert parameters to kwargs and dynamically call the correct API
            result = api_call(**kwargs)
            self.write_response(response, result)
        except (TypeError, AttributeError, calls.ApiError) as e:
            self.write_500(response, e)

    @staticmethod
    def write_response(response, body, status_code=200):
        response.setStatusCode(status_code)
        body = str(body)
        json_resp = {
            'status': status_code,
            'body': body
            }
        QgsLogger.debug(body)
        response.write(json.dumps(json_resp))

    def write_500(self, response, error):
        self.write_response(response, error, 500)
