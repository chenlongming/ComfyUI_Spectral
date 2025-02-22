import os
import spectral as sp
from ..utils.preprocess import image2tensor


class LoadSpectral:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'image_file': ('STRING',)
            }
        }

    RETURN_TYPES = ('IMAGE', 'SPE')
    RETURN_NAMES = ('preview', 'spectral')

    CATEGORY = 'Spectral'
    FUNCTION = 'load_spectral'


    def load_spectral(self, image_file: str):
        img = sp.open_image(image_file)
        os.makedirs('temp', exist_ok=True)
        fp = os.path.join('temp', 'spectral_preview.jpg')
        sp.save_rgb(fp, img)

        return image2tensor(fp), img
