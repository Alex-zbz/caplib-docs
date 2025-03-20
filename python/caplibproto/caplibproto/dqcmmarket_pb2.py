# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dqcmmarket.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import dqdatetime_pb2 as dqdatetime__pb2
from . import dqmarket_pb2 as dqmarket__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dqcmmarket.proto',
  package='dqproto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x64qcmmarket.proto\x12\x07\x64qproto\x1a\x10\x64qdatetime.proto\x1a\x0e\x64qmarket.proto\"\xb6\x01\n\x0ePmCashTemplate\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bstart_delay\x18\x03 \x01(\x05\x12?\n\x17\x64\x65livery_day_convention\x18\x04 \x01(\x0e\x32\x1e.dqproto.BusinessDayConvention\x12\x10\n\x08\x63\x61lendar\x18\x05 \x03(\t\x12.\n\tday_count\x18\x06 \x01(\x0e\x32\x1b.dqproto.DayCountConvention\"G\n\x12PmCashTemplateList\x12\x31\n\x10pm_cash_template\x18\x01 \x03(\x0b\x32\x17.dqproto.PmCashTemplateb\x06proto3'
  ,
  dependencies=[dqdatetime__pb2.DESCRIPTOR,dqmarket__pb2.DESCRIPTOR,])




_PMCASHTEMPLATE = _descriptor.Descriptor(
  name='PmCashTemplate',
  full_name='dqproto.PmCashTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dqproto.PmCashTemplate.name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_delay', full_name='dqproto.PmCashTemplate.start_delay', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_day_convention', full_name='dqproto.PmCashTemplate.delivery_day_convention', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='calendar', full_name='dqproto.PmCashTemplate.calendar', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day_count', full_name='dqproto.PmCashTemplate.day_count', index=4,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=64,
  serialized_end=246,
)


_PMCASHTEMPLATELIST = _descriptor.Descriptor(
  name='PmCashTemplateList',
  full_name='dqproto.PmCashTemplateList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pm_cash_template', full_name='dqproto.PmCashTemplateList.pm_cash_template', index=0,
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
  serialized_start=248,
  serialized_end=319,
)

_PMCASHTEMPLATE.fields_by_name['delivery_day_convention'].enum_type = dqdatetime__pb2._BUSINESSDAYCONVENTION
_PMCASHTEMPLATE.fields_by_name['day_count'].enum_type = dqdatetime__pb2._DAYCOUNTCONVENTION
_PMCASHTEMPLATELIST.fields_by_name['pm_cash_template'].message_type = _PMCASHTEMPLATE
DESCRIPTOR.message_types_by_name['PmCashTemplate'] = _PMCASHTEMPLATE
DESCRIPTOR.message_types_by_name['PmCashTemplateList'] = _PMCASHTEMPLATELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PmCashTemplate = _reflection.GeneratedProtocolMessageType('PmCashTemplate', (_message.Message,), {
  'DESCRIPTOR' : _PMCASHTEMPLATE,
  '__module__' : 'dqcmmarket_pb2'
  # @@protoc_insertion_point(class_scope:dqproto.PmCashTemplate)
  })
_sym_db.RegisterMessage(PmCashTemplate)

PmCashTemplateList = _reflection.GeneratedProtocolMessageType('PmCashTemplateList', (_message.Message,), {
  'DESCRIPTOR' : _PMCASHTEMPLATELIST,
  '__module__' : 'dqcmmarket_pb2'
  # @@protoc_insertion_point(class_scope:dqproto.PmCashTemplateList)
  })
_sym_db.RegisterMessage(PmCashTemplateList)


# @@protoc_insertion_point(module_scope)
