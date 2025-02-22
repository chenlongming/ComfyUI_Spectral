from .nodes.load_spectral import LoadSpectral
from .nodes.load_envi import LoadEnvi


NODE_CLASS_MAPPINGS = {
    "LoadSpectral": LoadSpectral,
    'LoadEnvi': LoadEnvi
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadSpectral": "Spectral Loader",
    "LoadEnvi": "ENVI Loader",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
