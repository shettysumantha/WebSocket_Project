# WebSocket_Project
This WebSocket backend performs the following actions:
1. Echoes whatever message is sent in a streaming format with a 0.1-second delay.
2. Echoes the message in reverse in a streaming format with a 0.1-second delay.
3. Counts the number of times the last character is repeated in the message (excluding the last character) and returns this count.

## Requirements
- Python 3.x version
- `websockets` library
- `asyncio` library

  ## Installation
- pip install websockets asyncio
- pip install nest_asyncio

  ## Procedure
  1. Set Up Your Development Environment
  2. Create the WebSocket Backend with appropriate file name(eg.websocket_server.py)
  3. Connect to the WebSocket server at 'ws://localhost:8765'.
     - Open WebSocketking.com and Connent the sever
     - Write message in input area avaible in WebSocketKing and Press and Send
  5. Create websocket_client.py file to test the WebSocket backend

  ##  Echo Request

  {
    "action": "echo",
    "content": "Hello"
  }
  ## Echo Response
  {
    "message": "H"
}
{
    "message": "e"
}
{
    "message": "l"
}
{
    "message": "l"
}
{
    "message": "o"

}

## Reverse Request
{
    "action": "reverse",
    "content": "Hello"
}
## Reverse Response
{
    "message": "o"
}
{
    "message": "l"
}
{
    "message": "l"
}
{
    "message": "e"
}
{
    "message": "H"
}

## Count_Last_Character Request
{
    "action": "count_last_char",
    "content": "The quick brown fox jumped over the lazy dog o"
}
## Response
{
    "message": "Last character: o, Count: 4"
}

## Running the Backend
- Open Terminal and Run websocket_server.py
- Open another terminal and run websocket_client.py(only for testing You can directly give input by opening WebSocketKing and by connecting server)
