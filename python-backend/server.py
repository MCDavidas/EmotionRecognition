import asyncio
import json
import logging
import websockets
import yaml
from PIL import Image, ImageFilter

from converter import ascii2image, image2ascii


logging.basicConfig()

connected_users = set()


async def handle_input_message(message):

    def handle_format_error():
        print('Incorrect input message!')
        return json.dumps({'type': 'error',
                           'value': 'Incorrect input message!'})

    try:
        json_data = json.loads(message)
    except json.JSONDecodeError:
        return handle_format_error()

    if 'type' not in json_data:
        return handle_format_error()

    if json_data['type'] == 'image':
        if 'image' not in json_data:
            return handle_format_error()
        else:
            answer_img = await analyze_image(json_data['image'])
            return json.dumps({'type': 'image',
                               'image': image2ascii(answer_img)})
    else:
        return handle_format_error()


async def register(websocket):
    connected_users.add(websocket)


async def unregister(websocket):
    connected_users.remove(websocket)


async def write_back(websocket, message):
    await websocket.send(message)


async def analyze_image(img_ascii):
    img = ascii2image(img_ascii)
    await asyncio.sleep(3)
    result_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    result_img.format = img.format
    return result_img


async def handler(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            await write_back(websocket,
                             json.dumps({'type': 'text',
                                         'value': 'waiting...'}))

            answer_message = await handle_input_message(message)
            await write_back(websocket, answer_message)

    finally:
        await unregister(websocket)


def init_server():
    try:
        with open("config.yaml", "r") as config_file:
            configuration = yaml.load(config_file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print("Error! Config not found.")
        return

    try:
        start_server = websockets.serve(handler,
                                        configuration['details']['host'],
                                        configuration['details']['port'])
    except Exception:
        print("Error! Incorrect config file.")
        return

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    init_server()
