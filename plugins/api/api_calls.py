from qgis.core import QgsProject, QgsRasterLayer


class ApiError(RuntimeError):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


def simple_test(path, name, provider='wms'):
    return path, name, provider


def add_raster_layer(path, url, name, shortname, is_basemap, provider='wms'):
    """Add a raster layer to the project,
    path: path of the project, relative to the projects' directory

    Return: id of the added layer
    """

    layer = QgsRasterLayer(url, name, 'wms')
    layer.setShortName(shortname)

    project = QgsProject()
    project.read(path)

    project = QgsProject.instance()

    add_to_legend = not is_basemap
    added_layer = project.addMapLayer(layer, addToLegend=add_to_legend)

    project.write()
    return added_layer.id()


if __name__ == '__main__':
    add_raster_layer(
        '/home/pippo/pippo.qgs',
        'type=xyz&&url=http://basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png',
        'CartoDb Dark Matter',
        'cartodb-dark-matter',
        False,
        True)
