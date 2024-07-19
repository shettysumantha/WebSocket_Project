import asyncio
import websockets
import json
import nest_asyncio

nest_asyncio.apply()

async def test():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Define messages for each action
        messages = [
            {"action": "echo", "content": "Hello"},
            {"action": "reverse", "content": "Hello"},
            {"action": "count_last_char", "content": "The quick brown fox jumped over the lazy dog o"}
        ]

        for message in messages:
            await websocket.send(json.dumps(message))

            if message['action'] == 'echo':
                print(f"\nSending echo message: {message['content']}")
                # Receive the initial echo response
                response = await websocket.recv()
                print(response)

                # Receive each character response
                for _ in message['content']:
                    response = await websocket.recv()
                    print(response)

            elif message['action'] == 'reverse':
                print(f"\nSending reverse message: {message['content']}")
                # Receive the initial reverse response
                response = await websocket.recv()
                print(response)

                # Receive each character response in reverse order
                for _ in message['content']:
                    response = await websocket.recv()
                    print(response)

            elif message['action'] == 'count_last_char':
                print(f"\nSending count_last_char message: {message['content']}")
                # Receive the count last character response
                response = await websocket.recv()
                print(response)

asyncio.run(test())
