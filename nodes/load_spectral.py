import os
from spectral.io import envi
import spectral as sp
from PIL import Image
from torchvision.transforms import ToTensor



class LoadSpectral:

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

    preprocess = ToTensor()

    def load_spectral(self, header_file: str, data_file: str):
        img = envi.open(header_file, data_file)
        os.makedirs('temp', exist_ok=True)
        fp = os.path.join('temp', 'spectral_preview.png')
        sp.save_rgb(fp, img)
        preview = self.preprocess(Image.open(fp)).unsqueeze(0).transpose(1, 3).transpose(1, 2)

        return preview, img

