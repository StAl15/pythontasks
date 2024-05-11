class HTTPRequest:
    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = "1.1"
        self.headers = dict()

        self.parse(data)

    def parse(self, data):
        lines = data.split(b"\r\n")

        request_line = lines[0]

        words = request_line.split(b" ")

        self.method = words[0].decode()

        if len(words) > 1:
            self.uri = words[1].decode()

        if len(words) > 2:
            self.http_version = words[2]

        if len(lines) > 1:
            tmp_headers = list(map(lambda x: x.decode().strip().split(":"), lines[1:len(lines) - 2]))
            self.headers = {i[0]: i[1].strip() for i in tmp_headers}
        return True
