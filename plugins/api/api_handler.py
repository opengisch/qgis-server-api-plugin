from qgis.PyQt.QtCore import QRegularExpression

from qgis.server import (
    QgsServerOgcApiHandler,
    QgsServerOgcApi,
    QgsServerQueryStringParameter,
    )


class HandlerOne(QgsServerOgcApiHandler):
    """Example handler"""

    def path(self):
        return QRegularExpression("/handlerone")

    def operationId(self):
        return "handlerOne"

    def summary(self):
        return "First of its name"

    def description(self):
        return "The first handler ever"

    def linkTitle(self):
        return "Handler One Link Title"

    def linkType(self):
        return QgsServerOgcApi.data

    def handleRequest(self, context):
        """Simple mirror: returns the parameters"""
        params = self.values(context)
        self.write(params, context)

    def parameters(self, context):
        return [QgsServerQueryStringParameter(
            "value1",
            True,
            QgsServerQueryStringParameter.Type.Double,
            "a double value")]
