# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy_service.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from google.protobuf.empty_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
    name='proxy_service.proto',
  package='proxy_service',
  syntax='proto3',
    serialized_pb=_b(
        '\n\x13proxy_service.proto\x12\rproxy_service\x1a\x1bgoogle/protobuf/empty.proto\"(\n\x14RegisterAgentRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\"<\n\x15RegisterAgentResponse\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x03\x12\x11\n\tproxy_url\x18\x02 \x01(\t\"5\n\x13RegisterPathRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\"\'\n\x14RegisterPathResponse\x12\x0f\n\x07path_id\x18\x01 \x01(\x03\"\x1d\n\tAgentInfo\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x03\"B\n\rScrapeRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x03\x12\x11\n\tscrape_id\x18\x02 \x01(\x03\x12\x0c\n\x04path\x18\x03 \x01(\t\"g\n\x0eScrapeResponse\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x03\x12\x11\n\tscrape_id\x18\x02 \x01(\x03\x12\r\n\x05valid\x18\x03 \x01(\x08\x12\x13\n\x0bstatus_code\x18\x04 \x01(\x05\x12\x0c\n\x04text\x18\x05 \x01(\t2\xed\x02\n\x0cProxyService\x12\\\n\rregisterAgent\x12#.proxy_service.RegisterAgentRequest\x1a$.proxy_service.RegisterAgentResponse\"\x00\x12Y\n\x0cregisterPath\x12\".proxy_service.RegisterPathRequest\x1a#.proxy_service.RegisterPathResponse\"\x00\x12S\n\x15readRequestsFromProxy\x12\x18.proxy_service.AgentInfo\x1a\x1c.proxy_service.ScrapeRequest\"\x00\x30\x01\x12O\n\x14writeResponseToProxy\x12\x1d.proxy_service.ScrapeResponse\x1a\x16.google.protobuf.Empty\"\x00\x42\x12\n\x0e\x63om.cinch.grpcP\x01P\x00\x62\x06proto3')
    ,
    dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR, ],
    public_dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR, ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_REGISTERAGENTREQUEST = _descriptor.Descriptor(
    name='RegisterAgentRequest',
    full_name='proxy_service.RegisterAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
        name='hostname', full_name='proxy_service.RegisterAgentRequest.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
    serialized_start=67,
    serialized_end=107,
)

_REGISTERAGENTRESPONSE = _descriptor.Descriptor(
    name='RegisterAgentResponse',
    full_name='proxy_service.RegisterAgentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
        name='agent_id', full_name='proxy_service.RegisterAgentResponse.agent_id', index=0,
        number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
        name='proxy_url', full_name='proxy_service.RegisterAgentResponse.proxy_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
    serialized_start=109,
    serialized_end=169,
)

_REGISTERPATHREQUEST = _descriptor.Descriptor(
    name='RegisterPathRequest',
    full_name='proxy_service.RegisterPathRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
        name='agent_id', full_name='proxy_service.RegisterPathRequest.agent_id', index=0,
        number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
        name='path', full_name='proxy_service.RegisterPathRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
    serialized_start=171,
    serialized_end=224,
)

_REGISTERPATHRESPONSE = _descriptor.Descriptor(
    name='RegisterPathResponse',
    full_name='proxy_service.RegisterPathResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
        name='path_id', full_name='proxy_service.RegisterPathResponse.path_id', index=0,
        number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
    serialized_start=226,
    serialized_end=265,
)


_AGENTINFO = _descriptor.Descriptor(
  name='AgentInfo',
  full_name='proxy_service.AgentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='proxy_service.AgentInfo.agent_id', index=0,
        number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
    serialized_start=267,
    serialized_end=296,
)


_SCRAPEREQUEST = _descriptor.Descriptor(
  name='ScrapeRequest',
  full_name='proxy_service.ScrapeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='proxy_service.ScrapeRequest.agent_id', index=0,
        number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scrape_id', full_name='proxy_service.ScrapeRequest.scrape_id', index=1,
        number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='proxy_service.ScrapeRequest.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
    serialized_start=298,
    serialized_end=364,
)


_SCRAPERESPONSE = _descriptor.Descriptor(
  name='ScrapeResponse',
  full_name='proxy_service.ScrapeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='proxy_service.ScrapeResponse.agent_id', index=0,
        number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scrape_id', full_name='proxy_service.ScrapeResponse.scrape_id', index=1,
        number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid', full_name='proxy_service.ScrapeResponse.valid', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='proxy_service.ScrapeResponse.status_code', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='proxy_service.ScrapeResponse.text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
    serialized_start=366,
    serialized_end=469,
)

