from qgis.PyQt.QtCore import QRegularExpression
from qgis.server import (QgsServerOgcApi, QgsServerOgcApiHandler)


class GenericHandler(QgsServerOgcApiHandler):
    """Base handler to be inherited"""

    def __init__(self, path, operationId, summary, description,
                 linkTitle, linkType, tags=None, parameters=None):
        super().__init__()
        # self._handleRequest = handleRequest
        self._path = path
        self._operationId = operationId
        self._summary = summary
        self._description = description
        self._linkTitle = linkTitle
        self._linkType = linkType
        self._tags = tags
        self._parameters = parameters

    def path(self):
        return QRegularExpression(self._path)

    def operationId(self):
        return self._operationId

    def summary(self):
        return self._summary

    def description(self):
        return self._description

    def linkTitle(self):
        return self._linkTitle

    def linkType(self):
        return self._linkType

    def tags(self):
        return self._tags

    def parameters(self, context):
        return self._parameters

    def handleRequest(self, context):
        #self._handleRequest(self, context)
        raise NotImplementedError("handleRequest Must be overriden")
