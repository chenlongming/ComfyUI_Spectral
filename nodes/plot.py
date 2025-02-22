import numpy as np
from spectral.io.bilfile import BilFile
from spectral.io.bipfile import BipFile
from spectral.io.bsqfile import BsqFile
from spectral.io.envi import SpectralLibrary
from matplotlib import pyplot as plt
from ..utils.preprocess import image2tensor


class Plot:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'image': ('SPE',),
                'series': ('NDARRAY',),
            },
        }

    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)

    CATEGORY = 'Spectral'
    FUNCTION = 'process'

    def process(self, image: BilFile | BipFile | BsqFile | SpectralLibrary, series: np.ndarray):
        x = np.arange(image.nbands)
        data = []
        for y in series:
            data.append(x)
            data.append(y)

        fig, ax = plt.subplots(1, 1)
        ax.plot(*data)
        fp = 'temp/plot.png'
        fig.savefig(fp)
        return image2tensor(fp),
