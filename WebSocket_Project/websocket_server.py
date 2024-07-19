import asyncio
import websockets
import json

async def echo_message(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        action = data.get('action')
        content = data.get('content')
        
        if action == 'echo':
            await websocket.send(json.dumps({"message": "Echoing message:"}))
            for char in content:
                await websocket.send(json.dumps({"message": char}))
                await asyncio.sleep(0.1)
                
        elif action == 'reverse':
            await websocket.send(json.dumps({"message": "Reversing message:"}))
            for char in reversed(content):
                await websocket.send(json.dumps({"message": char}))
                await asyncio.sleep(0.1)
                
        elif action == 'count_last_char':
            last_char = content[-1]
            count = content[:-1].count(last_char)
            await websocket.send(json.dumps({"message": f"Last character: {last_char}, Count: {count}"}))

async def main():
    async with websockets.serve(echo_message, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
