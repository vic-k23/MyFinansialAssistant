# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import stoporders_pb2 as stoporders__pb2


class StopOrdersServiceStub(object):
    """Сервис предназначен для работы со стоп-заявками:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение списка стоп-заявок.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PostStopOrder = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.StopOrdersService/PostStopOrder',
                request_serializer=stoporders__pb2.PostStopOrderRequest.SerializeToString,
                response_deserializer=stoporders__pb2.PostStopOrderResponse.FromString,
                )
        self.GetStopOrders = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.StopOrdersService/GetStopOrders',
                request_serializer=stoporders__pb2.GetStopOrdersRequest.SerializeToString,
                response_deserializer=stoporders__pb2.GetStopOrdersResponse.FromString,
                )
        self.CancelStopOrder = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.StopOrdersService/CancelStopOrder',
                request_serializer=stoporders__pb2.CancelStopOrderRequest.SerializeToString,
                response_deserializer=stoporders__pb2.CancelStopOrderResponse.FromString,
                )


class StopOrdersServiceServicer(object):
    """Сервис предназначен для работы со стоп-заявками:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение списка стоп-заявок.
    """

    def PostStopOrder(self, request, context):
        """Метод выставления стоп-заявки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStopOrders(self, request, context):
        """Метод получения списка активных стоп заявок по счёту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelStopOrder(self, request, context):
        """Метод отмены стоп-заявки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StopOrdersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'PostStopOrder': grpc.unary_unary_rpc_method_handler(
                servicer.PostStopOrder,
                request_deserializer=stoporders__pb2.PostStopOrderRequest.FromString,
                response_serializer=stoporders__pb2.PostStopOrderResponse.SerializeToString,
                ),
        'GetStopOrders': grpc.unary_unary_rpc_method_handler(
                servicer.GetStopOrders,
                request_deserializer=stoporders__pb2.GetStopOrdersRequest.FromString,
                response_serializer=stoporders__pb2.GetStopOrdersResponse.SerializeToString,
                ),
        'CancelStopOrder': grpc.unary_unary_rpc_method_handler(
                servicer.CancelStopOrder,
                request_deserializer=stoporders__pb2.CancelStopOrderRequest.FromString,
                response_serializer=stoporders__pb2.CancelStopOrderResponse.SerializeToString,
                ),
        }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.StopOrdersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class StopOrdersService(object):
    """Сервис предназначен для работы со стоп-заявками:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение списка стоп-заявок.
    """

    @staticmethod
    def PostStopOrder(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target,
                                             '/tinkoff.public.invest.api.contract.v1.StopOrdersService/PostStopOrder',
                                             stoporders__pb2.PostStopOrderRequest.SerializeToString,
                                             stoporders__pb2.PostStopOrderResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStopOrders(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target,
                                             '/tinkoff.public.invest.api.contract.v1.StopOrdersService/GetStopOrders',
                                             stoporders__pb2.GetStopOrdersRequest.SerializeToString,
                                             stoporders__pb2.GetStopOrdersResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelStopOrder(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target,
                                             '/tinkoff.public.invest.api.contract.v1.StopOrdersService/CancelStopOrder',
                                             stoporders__pb2.CancelStopOrderRequest.SerializeToString,
                                             stoporders__pb2.CancelStopOrderResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
