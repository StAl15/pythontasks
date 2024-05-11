import asyncio
import json
import socket

from webserver.service.HTTPRequest import HTTPRequest
from webserver.utils.logger import Logger


class TCPServer:
    def __init__(self):
        self.logger = Logger()
        with open("config/config.json") as f:
            content = json.loads(f.read())
            self.host = content["server"]["location"]
            self.port = int(content['server']['listen'])

    async def init(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('127.0.0.1', 9999))
        server_socket.listen(5)

        print("Listening at", server_socket.getsockname())
        self.logger.logging_info(f'Listening at {server_socket.getsockname()}')
        return server_socket

    async def start(self):
        init_task = asyncio.create_task(self.init())
        server_socket = await init_task

        while True:
            send_message_task = asyncio.create_task(self.send_message(server_socket))
            await send_message_task

    async def send_message(self, s):
        conn, addr = s.accept()
        print("Connected by", addr)
        self.logger.logging_info(f'Connected by {addr}')
        payload = b''
        while True:
            data = conn.recv(1024)
            payload += data
            if len(data) < 1024:
                break

        request = HTTPRequest(payload)

        if request.headers['Connection'] == 'keep-alive':
            response_task = asyncio.create_task(self.handle_request(payload))
            response = await response_task

            conn.sendall(response)

        elif request.headers['Connection'] == 'close':
            conn.close()

        if not payload:
            conn.close()
        return True

    async def handle_request(self, data):

        return data
