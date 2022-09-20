# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orders.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
  b'\n\x0corders.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\'\n\x13TradesStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\xaa\x01\n\x14TradesStreamResponse\x12J\n\x0corder_trades\x18\x01 \x01(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.OrderTradesH\x00\x12;\n\x04ping\x18\x02 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x42\t\n\x07payload\"\xfe\x01\n\x0bOrderTrades\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\tdirection\x18\x03 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x0c\n\x04\x66igi\x18\x04 \x01(\t\x12\x41\n\x06trades\x18\x05 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderTrade\x12\x12\n\naccount_id\x18\x06 \x01(\t\"\x8e\x01\n\nOrderTrade\x12-\n\tdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x05price\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x03 \x01(\x03\"\xa9\x02\n\x10PostOrderRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12H\n\tdirection\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x12\n\naccount_id\x18\x05 \x01(\t\x12\x44\n\norder_type\x18\x06 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12\x10\n\x08order_id\x18\x07 \x01(\t\"\xe1\x07\n\x11PostOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\taci_value\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\norder_type\x18\x0e \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12\x0f\n\x07message\x18\x0f \x01(\t\x12P\n\x16initial_order_price_pt\x18\x10 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\":\n\x12\x43\x61ncelOrderRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\"?\n\x13\x43\x61ncelOrderResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x14GetOrderStateRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\"&\n\x10GetOrdersRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"V\n\x11GetOrdersResponse\x12\x41\n\x06orders\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderState\"\xd8\x08\n\nOrderState\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x16\x61verage_position_price\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x41\n\x06stages\x18\x0e \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderStage\x12M\n\x12service_commission\x18\x0f \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08\x63urrency\x18\x10 \x01(\t\x12\x44\n\norder_type\x18\x11 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12.\n\norder_date\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"r\n\nOrderStage\x12@\n\x05price\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12\x10\n\x08trade_id\x18\x03 \x01(\t\"\xed\x01\n\x13ReplaceOrderRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x06 \x01(\t\x12\x17\n\x0fidempotency_key\x18\x07 \x01(\t\x12\x10\n\x08quantity\x18\x0b \x01(\x03\x12?\n\x05price\x18\x0c \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nprice_type\x18\r \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceType*d\n\x0eOrderDirection\x12\x1f\n\x1bORDER_DIRECTION_UNSPECIFIED\x10\x00\x12\x17\n\x13ORDER_DIRECTION_BUY\x10\x01\x12\x18\n\x14ORDER_DIRECTION_SELL\x10\x02*T\n\tOrderType\x12\x1a\n\x16ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10ORDER_TYPE_LIMIT\x10\x01\x12\x15\n\x11ORDER_TYPE_MARKET\x10\x02*\x80\x02\n\x1aOrderExecutionReportStatus\x12\'\n#EXECUTION_REPORT_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1c\x45XECUTION_REPORT_STATUS_FILL\x10\x01\x12$\n EXECUTION_REPORT_STATUS_REJECTED\x10\x02\x12%\n!EXECUTION_REPORT_STATUS_CANCELLED\x10\x03\x12\x1f\n\x1b\x45XECUTION_REPORT_STATUS_NEW\x10\x04\x12)\n%EXECUTION_REPORT_STATUS_PARTIALLYFILL\x10\x05*V\n\tPriceType\x12\x1a\n\x16PRICE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10PRICE_TYPE_POINT\x10\x01\x12\x17\n\x13PRICE_TYPE_CURRENCY\x10\x02\x32\xa1\x01\n\x13OrdersStreamService\x12\x89\x01\n\x0cTradesStream\x12:.tinkoff.public.invest.api.contract.v1.TradesStreamRequest\x1a;.tinkoff.public.invest.api.contract.v1.TradesStreamResponse0\x01\x32\x9e\x05\n\rOrdersService\x12~\n\tPostOrder\x12\x37.tinkoff.public.invest.api.contract.v1.PostOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x84\x01\n\x0b\x43\x61ncelOrder\x12\x39.tinkoff.public.invest.api.contract.v1.CancelOrderRequest\x1a:.tinkoff.public.invest.api.contract.v1.CancelOrderResponse\x12\x7f\n\rGetOrderState\x12;.tinkoff.public.invest.api.contract.v1.GetOrderStateRequest\x1a\x31.tinkoff.public.invest.api.contract.v1.OrderState\x12~\n\tGetOrders\x12\x37.tinkoff.public.invest.api.contract.v1.GetOrdersRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.GetOrdersResponse\x12\x84\x01\n\x0cReplaceOrder\x12:.tinkoff.public.invest.api.contract.v1.ReplaceOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_ORDERDIRECTION = DESCRIPTOR.enum_types_by_name['OrderDirection']
