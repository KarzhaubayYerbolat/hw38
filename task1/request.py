class Request:
    def __init__(self, rfile):
        self.file = rfile

        self.method = None
        self.uri = None
        self.protocol = None
        self.headers = {}
        self.body = None

        self.__parse_request_line()
        self.__parse_headers()
        self.__parse_body()

    def __parse_request_line(self):
        request_line = self.__readline()
        # GET / HTTP/1.1    ['GET', '/', 'HTTP/1.1']
        
        self.method, self.uri, self.protocol = request_line.split()

    def __readline(self):
        return self.file.readline().decode().strip()

    def __parse_headers(self):
        while True:
            header = self.__readline()
            
            if header == '':
                break

            name, value = header.split(': ')
            self.headers[name] = value

    def __parse_body(self):
        if 'Content-Length' in self.headers:
            content_length = int(self.headers['Content-Length'])
            self.body = self.file.read(content_length)

    def __str__(self):
        return (
            f'{"-" * 30}\n'
            f'{self.method} {self.uri}'
        )
