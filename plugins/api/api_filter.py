# -*- coding: utf-8 -*-
"""
/***************************************************************************
    QGIS Server Plugin Filters: Add a new request to call ApiService QGIS server
    ---------------------
    Date                 : February 2019
    Copyright            : (C) 2017 by Michaël Douchin - 3Liz
                           (C) 2019 by Marco Bernasocchi - OPENGIS.ch
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

import json
import os
from configparser import ConfigParser

from qgis.core import QgsMessageLog
from qgis.server import *


class ApiFilter(QgsServerFilter):
    metadata = {}

    def __init__(self, server_iface):
        QgsMessageLog.logMessage("ApiFilter.init")
        super(ApiFilter, self).__init__(server_iface)
        self.server_iface = server_iface
        self.request = None
        self.project_path = None
        self.debug_mode = True

        self.get_metadata()

        # syslog.syslog(syslog.LOG_ERR, "ApiService - INITIALIZE")

    def get_metadata(self):
        """
        Get plugin metadata
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mfile = os.path.join(dir_path, '../metadata.txt')
        if os.path.isfile(mfile):
            config = ConfigParser()
            config.read(mfile)
            self.metadata = {
                'name': config.get('general', 'name'),
                'version': config.get('general', 'version')
                }

    def set_json_response(self, status, body):
        """
        Set response with given parameters
        """
        self.request.clearHeaders()
        self.request.setInfoFormat('text/json')
        self.request.setHeader('Content-type', 'text/json')
        self.request.setHeader('Status', status)
        self.request.clearBody()
        self.request.appendBody(json.dumps(body))

    def responseComplete(self):
        """
        Send new response
        """

        self.request = self.server_iface.requestHandler()
        params = self.request.parameterMap()

        # Check if interesting request. If not, just send the response
        if 'REQUEST' not in params or params['REQUEST'].lower() not in [
            'getcapabilities']:
            return

        # Get capabilities
        if params['REQUEST'].lower() == 'getcapabilities':
            body = {
                'status': 'success',
                'metadata': self.metadata
                }
            self.set_json_response('200', body)
            return

        # REQUEST is now invalidatecache
        # Check if needed params are set
        if 'map' not in params:
            body = {
                'status': 'fail',
                'message': 'Missing parameters: map is required '
                }
            self.set_json_response('200', body)
            return

        self.project_path = params['map']

        QgsConfigCache.instance().removeEntry(self.project_path)

        body = {
            'MAP': self.project_path,
            'status': 'success',
            'message': 'cache cleared'
            }
        self.set_json_response('200', body)

        return
