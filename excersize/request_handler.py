import threading
from socket import socket

from excersize.controller import Controller


class RequestHandler(threading.Thread):
    def __init__(self, sock: socket):
        threading.Thread.__init__(self)
        self.sock: socket = sock

    def send(self, message: str | float):
        self.sock.send(str(message).encode())

    def run(self):
        while True:
            request_body = self.sock.recv(4096)

            args = request_body.decode().split(' ')

            if args[0] == "exit":
                self.sock.close()
                break

            self.send(Controller.calculate(args))

    def join(self, timeout: float | None = ...) -> None:
        self.sock.close()
        super().join(timeout)
