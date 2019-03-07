def serverClassFactory(serverIface):
    from . customservice import GetLayerCustomProperties
    return GetLayerCustomProperties(serverIface)

