from PIL import Image
from torchvision.transforms import ToTensor


transform = ToTensor()

def image2tensor(im: str | Image.Image):
    if isinstance(im, str):
        im = Image.open(im)

    return transform(im).permute(1, 2, 0).unsqueeze(0)
