from .nodes.load_spectral import LoadSpectral


NODE_CLASS_MAPPINGS = {
    "LoadSpectral": LoadSpectral,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadSpectral": "Spectral Loader",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
