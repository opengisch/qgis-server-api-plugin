# -*- coding: utf-8 -*-
"""
/***************************************************************************
    QGIS Server ApiService: Add a new request to call ApiService QGIS server
    ---------------------
    Date                 : February 2019
    Copyright            : (C) 2019 by Marco Bernasocchi - OPENGIS.ch
    Email                : marco at opengis.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Marco Bernasocchi'
__date__ = 'February 2019'
__copyright__ = '(C) 2019, Marco Bernasocchi - OPENGIS.ch'

from qgis.server import QgsServerOgcApi
from qgis.core import QgsMessageLog, Qgis

from .api_handler import HandlerOne

# can be tested with
# docker run -p8010:80 -v `pwd`/api/qgis-server-nginx.conf:/etc/nginx/nginx.conf -v `pwd`/api:/io/plugins/api:ro -v /home/marco/tmp/demo_projects/:/io/data:ro --rm --name qgistest openquake/qgis-server:3.10

class ApiServer:
    """Plugin for QGIS server this plugin loads the ApiService"""

    def __init__(self, serverIface):
        # Save reference to the QGIS server interface
        self.serverIface = serverIface
        QgsMessageLog.logMessage("SUCCESS - api init plugin", level=Qgis.Critical)

        # register api
        api = QgsServerOgcApi(self.serverIface,
                              "/api/v1",
                              "apione",
                              "A firs API",
                              "1.0")
        # register handlers
        h = HandlerOne()
        api.registerHandler(h)
        self.serverIface.serviceRegistry().registerApi(api)