DESCRIPTOR.message_types_by_name['RegisterAgentRequest'] = _REGISTERAGENTREQUEST
DESCRIPTOR.message_types_by_name['RegisterAgentResponse'] = _REGISTERAGENTRESPONSE
DESCRIPTOR.message_types_by_name['RegisterPathRequest'] = _REGISTERPATHREQUEST
DESCRIPTOR.message_types_by_name['RegisterPathResponse'] = _REGISTERPATHRESPONSE
DESCRIPTOR.message_types_by_name['AgentInfo'] = _AGENTINFO
DESCRIPTOR.message_types_by_name['ScrapeRequest'] = _SCRAPEREQUEST
DESCRIPTOR.message_types_by_name['ScrapeResponse'] = _SCRAPERESPONSE

RegisterAgentRequest = _reflection.GeneratedProtocolMessageType('RegisterAgentRequest', (_message.Message,), dict(
    DESCRIPTOR=_REGISTERAGENTREQUEST,
    __module__='proxy_service_pb2'
    # @@protoc_insertion_point(class_scope:proxy_service.RegisterAgentRequest)
))
_sym_db.RegisterMessage(RegisterAgentRequest)

RegisterAgentResponse = _reflection.GeneratedProtocolMessageType('RegisterAgentResponse', (_message.Message,), dict(
    DESCRIPTOR=_REGISTERAGENTRESPONSE,
    __module__='proxy_service_pb2'
    # @@protoc_insertion_point(class_scope:proxy_service.RegisterAgentResponse)
))
_sym_db.RegisterMessage(RegisterAgentResponse)

RegisterPathRequest = _reflection.GeneratedProtocolMessageType('RegisterPathRequest', (_message.Message,), dict(
    DESCRIPTOR=_REGISTERPATHREQUEST,
    __module__='proxy_service_pb2'
    # @@protoc_insertion_point(class_scope:proxy_service.RegisterPathRequest)
))
_sym_db.RegisterMessage(RegisterPathRequest)

RegisterPathResponse = _reflection.GeneratedProtocolMessageType('RegisterPathResponse', (_message.Message,), dict(
    DESCRIPTOR=_REGISTERPATHRESPONSE,
    __module__='proxy_service_pb2'
    # @@protoc_insertion_point(class_scope:proxy_service.RegisterPathResponse)
))
_sym_db.RegisterMessage(RegisterPathResponse)

AgentInfo = _reflection.GeneratedProtocolMessageType('AgentInfo', (_message.Message,), dict(
    DESCRIPTOR=_AGENTINFO,
    __module__='proxy_service_pb2'
  # @@protoc_insertion_point(class_scope:proxy_service.AgentInfo)
))
_sym_db.RegisterMessage(AgentInfo)

ScrapeRequest = _reflection.GeneratedProtocolMessageType('ScrapeRequest', (_message.Message,), dict(
    DESCRIPTOR=_SCRAPEREQUEST,
    __module__='proxy_service_pb2'
  # @@protoc_insertion_point(class_scope:proxy_service.ScrapeRequest)
))
_sym_db.RegisterMessage(ScrapeRequest)

