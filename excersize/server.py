import socket

from excersize.request_handler import RequestHandler


class Server:
    @staticmethod
    def start():
        s = socket.socket()
        host = socket.gethostname()
        port = 1380
        s.bind((host, port))
        s.listen(5)
        while True:
            c, addr = s.accept()
            RequestHandler(c).start()


Server.start()