OrderDirection = enum_type_wrapper.EnumTypeWrapper(_ORDERDIRECTION)
_ORDERTYPE = DESCRIPTOR.enum_types_by_name['OrderType']
OrderType = enum_type_wrapper.EnumTypeWrapper(_ORDERTYPE)
_ORDEREXECUTIONREPORTSTATUS = DESCRIPTOR.enum_types_by_name['OrderExecutionReportStatus']
OrderExecutionReportStatus = enum_type_wrapper.EnumTypeWrapper(_ORDEREXECUTIONREPORTSTATUS)
_PRICETYPE = DESCRIPTOR.enum_types_by_name['PriceType']
PriceType = enum_type_wrapper.EnumTypeWrapper(_PRICETYPE)
ORDER_DIRECTION_UNSPECIFIED = 0
ORDER_DIRECTION_BUY = 1
ORDER_DIRECTION_SELL = 2
ORDER_TYPE_UNSPECIFIED = 0
ORDER_TYPE_LIMIT = 1
ORDER_TYPE_MARKET = 2
EXECUTION_REPORT_STATUS_UNSPECIFIED = 0
EXECUTION_REPORT_STATUS_FILL = 1
EXECUTION_REPORT_STATUS_REJECTED = 2
EXECUTION_REPORT_STATUS_CANCELLED = 3
EXECUTION_REPORT_STATUS_NEW = 4
EXECUTION_REPORT_STATUS_PARTIALLYFILL = 5
PRICE_TYPE_UNSPECIFIED = 0
PRICE_TYPE_POINT = 1
PRICE_TYPE_CURRENCY = 2

_TRADESSTREAMREQUEST = DESCRIPTOR.message_types_by_name['TradesStreamRequest']
_TRADESSTREAMRESPONSE = DESCRIPTOR.message_types_by_name['TradesStreamResponse']
_ORDERTRADES = DESCRIPTOR.message_types_by_name['OrderTrades']
_ORDERTRADE = DESCRIPTOR.message_types_by_name['OrderTrade']
_POSTORDERREQUEST = DESCRIPTOR.message_types_by_name['PostOrderRequest']
_POSTORDERRESPONSE = DESCRIPTOR.message_types_by_name['PostOrderResponse']
_CANCELORDERREQUEST = DESCRIPTOR.message_types_by_name['CancelOrderRequest']
_CANCELORDERRESPONSE = DESCRIPTOR.message_types_by_name['CancelOrderResponse']
_GETORDERSTATEREQUEST = DESCRIPTOR.message_types_by_name['GetOrderStateRequest']
_GETORDERSREQUEST = DESCRIPTOR.message_types_by_name['GetOrdersRequest']
_GETORDERSRESPONSE = DESCRIPTOR.message_types_by_name['GetOrdersResponse']
_ORDERSTATE = DESCRIPTOR.message_types_by_name['OrderState']
_ORDERSTAGE = DESCRIPTOR.message_types_by_name['OrderStage']
_REPLACEORDERREQUEST = DESCRIPTOR.message_types_by_name['ReplaceOrderRequest']
TradesStreamRequest = _reflection.GeneratedProtocolMessageType('TradesStreamRequest', (_message.Message,), {
  'DESCRIPTOR': _TRADESSTREAMREQUEST,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.TradesStreamRequest)
  })
_sym_db.RegisterMessage(TradesStreamRequest)

TradesStreamResponse = _reflection.GeneratedProtocolMessageType('TradesStreamResponse', (_message.Message,), {
  'DESCRIPTOR': _TRADESSTREAMRESPONSE,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.TradesStreamResponse)
  })
_sym_db.RegisterMessage(TradesStreamResponse)

OrderTrades = _reflection.GeneratedProtocolMessageType('OrderTrades', (_message.Message,), {
  'DESCRIPTOR': _ORDERTRADES,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OrderTrades)
  })
_sym_db.RegisterMessage(OrderTrades)

OrderTrade = _reflection.GeneratedProtocolMessageType('OrderTrade', (_message.Message,), {
  'DESCRIPTOR': _ORDERTRADE,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OrderTrade)
  })
_sym_db.RegisterMessage(OrderTrade)

PostOrderRequest = _reflection.GeneratedProtocolMessageType('PostOrderRequest', (_message.Message,), {
  'DESCRIPTOR': _POSTORDERREQUEST,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.PostOrderRequest)
  })
_sym_db.RegisterMessage(PostOrderRequest)

PostOrderResponse = _reflection.GeneratedProtocolMessageType('PostOrderResponse', (_message.Message,), {
  'DESCRIPTOR': _POSTORDERRESPONSE,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.PostOrderResponse)
  })
_sym_db.RegisterMessage(PostOrderResponse)

CancelOrderRequest = _reflection.GeneratedProtocolMessageType('CancelOrderRequest', (_message.Message,), {
  'DESCRIPTOR': _CANCELORDERREQUEST,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CancelOrderRequest)
  })
