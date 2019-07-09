from concurrent import futures
import time
import logging

import grpc

import the_pb2
import the_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class QueryID(the_pb2_grpc.QueryIDServicer):

    def Query(self, request, context):
        return the_pb2.IdUrlReply(url='Hello, %s!' % request.isbn)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    the_pb2_grpc.add_QueryIDServicer_to_server(QueryID(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()

