def serverClassFactory(serverIface):
    from . layercustomproperties import GetLayerCustomProperties
    return GetLayerCustomProperties(serverIface)

