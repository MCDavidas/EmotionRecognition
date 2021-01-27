import asyncio
import json
import logging
import websockets
import yaml
from PIL import Image

from converter import ascii2image, image2ascii
from analyzer import analyze_image


connected_users = set()


async def handle_input_message(message):

    def handle_format_error():
        logging.warning('Incorrect input message')
        return json.dumps({'type': 'error',
                           'value': 'Incorrect input message'})

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
            img = ascii2image(json_data['image'])
            answer_img = await analyze_image(img)
            return json.dumps({'type': 'image',
                               'image': image2ascii(answer_img)})
    else:
        return handle_format_error()


async def register(websocket):
    logging.info('Registering connection ip={ip}, port={port}'.
                 format(ip=websocket.remote_address[0],
                        port=websocket.remote_address[1]))
    connected_users.add(websocket)


async def unregister(websocket):
    logging.info('Closing connection ip={ip}, port={port}'.
                 format(ip=websocket.remote_address[0],
                        port=websocket.remote_address[1]))
    connected_users.remove(websocket)


async def write_back(websocket, message):
    logging.info('Sending message to client ip={ip}, port={port}'.
                 format(ip=websocket.remote_address[0],
                        port=websocket.remote_address[1]))
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

    finally:
        await unregister(websocket)


def init_server():
    logging_level = logging.WARNING
    logging_filename = 'server.log'

    logging.basicConfig(level=logging_level)

    try:
        with open("config.yaml", "r") as config_file:
            configuration = yaml.load(config_file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        logging.error("Config not found")
        return

    try:
        if 'logging' in configuration:

            if 'level' in configuration['logging']:
                if configuration['logging']['level'] == 'DEBUG':
                    logging_level = logging.DEBUG
                elif configuration['logging']['level'] == 'INFO':
                    logging_level = logging.INFO
                elif configuration['logging']['level'] == 'WARNING':
                    logging_level = logging.WARNING
                elif configuration['logging']['level'] == 'ERROR':
                    logging_level = logging.ERROR
                elif configuration['logging']['level'] == 'CRITICAL':
                    logging_level = logging.CRITICAL
                else:
                    raise Exception

            logging.getLogger().setLevel(logging_level)

        logging.info('Opening websocket...')
        start_server = websockets.serve(handler,
                                        configuration['server']['host'],
                                        configuration['server']['port'],
                                        ping_interval=None)
        logging.info('Websocket is serving')

    except Exception:
        logging.error("Incorrect config file")
        return

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
