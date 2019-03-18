import json
from qgis.server import QgsService


class EWMS(QgsService):

    def __init__(self):
        QgsService.__init__(self)

    def name(self):
        return "EWMS"

    def version(self):
        return "1.0.0"

    def allowMethod(method):
        return True

    def executeRequest(self, request, response, project):
        if request.parameters()['REQUEST'] == 'GetCustomPropertiesByLayerName':
            service = self._get_custom_properties_by_layer_name
        elif request.parameters()['REQUEST'] == 'GetCustomPropertiesByLayerId':
            service = self._get_custom_properties_by_layer_id
        else:
            response.setStatusCode(400)
            response.write("Missing or invalid 'REQUEST' parameter")
        try:
            service(request, response, project)
        except Exception as exc:
            response.setStatusCode(500)
            response.write("An error occurred: %s" % exc)

    def _get_custom_properties_by_layer_name(self, request, response, project):
        try:
            layer_names_str = request.parameters()['LAYERS']
        except KeyError:
            layer_names_str = None
        try:
            filter_str = request.parameters()['FILTER']
        except KeyError:
            filter_str = None
        if layer_names_str:
            layer_names = layer_names_str.split(',')
        else:
            layer_names = None
        print('layer_names: %s' % layer_names)
        if filter_str:
            filter_prop_items = [filter_prop.split(':')
                                 for filter_prop in filter_str.split(',')]
            print('filter_prop_items: %s' % filter_prop_items)
            filter_props = {
                filter_prop_name: filter_prop_value
                for filter_prop_name, filter_prop_value in filter_prop_items}
        else:
            filter_props = None
        print('filter_props: %s' % filter_props)
        custom_props = {}
        for layer_id, layer in project.mapLayers().items():
            layer_name = layer.name()
            if layer_names and layer_name not in layer_names:
                continue
            custom_props[layer_name] = {}
            custom_props[layer_name]['layer_id'] = layer_id
            for prop in layer.customPropertyKeys():
                prop_value = layer.customProperty(prop)
                custom_props[layer_name][prop] = prop_value
        print('custom_props: %s' % custom_props)
        for filter_prop in filter_props:
            for layer in custom_props:
                print('custom_props[%s][%s]: %s'
                      % (layer, filter_prop, custom_props[layer][filter_prop]))
                filter_prop_value = filter_props[filter_prop]
                if custom_props[layer][filter_prop] != filter_prop_value:
                    # del custom_props[layer]
                    break
        response.setStatusCode(200)
        response.write(
            json.dumps(custom_props, indent=4, sort_keys=True))

    def _get_custom_properties_by_layer_id(self, request, response, project):
        custom_props = {}
        for layer_id, layer in project.mapLayers().items():
            layer_name = layer.name()
            custom_props[layer_id] = {}
            custom_props[layer_id]['layer_name'] = layer_name
            for prop_key in layer.customPropertyKeys():
                custom_props[layer_id][prop_key] = (
                    layer.customProperty(prop_key))
        response.setStatusCode(200)
        response.write(
            json.dumps(custom_props, indent=4, sort_keys=True))


class EWM():

    def __init__(self, serverIface):
        self.serv = EWMS()
        serverIface.serviceRegistry().registerService(EWMS())