_sym_db.RegisterMessage(CancelOrderRequest)

CancelOrderResponse = _reflection.GeneratedProtocolMessageType('CancelOrderResponse', (_message.Message,), {
  'DESCRIPTOR': _CANCELORDERRESPONSE,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CancelOrderResponse)
  })
_sym_db.RegisterMessage(CancelOrderResponse)

GetOrderStateRequest = _reflection.GeneratedProtocolMessageType('GetOrderStateRequest', (_message.Message,), {
  'DESCRIPTOR': _GETORDERSTATEREQUEST,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetOrderStateRequest)
  })
_sym_db.RegisterMessage(GetOrderStateRequest)

GetOrdersRequest = _reflection.GeneratedProtocolMessageType('GetOrdersRequest', (_message.Message,), {
  'DESCRIPTOR': _GETORDERSREQUEST,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetOrdersRequest)
  })
_sym_db.RegisterMessage(GetOrdersRequest)

GetOrdersResponse = _reflection.GeneratedProtocolMessageType('GetOrdersResponse', (_message.Message,), {
  'DESCRIPTOR': _GETORDERSRESPONSE,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetOrdersResponse)
  })
_sym_db.RegisterMessage(GetOrdersResponse)

OrderState = _reflection.GeneratedProtocolMessageType('OrderState', (_message.Message,), {
  'DESCRIPTOR': _ORDERSTATE,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OrderState)
  })
_sym_db.RegisterMessage(OrderState)

OrderStage = _reflection.GeneratedProtocolMessageType('OrderStage', (_message.Message,), {
  'DESCRIPTOR': _ORDERSTAGE,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OrderStage)
  })
_sym_db.RegisterMessage(OrderStage)

ReplaceOrderRequest = _reflection.GeneratedProtocolMessageType('ReplaceOrderRequest', (_message.Message,), {
  'DESCRIPTOR': _REPLACEORDERREQUEST,
  '__module__': 'orders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.ReplaceOrderRequest)
  })
_sym_db.RegisterMessage(ReplaceOrderRequest)

_ORDERSSTREAMSERVICE = DESCRIPTOR.services_by_name['OrdersStreamService']
_ORDERSSERVICE = DESCRIPTOR.services_by_name['OrdersService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _ORDERDIRECTION._serialized_start = 3800
  _ORDERDIRECTION._serialized_end = 3900
  _ORDERTYPE._serialized_start = 3902
  _ORDERTYPE._serialized_end = 3986
  _ORDEREXECUTIONREPORTSTATUS._serialized_start = 3989
  _ORDEREXECUTIONREPORTSTATUS._serialized_end = 4245
  _PRICETYPE._serialized_start = 4247
  _PRICETYPE._serialized_end = 4333
  _TRADESSTREAMREQUEST._serialized_start = 102
  _TRADESSTREAMREQUEST._serialized_end = 141
  _TRADESSTREAMRESPONSE._serialized_start = 144
  _TRADESSTREAMRESPONSE._serialized_end = 314
  _ORDERTRADES._serialized_start = 317
  _ORDERTRADES._serialized_end = 571
  _ORDERTRADE._serialized_start = 574
  _ORDERTRADE._serialized_end = 716
  _POSTORDERREQUEST._serialized_start = 719
  _POSTORDERREQUEST._serialized_end = 1016
  _POSTORDERRESPONSE._serialized_start = 1019
  _POSTORDERRESPONSE._serialized_end = 2012
  _CANCELORDERREQUEST._serialized_start = 2014
  _CANCELORDERREQUEST._serialized_end = 2072
  _CANCELORDERRESPONSE._serialized_start = 2074
  _CANCELORDERRESPONSE._serialized_end = 2137
  _GETORDERSTATEREQUEST._serialized_start = 2139
  _GETORDERSTATEREQUEST._serialized_end = 2199
  _GETORDERSREQUEST._serialized_start = 2201
  _GETORDERSREQUEST._serialized_end = 2239
  _GETORDERSRESPONSE._serialized_start = 2241
  _GETORDERSRESPONSE._serialized_end = 2327
  _ORDERSTATE._serialized_start = 2330
  _ORDERSTATE._serialized_end = 3442
  _ORDERSTAGE._serialized_start = 3444
  _ORDERSTAGE._serialized_end = 3558
  _REPLACEORDERREQUEST._serialized_start = 3561
  _REPLACEORDERREQUEST._serialized_end = 3798
  _ORDERSSTREAMSERVICE._serialized_start = 4336
  _ORDERSSTREAMSERVICE._serialized_end = 4497
  _ORDERSSERVICE._serialized_start = 4500
  _ORDERSSERVICE._serialized_end = 5170
# @@protoc_insertion_point(module_scope)
