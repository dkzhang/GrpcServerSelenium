# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import the_pb2 as the__pb2


class QueryIDStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Query = channel.unary_unary(
        '/queryDouBanID.QueryID/Query',
        request_serializer=the__pb2.IsbnRequest.SerializeToString,
        response_deserializer=the__pb2.IdUrlReply.FromString,
        )


class QueryIDServicer(object):
  """The greeting service definition.
  """

  def Query(self, request, context):
    """Sends a query
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryIDServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=the__pb2.IsbnRequest.FromString,
          response_serializer=the__pb2.IdUrlReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'queryDouBanID.QueryID', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))