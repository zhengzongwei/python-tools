import socket


class Client(object):
    BUF_SIZE = 1024

    def __init__(self, host: str = "127.0.0.1", port: int = 9527):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def run(self, data: str):
        with self.client:
            self.client.sendall(data.encode())
            recv_data = self.client.recv(self.BUF_SIZE)
            if not recv_data:
                print("[client] no recv data")
            print("[client] recv data: %s" % recv_data.decode())

    def input_command(self):
        message = {'type': "input_command"}
        input_data = input("[client]input message to send >")

        if not input_data:
            print("[client] no input info")
        message['data'] = input_data
        self.run(repr(message))

    def __del__(self):
        print("[client] Close client socket")
        if self.client:
            self.client.close()


if __name__ == '__main__':
    client = Client()
    # client.run(b"hello workd")
    client.input_command()
