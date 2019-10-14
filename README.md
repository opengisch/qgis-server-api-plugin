# oq-qgis-server-plugins

Plugins extending QGIS web services

### Download demos

```bash
$ git submodule update --init
```

### Start the container (ephemeral)

```bash
$ docker run -v $(pwd)/demos/projects:/io/data -v $(pwd)/plugins:/io/plugins --name qgis --rm -ti -p 8015:80 openquake/qgis-server:stable
```

### Debug

```bash
$ docker logs [-f] qgis
$ docker exec -ti qgis /bin/bash
```

### Example URL

- http://localhost:8015/ogc/nepal_hazard?service=WMS&request=GetCapabilities
- http://localhost:8015/ogc/nepal_hazard?service=EWMS&request=GetLayerCustomProperties
- http://localhost:8015/ogc/nepal_hazard?service=HC
