from PyQt5.QtCore import QRegularExpression
from qgis.server import QgsServerQueryStringParameter
from qgis.server import QgsServerOgcApiHandler
from qgis.server import QgsServerOgcApi
from qgis.PyQt import QtCore

from api.api_calls.generic_handler import GenericHandler


class DemoHandler(GenericHandler):
    PARAMS = [QgsServerQueryStringParameter("value1", True, QgsServerQueryStringParameter.Type.Double, "a double value")]

    def __init__(self):
        super().__init__("/test",
                         "handlerTest",
                         "First of its name Test",
                         "The first handler ever",
                         "Handler One Link Title",
                         QgsServerOgcApi.data,
                         tags=[],
                         parameters=self.PARAMS)

    def handleRequest(self, context):
        params = self.values(context)
        self.write(params, context)
