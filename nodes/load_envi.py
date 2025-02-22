import os
from spectral.io import envi
import spectral as sp
from ..utils.preprocess import image2tensor


class LoadEnvi:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'header_file': ('STRING',),
                'image_file': ('STRING',)
            }
        }

    RETURN_TYPES = ('IMAGE', 'SPE')
    RETURN_NAMES = ('preview', 'spectral')

    CATEGORY = 'Spectral'
    FUNCTION = 'load_spectral'


    def load_spectral(self, header_file: str, image_file: str):
        if image_file.startswith('*.'):
            image_file = os.path.splitext(header_file)[0] + image_file[1:]

        img = envi.open(header_file, image_file)
        os.makedirs('temp', exist_ok=True)
        fp = os.path.join('temp', 'envi_preview.jpg')
        sp.save_rgb(fp, img)

        return image2tensor(fp), img

