
import json
from qgis.PyQt.QtCore import QBuffer, QIODevice, QTextStream
from qgis.server import (QgsServiceRegistry,
                         QgsService, QgsServerFilter)
from qgis.core import QgsMessageLog, QgsProject

class CustomServiceService(QgsService):

    def __init__(self):
        QgsService.__init__(self)

    def name(self):
        return "CUSTOM"

    def version(self):
        return "1.0.0"

    def allowMethod(method):
        return True

    def executeRequest(self, request, response, project):
        try:
            custom_props = {}
            for layer_id, layer in QgsProject.instance().mapLayers().items():
                layer_name = layer.name()
                custom_props[layer_name] = {}
                custom_props[layer_name]['layer_id'] = layer_id
                for prop_key in layer.customPropertyKeys():
                    custom_props[layer_name][prop_key] = layer.customProperty(
                        prop_key)
            response.setStatusCode(200)
            QgsMessageLog.logMessage('Custom service executeRequest')
            response.write(json.dumps(custom_props, indent=4, sort_keys=True))
        except Exception as exc:
            response.setStatusCode(500)
            QgsMessageLog.logMessage('Custom service executeRequest')
            response.write("An error occurred: %s" % exc)


class CustomService():

    def __init__(self, serverIface):
        self.serv = CustomServiceService()
        serverIface.serviceRegistry().registerService(CustomServiceService())

