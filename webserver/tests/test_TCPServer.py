import asyncio
from unittest import TestCase

from webserver.service.TCPServer import TCPServer


class TestTCPServer(TestCase):
    def setUp(self):
        self.root = TCPServer()

    async def test_send_message(self):
        init_task = asyncio.create_task(self.root.init())
        server_socket = await init_task
        self.assertTrue(self.root.send_message(server_socket))
