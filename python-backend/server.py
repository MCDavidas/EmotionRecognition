import asyncio
import json
import logging
import websockets
import yaml


logging.basicConfig()

connected_users = set()


async def register(websocket):
    connected_users.add(websocket)


async def unregister(websocket):
    connected_users.remove(websocket)


async def write_back(websocket, message):
    await websocket.send(message)


async def analyze(data):
    await asyncio.sleep(3)
    return 'OK'


async def handler(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            await write_back(websocket,
                             json.dumps({"type": "answer",
                                         "value": "waiting..."}))
            data = json.loads(message)
            answer = await analyze(data)
            await write_back(websocket,
                             json.dumps({"type": "answer",
                                         "value": answer}))
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