ScrapeResponse = _reflection.GeneratedProtocolMessageType('ScrapeResponse', (_message.Message,), dict(
    DESCRIPTOR=_SCRAPERESPONSE,
    __module__='proxy_service_pb2'
  # @@protoc_insertion_point(class_scope:proxy_service.ScrapeResponse)
))
_sym_db.RegisterMessage(ScrapeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.cinch.grpcP\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class ProxyServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.registerAgent = channel.unary_unary(
          '/proxy_service.ProxyService/registerAgent',
          request_serializer=RegisterAgentRequest.SerializeToString,
          response_deserializer=RegisterAgentResponse.FromString,
      )
      self.registerPath = channel.unary_unary(
          '/proxy_service.ProxyService/registerPath',
          request_serializer=RegisterPathRequest.SerializeToString,
          response_deserializer=RegisterPathResponse.FromString,
      )
      self.readRequestsFromProxy = channel.unary_stream(
          '/proxy_service.ProxyService/readRequestsFromProxy',
          request_serializer=AgentInfo.SerializeToString,
          response_deserializer=ScrapeRequest.FromString,
      )
      self.writeResponseToProxy = channel.unary_unary(
          '/proxy_service.ProxyService/writeResponseToProxy',
          request_serializer=ScrapeResponse.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      )


  class ProxyServiceServicer(object):

    def registerAgent(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def registerPath(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def readRequestsFromProxy(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def writeResponseToProxy(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_ProxyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'registerAgent': grpc.unary_unary_rpc_method_handler(
            servicer.registerAgent,
            request_deserializer=RegisterAgentRequest.FromString,
            response_serializer=RegisterAgentResponse.SerializeToString,
        ),
        'registerPath': grpc.unary_unary_rpc_method_handler(
            servicer.registerPath,
            request_deserializer=RegisterPathRequest.FromString,
            response_serializer=RegisterPathResponse.SerializeToString,
        ),
        'readRequestsFromProxy': grpc.unary_stream_rpc_method_handler(
            servicer.readRequestsFromProxy,
            request_deserializer=AgentInfo.FromString,
            response_serializer=ScrapeRequest.SerializeToString,
        ),
        'writeResponseToProxy': grpc.unary_unary_rpc_method_handler(
            servicer.writeResponseToProxy,
            request_deserializer=ScrapeResponse.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'proxy_service.ProxyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaProxyServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def registerAgent(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def registerPath(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def readRequestsFromProxy(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def writeResponseToProxy(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaProxyServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def registerAgent(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    registerAgent.future = None
    def registerPath(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    registerPath.future = None
    def readRequestsFromProxy(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    def writeResponseToProxy(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    writeResponseToProxy.future = None


  def beta_create_ProxyService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('proxy_service.ProxyService', 'readRequestsFromProxy'): AgentInfo.FromString,
        ('proxy_service.ProxyService', 'registerAgent'): RegisterAgentRequest.FromString,
        ('proxy_service.ProxyService', 'registerPath'): RegisterPathRequest.FromString,
      ('proxy_service.ProxyService', 'writeResponseToProxy'): ScrapeResponse.FromString,
    }
    response_serializers = {
      ('proxy_service.ProxyService', 'readRequestsFromProxy'): ScrapeRequest.SerializeToString,
        ('proxy_service.ProxyService', 'registerAgent'): RegisterAgentResponse.SerializeToString,
        ('proxy_service.ProxyService', 'registerPath'): RegisterPathResponse.SerializeToString,
        ('proxy_service.ProxyService',
         'writeResponseToProxy'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
    }
    method_implementations = {
        ('proxy_service.ProxyService', 'readRequestsFromProxy'): face_utilities.unary_stream_inline(
            servicer.readRequestsFromProxy),
      ('proxy_service.ProxyService', 'registerAgent'): face_utilities.unary_unary_inline(servicer.registerAgent),
      ('proxy_service.ProxyService', 'registerPath'): face_utilities.unary_unary_inline(servicer.registerPath),
        ('proxy_service.ProxyService', 'writeResponseToProxy'): face_utilities.unary_unary_inline(
            servicer.writeResponseToProxy),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers,
                                                         response_serializers=response_serializers, thread_pool=pool,
                                                         thread_pool_size=pool_size, default_timeout=default_timeout,
                                                         maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_ProxyService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('proxy_service.ProxyService', 'readRequestsFromProxy'): AgentInfo.SerializeToString,
        ('proxy_service.ProxyService', 'registerAgent'): RegisterAgentRequest.SerializeToString,
        ('proxy_service.ProxyService', 'registerPath'): RegisterPathRequest.SerializeToString,
      ('proxy_service.ProxyService', 'writeResponseToProxy'): ScrapeResponse.SerializeToString,
    }
    response_deserializers = {
      ('proxy_service.ProxyService', 'readRequestsFromProxy'): ScrapeRequest.FromString,
        ('proxy_service.ProxyService', 'registerAgent'): RegisterAgentResponse.FromString,
        ('proxy_service.ProxyService', 'registerPath'): RegisterPathResponse.FromString,
        ('proxy_service.ProxyService', 'writeResponseToProxy'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
    }
    cardinalities = {
      'readRequestsFromProxy': cardinality.Cardinality.UNARY_STREAM,
      'registerAgent': cardinality.Cardinality.UNARY_UNARY,
      'registerPath': cardinality.Cardinality.UNARY_UNARY,
      'writeResponseToProxy': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer,
                                                     request_serializers=request_serializers,
                                                     response_deserializers=response_deserializers, thread_pool=pool,
                                                     thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'proxy_service.ProxyService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)