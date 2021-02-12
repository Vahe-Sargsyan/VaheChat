import asyncio
import websockets

USERS = set()

async def addUser(websocket):
    USERS.add(websocket)

async def removeUser(websocket):
    USERS.remove(websocket)

async def socket(websocket, path):
    await addUser(websocket)

    try:
        while True:
            message = await websocket.recv()
            print('---------')
            for us in USERS:
            	print(us.host +' > '+message)
            	print()
            # print(list(user) )

            if '<' in message and '>' in message:
            	message = message.split('>')[1].split('<')[0]
            print('---------')
            await asyncio.wait([user.send(message) for user in USERS])
    finally:
        await removeUser(websocket)

start_server = websockets.serve(socket, '192.168.2.104', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()