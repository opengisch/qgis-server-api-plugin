def serverClassFactory(serverIface):
    from . extended_qgis_web_services import EWM
    return EWM(serverIface)
