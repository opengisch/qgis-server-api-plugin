# oq-qgis-server-plugin

Experiments with server side QGIS plugins

### Start the container (ephemeral)

```bash
$ docker run -v $(pwd):/io/data -v $(pwd)/plugins:/io/plugins --name qgis --rm -ti -p 8015:80 openquake/qgis-server:3
```

### Debug

```bash
$ docker exec -ti qgis /bin/bash
> cat /tmp/qgis-server.log
```

### Example URL

- http://localhost:8015/ogc/demo_italy?SERVICE=WMS&REQUEST=GetCapabilities
- http://localhost:8015/ogc/demo_italy?SERVICE=CUSTOM

