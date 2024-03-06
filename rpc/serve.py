#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/6 10:37                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
import logging
from concurrent import futures
import grpc
import serve_pb2
import serve_pb2_grpc


class Greeter(serve_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return serve_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serve_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()

    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
