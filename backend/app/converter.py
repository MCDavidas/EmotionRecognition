import base64
import io
from PIL import Image


def image2ascii(img):
    try:
        img_data = io.BytesIO()
        img.save(img_data, format=img.format)
        result = base64.b64encode(img_data.getvalue()).decode('ascii')
    except Exception:
        raise TypeError

    return result


def ascii2image(data):
    if data[:23] == 'data:image/jpeg;base64,':
        data = data[23:]

    try:
        img_data = base64.b64decode(data)
        img = Image.open(io.BytesIO(img_data))
    except Exception:
        raise TypeError
    return img
