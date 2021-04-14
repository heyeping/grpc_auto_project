# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DeviceService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import Base_pb2 as Base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DeviceService.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\036com.aylaasia.referenceapp.grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x44\x65viceService.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\nBase.proto\"A\n\rBindDeviceReq\x12\x0c\n\x04\x63uId\x18\x01 \x01(\x05\x12\x10\n\x08\x64\x65viceId\x18\x02 \x01(\t\x12\x10\n\x08nickName\x18\x03 \x01(\t\"*\n\x0e\x44\x65viceListResp\x12\x18\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x07.Device\"\x1d\n\tDeviceReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\"\x89\x01\n\x06\x44\x65vice\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x10\n\x08nickName\x18\x02 \x01(\t\x12\x18\n\x10\x63onnectionStatus\x18\x03 \x01(\t\x12\x17\n\x0f\x66irmwareVersion\x18\x04 \x01(\t\x12\x12\n\nmacAddress\x18\x05 \x01(\t\x12\x14\n\x0c\x63onnectivity\x18\x06 \x01(\t\"#\n\x0fUnBindDeviceReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\"4\n\x10UnBindDeviceResp\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\"U\n\x14SetDevicePropertyReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x14\n\x0cpropertyName\x18\x02 \x01(\t\x12\x15\n\rpropertyValue\x18\x03 \x01(\t\">\n\x14GetDevicePropertyReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x14\n\x0cpropertyName\x18\x02 \x01(\t\"O\n\x12\x44\x65vicePropertyResp\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\'\n\x0e\x64\x65viceProperty\x18\x02 \x01(\x0b\x32\x0f.DeviceProperty\"*\n\x16GetDevicePropertiesReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\"D\n\x17GetDevicePropertiesResp\x12)\n\x10\x64\x65viceProperties\x18\x01 \x03(\x0b\x32\x0f.DeviceProperty\"=\n\x0e\x44\x65viceProperty\x12\x14\n\x0cpropertyName\x18\x01 \x01(\t\x12\x15\n\rpropertyValue\x18\x02 \x01(\t\"5\n\x0fUpdateDeviceReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x10\n\x08nickName\x18\x02 \x01(\t2\xb6\x03\n\rDeviceService\x12%\n\nbindDevice\x12\x0e.BindDeviceReq\x1a\x07.Result\x12\x38\n\rgetDeviceList\x12\x16.google.protobuf.Empty\x1a\x0f.DeviceListResp\x12$\n\rgetDeviceInfo\x12\n.DeviceReq\x1a\x07.Device\x12\x33\n\x0cunBindDevice\x12\x10.UnBindDeviceReq\x1a\x11.UnBindDeviceResp\x12\x33\n\x11setDeviceProperty\x12\x15.SetDevicePropertyReq\x1a\x07.Result\x12?\n\x11getDeviceProperty\x12\x15.GetDevicePropertyReq\x1a\x13.DevicePropertyResp\x12H\n\x13getDeviceProperties\x12\x17.GetDevicePropertiesReq\x1a\x18.GetDevicePropertiesResp\x12)\n\x0cupdateDevice\x12\x10.UpdateDeviceReq\x1a\x07.DeviceB \n\x1e\x63om.aylaasia.referenceapp.grpcb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,Base__pb2.DESCRIPTOR,])




_BINDDEVICEREQ = _descriptor.Descriptor(
  name='BindDeviceReq',
  full_name='BindDeviceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cuId', full_name='BindDeviceReq.cuId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='BindDeviceReq.deviceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='BindDeviceReq.nickName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_end=129,
)


_DEVICELISTRESP = _descriptor.Descriptor(
  name='DeviceListResp',
  full_name='DeviceListResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='devices', full_name='DeviceListResp.devices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=131,
  serialized_end=173,
)


_DEVICEREQ = _descriptor.Descriptor(
  name='DeviceReq',
  full_name='DeviceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='DeviceReq.deviceId', index=0,
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
  serialized_start=175,
  serialized_end=204,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='Device.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='Device.nickName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connectionStatus', full_name='Device.connectionStatus', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firmwareVersion', full_name='Device.firmwareVersion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='macAddress', full_name='Device.macAddress', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connectivity', full_name='Device.connectivity', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=207,
  serialized_end=344,
)


_UNBINDDEVICEREQ = _descriptor.Descriptor(
  name='UnBindDeviceReq',
  full_name='UnBindDeviceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='UnBindDeviceReq.deviceId', index=0,
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
  serialized_start=346,
  serialized_end=381,
)


_UNBINDDEVICERESP = _descriptor.Descriptor(
  name='UnBindDeviceResp',
  full_name='UnBindDeviceResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='UnBindDeviceResp.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='UnBindDeviceResp.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=383,
  serialized_end=435,
)


