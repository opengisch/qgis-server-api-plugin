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
$ docker exec -ti qgis /bin/bash
> cat /tmp/qgis-server.log
```

### Example URL

- http://localhost:8015/ogc/nepal_hazard?SERVICE=WMS&REQUEST=GetCapabilities
- http://localhost:8015/ogc/nepal_hazard?SERVICE=EWMS&REQUEST=GetCustomProperties
