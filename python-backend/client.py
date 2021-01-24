import asyncio
import websockets
import json
from PIL import Image

from converter import ascii2image, image2ascii


def read_image():
    img_path = input('Insert path to image ... ')
    img = Image.open(img_path)
    print(img.format, img.size, img.mode)
    return img


async def client():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        while True:
            img = read_image()
            message = json.dumps({'type': 'image', 'image': image2ascii(img)})
            await websocket.send(message)

            while True:
                answer = await websocket.recv()
                data = json.loads(answer)

                if data['type'] == 'image':
                    img = ascii2image(data['image'])
                    img.save('result.jpg')
                    break
                else:
                    print(data['value'])


def main():
    asyncio.get_event_loop().run_until_complete(client())


if __name__ == '__main__':
    main()
