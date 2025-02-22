from .nodes.load_spectral import LoadSpectral
from .nodes.load_envi import LoadEnvi
from .nodes.calculate import Calculate
from .nodes.plot import Plot
from .nodes.kmeans import KMeans


NODE_CLASS_MAPPINGS = {
    "LoadSpectral": LoadSpectral,
    'LoadEnvi': LoadEnvi,
    'Calculate': Calculate,
    'Plot': Plot,
    'KMeans': KMeans,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadSpectral": "Spectral Loader",
    "LoadEnvi": "ENVI Loader",
    'Calculate': 'Calculator',
    'Plot': 'Plot',
    'KMeans': 'KMeans',
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
