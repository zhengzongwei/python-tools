#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/6 10:37                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from __future__ import print_function
import logging
import grpc
import serve_pb2
import serve_pb2_grpc


def run():
    print("Starting RPC server...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = serve_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(serve_pb2.HelloRequest(name="World"))
    print("RPC client received: {}".format(response.message))


if __name__ == '__main__':
    logging.basicConfig()
    run()
