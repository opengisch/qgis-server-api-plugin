def serverClassFactory(serverIface):
    from . qgis_health import HealthCheck
    return HealthCheck(serverIface)
