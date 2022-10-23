from skimage import exposure, io, measure
import numpy as np

class SurfaceTool:

    def __init__(self, viewer):
        self.viewer = viewer

    def createSurface(self):
        layer = self.viewer.layers.selection.active
        if not layer:
            return
        rawData = layer.data
        data = np.squeeze(rawData)
        max = 1
        if np.issubdtype(data.dtype, np.integer):
            max = np.iinfo(data.dtype).max
        iso_threshold = layer.iso_threshold * max
        scale = layer.scale
        spacing = (scale[1], scale[2], scale[0])
        volume = data.transpose(1, 2, 0)
        verts, faces, normals, values = measure.marching_cubes(volume, level=iso_threshold, spacing=spacing)
        self.viewer.add_surface((verts[:, [2, 0, 1]], faces,  values), name='surface of ' + layer.name)



