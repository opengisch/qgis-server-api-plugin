from qgis.server import (QgsConfigCache, QgsService)
from qgis.core import QgsMessageLog, Qgis


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

        map = request.parameters()['MAP']
        QgsMessageLog.logMessage(
            'ApiService service executeRequest for %s' % map,
            'Server',
            Qgis.Info
            )
        try:
            QgsConfigCache.instance().removeEntry(map)
            msg = 'Success - cache cleared'
            level = Qgis.Info
            response.setStatusCode(200)
        except:
            msg = 'Fail - cache not cleared'
            level = Qgis.Warning
            response.setStatusCode(500)
        finally:
            QgsMessageLog.logMessage(msg, 'Server', level)
            response.write(msg)