_SETDEVICEPROPERTYREQ = _descriptor.Descriptor(
  name='SetDevicePropertyReq',
  full_name='SetDevicePropertyReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='SetDevicePropertyReq.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propertyName', full_name='SetDevicePropertyReq.propertyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propertyValue', full_name='SetDevicePropertyReq.propertyValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=437,
  serialized_end=522,
)


_GETDEVICEPROPERTYREQ = _descriptor.Descriptor(
  name='GetDevicePropertyReq',
  full_name='GetDevicePropertyReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='GetDevicePropertyReq.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propertyName', full_name='GetDevicePropertyReq.propertyName', index=1,
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
  serialized_start=524,
  serialized_end=586,
)


_DEVICEPROPERTYRESP = _descriptor.Descriptor(
  name='DevicePropertyResp',
  full_name='DevicePropertyResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='DevicePropertyResp.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceProperty', full_name='DevicePropertyResp.deviceProperty', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=588,
  serialized_end=667,
)


_GETDEVICEPROPERTIESREQ = _descriptor.Descriptor(
  name='GetDevicePropertiesReq',
  full_name='GetDevicePropertiesReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='GetDevicePropertiesReq.deviceId', index=0,
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
  serialized_start=669,
  serialized_end=711,
)


_GETDEVICEPROPERTIESRESP = _descriptor.Descriptor(
  name='GetDevicePropertiesResp',
  full_name='GetDevicePropertiesResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceProperties', full_name='GetDevicePropertiesResp.deviceProperties', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=713,
  serialized_end=781,
)


_DEVICEPROPERTY = _descriptor.Descriptor(
  name='DeviceProperty',
  full_name='DeviceProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='propertyName', full_name='DeviceProperty.propertyName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propertyValue', full_name='DeviceProperty.propertyValue', index=1,
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
  serialized_start=783,
  serialized_end=844,
)


_UPDATEDEVICEREQ = _descriptor.Descriptor(
  name='UpdateDeviceReq',
  full_name='UpdateDeviceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='UpdateDeviceReq.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='UpdateDeviceReq.nickName', index=1,
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
  serialized_start=846,
  serialized_end=899,
)

_DEVICELISTRESP.fields_by_name['devices'].message_type = _DEVICE
_DEVICEPROPERTYRESP.fields_by_name['deviceProperty'].message_type = _DEVICEPROPERTY
_GETDEVICEPROPERTIESRESP.fields_by_name['deviceProperties'].message_type = _DEVICEPROPERTY
DESCRIPTOR.message_types_by_name['BindDeviceReq'] = _BINDDEVICEREQ
DESCRIPTOR.message_types_by_name['DeviceListResp'] = _DEVICELISTRESP
DESCRIPTOR.message_types_by_name['DeviceReq'] = _DEVICEREQ
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['UnBindDeviceReq'] = _UNBINDDEVICEREQ
DESCRIPTOR.message_types_by_name['UnBindDeviceResp'] = _UNBINDDEVICERESP
DESCRIPTOR.message_types_by_name['SetDevicePropertyReq'] = _SETDEVICEPROPERTYREQ
DESCRIPTOR.message_types_by_name['GetDevicePropertyReq'] = _GETDEVICEPROPERTYREQ
DESCRIPTOR.message_types_by_name['DevicePropertyResp'] = _DEVICEPROPERTYRESP
DESCRIPTOR.message_types_by_name['GetDevicePropertiesReq'] = _GETDEVICEPROPERTIESREQ
DESCRIPTOR.message_types_by_name['GetDevicePropertiesResp'] = _GETDEVICEPROPERTIESRESP
DESCRIPTOR.message_types_by_name['DeviceProperty'] = _DEVICEPROPERTY
DESCRIPTOR.message_types_by_name['UpdateDeviceReq'] = _UPDATEDEVICEREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BindDeviceReq = _reflection.GeneratedProtocolMessageType('BindDeviceReq', (_message.Message,), {
  'DESCRIPTOR' : _BINDDEVICEREQ,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:BindDeviceReq)
  })
_sym_db.RegisterMessage(BindDeviceReq)

DeviceListResp = _reflection.GeneratedProtocolMessageType('DeviceListResp', (_message.Message,), {
  'DESCRIPTOR' : _DEVICELISTRESP,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:DeviceListResp)
  })
_sym_db.RegisterMessage(DeviceListResp)

DeviceReq = _reflection.GeneratedProtocolMessageType('DeviceReq', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEREQ,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:DeviceReq)
  })
_sym_db.RegisterMessage(DeviceReq)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:Device)
  })
