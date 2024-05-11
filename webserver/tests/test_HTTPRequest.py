from unittest import TestCase

from webserver.service.HTTPRequest import HTTPRequest


class TestHTTPRequest(TestCase):
    def setUp(self):
        self.data = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
        self.root = HTTPRequest(self.data)

    def test_parse(self):
        self.assertTrue(self.root.parse(self.data))
