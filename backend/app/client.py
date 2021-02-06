import asyncio
import websockets
import json
import os
from PIL import Image

from .converter import ascii2image, image2ascii


IMAGES_PATH = os.path.join(os.path.dirname(__file__), 'images')


def read_image():
    img_name = input('Insert image name ... ')
    img = Image.open(os.path.join(IMAGES_PATH, img_name))
    print(img.format, img.size, img.mode)
    return img


async def client():
    uri = "ws://localhost:56789"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        while True:
            img = read_image()
            message = json.dumps({'type': 'image', 'image': image2ascii(img)})
            await websocket.send(message)

            while True:
                answer = await websocket.recv()
                data = json.loads(answer)

                if data['type'] == 'image':
                    img = ascii2image(data['image'])
                    img.save(os.path.join(IMAGES_PATH, 'result.' + img.format))
                    break
                else:
                    print(data['value'])


def init_client():
    asyncio.get_event_loop().run_until_complete(client())


if __name__ == '__main__':
    init_client()
