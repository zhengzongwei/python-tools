import socket
import json
import os
from time import ctime


def dict2json(data: dict) -> str:
    data = json.dumps(data)
    return data


def json2dict(data: str) -> dict:
    print(data, 'json2dict')
    data = json.loads(data)
    return data


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

                data_dict = eval(data)
                # 解析命令
                data = self.parse_command(data_dict)
                data_str = repr(data)

                if data == "exit":
                    print("[server] command interrupted，exit...")
                    break
                msg = "[server] <%s> success got the data: %s" % (ctime(), data_str)
                self.conn.send(msg.encode())
            self.conn.close()


    def parse_command(self, data: dict):
        data_type = data['type']

        if data_type == "input_command":
            command = data['data']
            return command

        if data_type == "exit":
            print("[server] command interrupted，exit...")
            return data_type

    def __del__(self):
        print("[server] Close serve socket")
        if self.serve:
            self.serve.close()


if __name__ == '__main__':
    serve = Serve()
    serve.run()
