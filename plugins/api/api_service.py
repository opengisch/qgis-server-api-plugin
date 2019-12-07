from qgis._core import QgsLogger
from qgis.server import (QgsService)
from qgis.core import QgsMessageLog, Qgis

import api.api_calls as calls

class ApiService(QgsService):

    def __init__(self):
        QgsService.__init__(self)

    def name(self):
        return "API"

    def version(self):
        return "0.0.1"

    def allowMethod(method):
        return True

    def executeRequest(self, request, response, project):
        kwargs = request.parameters()
        kwargs = {k.lower(): v for k, v in kwargs.items()}
        del(kwargs['service'])
        map = kwargs.pop('map')
        call = kwargs.pop('request')

        QgsMessageLog.logMessage(
            'ApiService service executeRequest CALL %s for %s -- %s ' % (
                call, map, request.parameters()),
            'Server',
            Qgis.Info
            )
        QgsLogger.debug(str(kwargs))
        try:
            # get the API method from the CALL parameter
            api_call = getattr(calls, call)
            # convert parameters to kwargs and dynamically call the correct API
            result = api_call(**kwargs)
            level = Qgis.Info
            response.setStatusCode(200)
        except (TypeError, calls.ApiError) as e:
            result = str(e)
            level = Qgis.Warning
            response.setStatusCode(500)
        finally:
            QgsMessageLog.logMessage(str(result), 'Server', level)
            response.write(str(result))
