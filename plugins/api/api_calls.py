from qgis.core import QgsProject, QgsRasterLayer


class ApiError(RuntimeError):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


# Dynamic API generation #####################################################
# All functions in this module MUST have a first positional parameter called
# MAP. This is the path to the qgs file that is being edited. It is the
# content of the MAP url parameter
# all other parameters are poassed as kwargs from ApiService.executeRequest
# ############################################################################

def simple_test(MAP, name, provider='wms'):
    if name == 'mini-me':
        raise ApiError("I'm Austin Powers, I got you")
    return MAP, name, provider


def add_raster_layer(MAP, url, name, shortname, is_basemap, provider='wms'):
    """Add a raster layer to the project,
    path: path of the project, relative to the projects' directory

    Return: id of the added layer
    """

    layer = QgsRasterLayer(url, name, 'wms')
    layer.setShortName(shortname)

    project = QgsProject()
    project.read(MAP)

    project = QgsProject.instance()

    add_to_legend = not is_basemap
    added_layer = project.addMapLayer(layer, addToLegend=add_to_legend)

    project.write()
    return added_layer.id()


if __name__ == '__main__':
    import requests
    urls = {}
    base_url = 'http://localhost:8010/ogc/nepal_hazard?service=API'
    urls[base_url + '&request=simple_test&name=good'] = 200
    urls[base_url + '&request=simple_test&name=mini-me'] = 500
    urls[base_url + '&request=simple_test'] = 500
    urls[base_url +
                '&request=add_raster_layer'
                '&url=type%3Dxyz%26%26url%3Dhttp%3A%2F%2Fbasemaps.cartocdn.com%2Fdark_all%2F%7Bz%7D%2F%7Bx%7D%2F%7By%7D.png'
                '&name=CartoDb%20Dark%20Matter'
                '&shortname=cartodb-dark-matter'
                '&is_basemap=true'
                ] = 200
    for url, status in urls.items():
        print(url)
        response = requests.get(url)
        if response.status_code != status:
            raise RuntimeError('Expected status code {}, got {}'.format(
                status, response.status_code))
        print(response.text)
