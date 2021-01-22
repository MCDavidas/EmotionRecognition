import asyncio
import json
import logging
import websockets
import yaml


logging.basicConfig()

STATE = {"value": 0}

USERS = set()


def state_event():
    return json.dumps({"type": "state", **STATE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def handler(websocket, path):
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "minus":
                STATE["value"] -= 1
                await notify_state()
            elif data["action"] == "plus":
                STATE["value"] += 1
                await notify_state()
            else:
                logging.error("unsupported event: {}", data)
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
    except:
        print("Error! Incorrect config file.")
        return

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    init_server()
