from PIL import Image

def resize_image(path, size=(256, 256)):
    img = Image.open(path)
    return img.resize(size)