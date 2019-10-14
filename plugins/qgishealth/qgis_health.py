import json
from qgis.core.Qgis import QGIS_VERSION
from qgis.server import QgsService


class HC(QgsService):

    def __init__(self):
        QgsService.__init__(self)

    def name(self):
        return "HC"

    def version(self):
        return "1.0.0"

    def allowMethod(method):
        return True

    def executeRequest(self, request, response, project):
        try:
            status = {
                'status': 200,
                'version': QGIS_VERSION,
            }
            response.setStatusCode(200)
            response.write(
                json.dumps(status, indent=4, sort_keys=True))
        except Exception as exc:
            response.setStatusCode(500)
            response.write("An error occurred: %s" % exc)


class HealthCheck():

    def __init__(self, serverIface):
        self.serv = HC()
        serverIface.serviceRegistry().registerService(HC())
