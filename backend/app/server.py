import asyncio
import json
import logging
import websockets
from PIL import Image

from .converter import ascii2image, image2ascii
from .analyzer import analyze_image


ERROR_MESSAGE = json.dumps({'type': 'error',
                            'value': 'Incorrect input message'})

connected_users = set()


async def handle_input_message(message):
    logging.info('Starting message parsing')

    def handle_format_error(explanation):
        logging.warning(f'Incorrect input message. {explanation}')
        return ERROR_MESSAGE

    try:
        json_data = json.loads(message)
    except (json.JSONDecodeError, TypeError):
        return handle_format_error('JSON decode error')

    if 'type' not in json_data:
        return handle_format_error('No type attribute')

    if json_data['type'] == 'image':
        if 'image' not in json_data:
            return handle_format_error('No image attribute')
        else:
            try:
                img = ascii2image(json_data['image'])
            except TypeError:
                return handle_format_error('Image type error')

            answer_img, emotion = await analyze_image(img)
            return json.dumps({'type': 'image',
                               'image': image2ascii(answer_img)})
    else:
        return handle_format_error('Message type is not image')


async def register(websocket):
    logging.info(f'Registering connection ip={websocket.remote_address[0]},' \
                 f'port={websocket.remote_address[1]}')
    connected_users.add(websocket)


async def unregister(websocket):
    logging.info('Closing connection ip={ip}, port={port}'.
                 format(ip=websocket.remote_address[0],
                        port=websocket.remote_address[1]))
    connected_users.remove(websocket)


async def write_back(websocket, message):
    logging.info(f'Sending message to ip={websocket.remote_address[0]},' \
                 f'port={websocket.remote_address[1]}')
    await websocket.send(message)


async def handler(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            await write_back(websocket,
                             json.dumps({'type': 'text',
                                         'value': 'waiting...'}))

            answer_message = await handle_input_message(message)
            await write_back(websocket, answer_message)

    except websockets.exceptions.ConnectionClosedError:
        logging.error(f'Connection ip={websocket.remote_address[0]}' \
                      f'port={websocket.remote_address[1]} closed abnormaly')
    finally:
        await unregister(websocket)


def init_server(host, port):
    logging.info('Opening websocket')
    start_server = websockets.serve(handler, host, port, ping_interval=None)
    logging.info('Websocket is serving')

    logging.info('Starting event loop')
    try:
        asyncio.get_event_loop().run_until_complete(start_server)
    except OSError as e:
        logging.error(e)
        return

    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        logging.info('Stopping server')


if __name__ == '__main__':
    init_server()
