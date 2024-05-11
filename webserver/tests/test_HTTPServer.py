import asyncio
from unittest import TestCase

from webserver.service.HTTPServer import HTTPServer


class TestHTTPServer(TestCase):

    def setUp(self) -> None:
        self.request = '''
        GET /poka.html HTTP/1.1
        Connection: keep-alive
        Host: primary.com
        User-Agent: PostmanRuntime/7.37.3
        Accept: */*
        Postman-Token: b3a34d9f-21a9-46c6-a8a8-58cc15826dcd
        Accept-Encoding: gzip, deflate, br
        '''
        self.root = HTTPServer()

    async def test_handle_request(self):
        rsp = b'''HTTP/1.1 404 Not Found Content-Type: text/html'''
        rsp += self.root.get_status_code_html(404).encode()
        task = await self.root.handle_request(self.request)
        self.assertEquals(rsp, task)

    def test_http_501_handler(self):
        response_line = self.root.response_line(status_code=501)
        response_body = self.root.get_status_code_html(501).encode()
        response_headers = self.root.response_headers()
        blank_line = b"\r\n"
        rsp = b"".join([response_line, response_headers, blank_line, response_body])

        task = self.root.HTTP_501_handler(self.request)
        self.assertEquals(rsp, task)
