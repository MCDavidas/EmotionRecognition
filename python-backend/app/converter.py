import base64
import io
from PIL import Image


def image2ascii(img):
    img_data = io.BytesIO()
    img.save(img_data, format=img.format)
    return base64.b64encode(img_data.getvalue()).decode('ascii')


def ascii2image(data):
    img_data = base64.b64decode(data)
    img = Image.open(io.BytesIO(img_data))
    return img
