import json
import mimetypes
import os

from webserver.service.HTTPRequest import HTTPRequest
from webserver.service.TCPServer import TCPServer
from webserver.utils.logger import Logger


class HTTPServer(TCPServer):
    def __init__(self):
        super().__init__()
        with open("config/config.json") as f:
            content = json.loads(f.read())
            self.logger = Logger()
            self.headers = content['headers']
            self.status_codes = content['status_codes']
            self.virtual_hosts = content['server']['virtual_hosts']
            self.default_host = content['server']['default_host']

    async def handle_request(self, data):
        request = HTTPRequest(data)
        try:
            handler = getattr(self, 'handle_%s' % request.method)
        except AttributeError as e:
            handler = self.HTTP_501_handler
            self.logger.logging_error(e)

        response = handler(request)
        self.logger.logging_info(
            f'{request.method}\n{response}\n{request.headers}'
        )
        return response

    def HTTP_501_handler(self, request):
        response_line = self.response_line(status_code=501)

        response_headers = self.response_headers()

        blank_line = b"\r\n"

        response_body = b"<h1>501 Not Implemented</h1>"

        return b"".join([response_line, response_headers, blank_line, response_body])

    def handle_GET(self, request):
        filename = request.uri.strip('/')
        host = request.headers['Host']

        current_host = [i for i in self.virtual_hosts if i['host'] == host]
        current_host = current_host[0] if len(current_host) > 0 else self.default_host

        if os.path.exists(f'{current_host["resources"]["html"]}/{filename}'):
            response_line = self.response_line(status_code=200)

            content_type = mimetypes.guess_type(filename)[0] or 'text/html'

            extra_headers = {'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

            with open(f'{current_host["resources"]["html"]}/{filename}', 'rb') as f:
                response_body = f.read()
        else:
            response_line = self.response_line(status_code=404)
            response_headers = self.response_headers()
            response_body = b"<h1>404 Not found</h1>"

        blank_line = b"\r\n"

        return b"".join([response_line, response_headers, blank_line, response_body])

    def response_line(self, status_code):
        reason = self.status_codes[str(status_code)]
        line = "HTTP/1.1 %s %s\r\n" % (status_code, reason)

        return line.encode()

    def response_headers(self, extra_headers=None):
        headers_copy = self.headers.copy()

        if extra_headers:
            headers_copy.update(extra_headers)

        headers = ""

        for h in headers_copy:
            headers += "%s: %s\r\n" % (h, headers_copy[h])
        self.logger.logging_info(headers)
        return headers.encode()
