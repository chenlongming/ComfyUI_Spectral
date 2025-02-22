import numpy as np
import torch
from spectral.io.bilfile import BilFile
from spectral.io.bipfile import BipFile
from spectral.io.bsqfile import BsqFile
from spectral.io.envi import SpectralLibrary


class Calculate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'image': ('SPE',),
                'method': (['mean'], {'default': 'mean'}),
                'masks': ('MASK',)
            },
        }

    RETURN_TYPES = ('NDARRAY',)
    RETURN_NAMES = ('results',)

    CATEGORY = 'Spectral'
    FUNCTION = 'calculate'

    def calculate(self, image: BilFile | BipFile | BsqFile | SpectralLibrary, masks: torch.Tensor, method: str = 'mean'):
        if method == 'mean':
            raw = image.asarray()
            data = np.zeros((masks.shape[0], image.shape[-1]), )
            for i, mask in enumerate(masks):
                data[i] = raw[mask != 0].mean(0)
            return data,
        else:
            raise NotImplementedError('Not implemented method {}.'.format(method))
