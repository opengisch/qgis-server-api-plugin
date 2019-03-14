def serverClassFactory(serverIface):
    from . openquakeqgiswebservices import OpenQuakeQGIS
    return OpenQuakeQGIS(serverIface)

