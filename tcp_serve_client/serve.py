import socket
import json
import os
from time import ctime


class Serve(object):
    BUF_SIZE = 1024

    def __init__(self, host: str = "", port: int = 9527):
        self.addr = None
        self.conn = None
        self.serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serve.bind((host, port))
        self.serve.listen()

    def run(self):
        while True:
            print("[server] waiting for connecting...")
            self.conn, self.addr = self.serve.accept()
            print("[server] connecting from %s:%s..." % (self.addr[0], self.addr[1]))
            with self.conn:
                data = self.conn.recv(self.BUF_SIZE).decode()

                if not data:
                    print("[server] connect interrupted，exit...")
                    break

                if data == "exit":
                    print("[server] command interrupted，exit...")
                    break
                msg = "[server] <%s> success got the data: %s" % (ctime(), data)
                self.conn.send(msg.encode())
            self.conn.close()

    def parse_command(self, command: dict):

        pass

    def __del__(self):
        print("[server] Close serve socket")
        if self.serve:
            self.serve.close()


if __name__ == '__main__':
    serve = Serve()
    serve.run()
