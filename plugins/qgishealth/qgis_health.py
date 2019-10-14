# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# oq-qgis-server-plugins
# Copyright (C) 2019 GEM Foundation
#
# oq-geoviewer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# oq-geoviewer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import platform
from qgis.core import Qgis
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
                'version': Qgis.QGIS_VERSION,
                'python': platform.python_version(),
                'platform': platform.platform()
            }
            response.setStatusCode(200)
        except Exception as exc:
            status = {
                'status': 500,
                'exception': exc
            }
            response.setStatusCode(500)
        # Write the response as json
        response.write(json.dumps(status, indent=4))


class HealthCheck():

    def __init__(self, serverIface):
        self.serv = HC()
        serverIface.serviceRegistry().registerService(HC())
