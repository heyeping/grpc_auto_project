# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf_grpc import Base_pb2 as Base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Auth.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\036com.aylaasia.referenceapp.grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nAuth.proto\x1a\nBase.proto\"$\n\x13VerificationCodeReq\x12\r\n\x05phone\x18\x01 \x01(\t\"3\n\x08LoginReq\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x18\n\x10verificationCode\x18\x02 \x01(\t\"D\n\x05Token\x12\x11\n\tauthToken\x18\x01 \x01(\t\x12\x14\n\x0crefreshToken\x18\x02 \x01(\t\x12\x12\n\nexpireTime\x18\x03 \x01(\x03\"\'\n\x0fRefreshTokenReq\x12\x14\n\x0crefreshToken\x18\x01 \x01(\t2\x8a\x01\n\x0b\x41uthService\x12\x35\n\x14sendVerificationCode\x12\x14.VerificationCodeReq\x1a\x07.Result\x12\x1a\n\x05login\x12\t.LoginReq\x1a\x06.Token\x12(\n\x0crefreshToken\x12\x10.RefreshTokenReq\x1a\x06.TokenB \n\x1e\x63om.aylaasia.referenceapp.grpcb\x06proto3'
  ,
  dependencies=[Base__pb2.DESCRIPTOR,])




_VERIFICATIONCODEREQ = _descriptor.Descriptor(
  name='VerificationCodeReq',
  full_name='VerificationCodeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='VerificationCodeReq.phone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=62,
)


_LOGINREQ = _descriptor.Descriptor(
  name='LoginReq',
  full_name='LoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='LoginReq.phone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verificationCode', full_name='LoginReq.verificationCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=115,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authToken', full_name='Token.authToken', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refreshToken', full_name='Token.refreshToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expireTime', full_name='Token.expireTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=185,
)


_REFRESHTOKENREQ = _descriptor.Descriptor(
  name='RefreshTokenReq',
  full_name='RefreshTokenReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='refreshToken', full_name='RefreshTokenReq.refreshToken', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=226,
)

DESCRIPTOR.message_types_by_name['VerificationCodeReq'] = _VERIFICATIONCODEREQ
DESCRIPTOR.message_types_by_name['LoginReq'] = _LOGINREQ
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['RefreshTokenReq'] = _REFRESHTOKENREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VerificationCodeReq = _reflection.GeneratedProtocolMessageType('VerificationCodeReq', (_message.Message,), {
  'DESCRIPTOR' : _VERIFICATIONCODEREQ,
  '__module__' : 'Auth_pb2'
  # @@protoc_insertion_point(class_scope:VerificationCodeReq)
  })
_sym_db.RegisterMessage(VerificationCodeReq)

LoginReq = _reflection.GeneratedProtocolMessageType('LoginReq', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQ,
  '__module__' : 'Auth_pb2'
  # @@protoc_insertion_point(class_scope:LoginReq)
  })
_sym_db.RegisterMessage(LoginReq)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'Auth_pb2'
  # @@protoc_insertion_point(class_scope:Token)
  })
_sym_db.RegisterMessage(Token)

RefreshTokenReq = _reflection.GeneratedProtocolMessageType('RefreshTokenReq', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHTOKENREQ,
  '__module__' : 'Auth_pb2'
  # @@protoc_insertion_point(class_scope:RefreshTokenReq)
  })
_sym_db.RegisterMessage(RefreshTokenReq)


DESCRIPTOR._options = None

_AUTHSERVICE = _descriptor.ServiceDescriptor(
  name='AuthService',
  full_name='AuthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=229,
  serialized_end=367,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendVerificationCode',
    full_name='AuthService.sendVerificationCode',
    index=0,
    containing_service=None,
    input_type=_VERIFICATIONCODEREQ,
    output_type=Base__pb2._RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='login',
    full_name='AuthService.login',
    index=1,
    containing_service=None,
    input_type=_LOGINREQ,
    output_type=_TOKEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='refreshToken',
    full_name='AuthService.refreshToken',
    index=2,
    containing_service=None,
    input_type=_REFRESHTOKENREQ,
    output_type=_TOKEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSERVICE)

DESCRIPTOR.services_by_name['AuthService'] = _AUTHSERVICE

# @@protoc_insertion_point(module_scope)
