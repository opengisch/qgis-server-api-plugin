# -*- coding: utf-8 -*-
"""
/***************************************************************************
    QGIS Server Plugin ApiService: Add a new request to call ApiService
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

 This script initializes the plugin, making it known to QGIS and QGIS Server.
"""


def serverClassFactory(serverIface):  # pylint: disable=invalid-name
    """Load ApiServer class from file api_server.

    :param iface: A QGIS Server interface instance.
    :type iface: QgsServerInterface
    """

    from .api_server import ApiServer
    return ApiServer(serverIface)
