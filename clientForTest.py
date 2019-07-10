from __future__ import print_function
import logging

import grpc

import the_pb2
import the_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('dk.gribgp.com:50051') as channel:
        stub = the_pb2_grpc.QueryIDStub(channel)
        response = stub.Query(the_pb2.IsbnRequest(isbn='920910201209'))
        print("Greeter client received: " + response.url)


if __name__ == '__main__':
    logging.basicConfig()
    run()