_sym_db.RegisterMessage(Device)

UnBindDeviceReq = _reflection.GeneratedProtocolMessageType('UnBindDeviceReq', (_message.Message,), {
  'DESCRIPTOR' : _UNBINDDEVICEREQ,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:UnBindDeviceReq)
  })
_sym_db.RegisterMessage(UnBindDeviceReq)

UnBindDeviceResp = _reflection.GeneratedProtocolMessageType('UnBindDeviceResp', (_message.Message,), {
  'DESCRIPTOR' : _UNBINDDEVICERESP,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:UnBindDeviceResp)
  })
_sym_db.RegisterMessage(UnBindDeviceResp)

SetDevicePropertyReq = _reflection.GeneratedProtocolMessageType('SetDevicePropertyReq', (_message.Message,), {
  'DESCRIPTOR' : _SETDEVICEPROPERTYREQ,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:SetDevicePropertyReq)
  })
_sym_db.RegisterMessage(SetDevicePropertyReq)

GetDevicePropertyReq = _reflection.GeneratedProtocolMessageType('GetDevicePropertyReq', (_message.Message,), {
  'DESCRIPTOR' : _GETDEVICEPROPERTYREQ,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:GetDevicePropertyReq)
  })
_sym_db.RegisterMessage(GetDevicePropertyReq)

DevicePropertyResp = _reflection.GeneratedProtocolMessageType('DevicePropertyResp', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEPROPERTYRESP,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:DevicePropertyResp)
  })
_sym_db.RegisterMessage(DevicePropertyResp)

GetDevicePropertiesReq = _reflection.GeneratedProtocolMessageType('GetDevicePropertiesReq', (_message.Message,), {
  'DESCRIPTOR' : _GETDEVICEPROPERTIESREQ,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:GetDevicePropertiesReq)
  })
_sym_db.RegisterMessage(GetDevicePropertiesReq)

GetDevicePropertiesResp = _reflection.GeneratedProtocolMessageType('GetDevicePropertiesResp', (_message.Message,), {
  'DESCRIPTOR' : _GETDEVICEPROPERTIESRESP,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:GetDevicePropertiesResp)
  })
_sym_db.RegisterMessage(GetDevicePropertiesResp)

DeviceProperty = _reflection.GeneratedProtocolMessageType('DeviceProperty', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEPROPERTY,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:DeviceProperty)
  })
_sym_db.RegisterMessage(DeviceProperty)

UpdateDeviceReq = _reflection.GeneratedProtocolMessageType('UpdateDeviceReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDEVICEREQ,
  '__module__' : 'DeviceService_pb2'
  # @@protoc_insertion_point(class_scope:UpdateDeviceReq)
  })
_sym_db.RegisterMessage(UpdateDeviceReq)


DESCRIPTOR._options = None

_DEVICESERVICE = _descriptor.ServiceDescriptor(
  name='DeviceService',
  full_name='DeviceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=902,
  serialized_end=1340,
  methods=[
  _descriptor.MethodDescriptor(
    name='bindDevice',
    full_name='DeviceService.bindDevice',
    index=0,
    containing_service=None,
    input_type=_BINDDEVICEREQ,
    output_type=Base__pb2._RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getDeviceList',
    full_name='DeviceService.getDeviceList',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_DEVICELISTRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getDeviceInfo',
    full_name='DeviceService.getDeviceInfo',
    index=2,
    containing_service=None,
    input_type=_DEVICEREQ,
    output_type=_DEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='unBindDevice',
    full_name='DeviceService.unBindDevice',
    index=3,
    containing_service=None,
    input_type=_UNBINDDEVICEREQ,
    output_type=_UNBINDDEVICERESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='setDeviceProperty',
    full_name='DeviceService.setDeviceProperty',
    index=4,
    containing_service=None,
    input_type=_SETDEVICEPROPERTYREQ,
    output_type=Base__pb2._RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getDeviceProperty',
    full_name='DeviceService.getDeviceProperty',
    index=5,
    containing_service=None,
    input_type=_GETDEVICEPROPERTYREQ,
    output_type=_DEVICEPROPERTYRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getDeviceProperties',
    full_name='DeviceService.getDeviceProperties',
    index=6,
    containing_service=None,
    input_type=_GETDEVICEPROPERTIESREQ,
    output_type=_GETDEVICEPROPERTIESRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateDevice',
    full_name='DeviceService.updateDevice',
    index=7,
    containing_service=None,
    input_type=_UPDATEDEVICEREQ,
    output_type=_DEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVICESERVICE)

DESCRIPTOR.services_by_name['DeviceService'] = _DEVICESERVICE

# @@protoc_insertion_point(module_scope)
