from webserver.service.HTTPServer import HTTPServer
import asyncio

if __name__ == '__main__':
    server = HTTPServer()
    asyncio.run(server.start())
