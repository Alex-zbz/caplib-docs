# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dqfianalytics.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import dqdatetime_pb2 as dqdatetime__pb2
from . import dqnumerics_pb2 as dqnumerics__pb2
from . import dqanalytics_pb2 as dqanalytics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dqfianalytics.proto',
  package='dqproto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x64qfianalytics.proto\x12\x07\x64qproto\x1a\x10\x64qdatetime.proto\x1a\x10\x64qnumerics.proto\x1a\x11\x64qanalytics.proto\"\xbc\x01\n\x1b\x42ondYieldCurveBuildSettings\x12\x12\n\ncurve_name\x18\x01 \x01(\t\x12-\n\ncurve_type\x18\x02 \x01(\x0e\x32\x19.dqproto.IrYieldCurveType\x12,\n\rinterp_method\x18\x03 \x01(\x0e\x32\x15.dqproto.InterpMethod\x12,\n\rextrap_method\x18\x04 \x01(\x0e\x32\x15.dqproto.ExtrapMethod\"\xe2\x01\n\x0c\x42ondParCurve\x12%\n\x0ereference_date\x18\x01 \x01(\x0b\x32\r.dqproto.Date\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12-\n\x07pillars\x18\x03 \x03(\x0b\x32\x1c.dqproto.BondParCurve.Pillar\x12*\n\nquote_type\x18\x04 \x01(\x0e\x32\x16.dqproto.BondQuoteType\x12\x0c\n\x04name\x18\x05 \x01(\t\x1a\x30\n\x06Pillar\x12\x17\n\x0finstrument_name\x18\x01 \x01(\t\x12\r\n\x05quote\x18\x02 \x01(\x01\"\xd0\x02\n$BondYieldCurveBuildSettingsContainer\x12\x19\n\x11target_curve_name\x18\x01 \x01(\t\x12M\n\x1f\x62ond_yield_curve_build_settings\x18\x02 \x01(\x0b\x32$.dqproto.BondYieldCurveBuildSettings\x12(\n\tpar_curve\x18\x03 \x01(\x0b\x32\x15.dqproto.BondParCurve\x12\x39\n\x14\x64\x61y_count_convention\x18\x04 \x01(\x0e\x32\x1b.dqproto.DayCountConvention\x12\x32\n\x10\x63ompounding_type\x18\x05 \x01(\x0e\x32\x18.dqproto.CompoundingType\x12%\n\tfrequency\x18\x06 \x01(\x0e\x32\x12.dqproto.Frequency\"\xac\x02\n\x0c\x46iMktDataSet\x12!\n\nas_of_date\x18\x01 \x01(\x0b\x32\r.dqproto.Date\x12-\n\x0e\x64iscount_curve\x18\x02 \x01(\x0b\x32\x15.dqproto.IrYieldCurve\x12*\n\x0cspread_curve\x18\x03 \x01(\x0b\x32\x14.dqproto.CreditCurve\x12,\n\rforward_curve\x18\x04 \x01(\x0b\x32\x15.dqproto.IrYieldCurve\x12\x38\n\x19underlying_discount_curve\x18\x05 \x01(\x0b\x32\x15.dqproto.IrYieldCurve\x12\x36\n\x17underlying_income_curve\x18\x06 \x01(\x0b\x32\x15.dqproto.IrYieldCurve\"\xba\x01\n\x0e\x46iRiskSettings\x12\x37\n\x11ir_curve_settings\x18\x01 \x01(\x0b\x32\x1c.dqproto.IrCurveRiskSettings\x12;\n\x11\x63s_curve_settings\x18\x03 \x01(\x0b\x32 .dqproto.CreditCurveRiskSettings\x12\x32\n\x0etheta_settings\x18\x02 \x01(\x0b\x32\x1a.dqproto.ThetaRiskSettings*V\n\rBondQuoteType\x12\x15\n\x11YIELD_TO_MATURITY\x10\x00\x12\x0f\n\x0b\x43LEAN_PRICE\x10\x01\x12\x0f\n\x0b\x44IRTY_PRICE\x10\x02\x12\x0c\n\x08PAR_RATE\x10\x03*\x8a\x01\n\x11\x42ondPricingMethod\x12\x1b\n\x17STD_BOND_PRICING_METHOD\x10\x00\x12\x1b\n\x17\x43SI_BOND_PRICING_METHOD\x10\x01\x12\x1c\n\x18\x43\x43\x44\x43_BOND_PRICING_METHOD\x10\x02\x12\x1d\n\x19\x43\x46\x45TS_BOND_PRICING_METHOD\x10\x03*\x9c\x02\n\x1a\x42ondSpecificPricingRequest\x12\x1d\n\x19YIELD_TO_MATUIRTY_REQUEST\x10\x00\x12\x17\n\x13\x44IRTY_PRICE_REQUEST\x10\x01\x12\x17\n\x13\x43LEAN_PRICE_REQUEST\x10\x02\x12\x1c\n\x18\x41\x43\x43RUED_INTEREST_REQUEST\x10\x03\x12\x1b\n\x17SIMPLE_DURATION_REQUEST\x10\x04\x12\x1d\n\x19MODIFIED_DURATION_REQUEST\x10\x05\x12\x1d\n\x19MACAULAY_DURATION_REQUEST\x10\x06\x12\x15\n\x11\x43ONVEXITY_REQUEST\x10\x07\x12\x1d\n\x19\x42\x41SIS_POINT_VALUE_REQUEST\x10\x08\x62\x06proto3'
  ,
  dependencies=[dqdatetime__pb2.DESCRIPTOR,dqnumerics__pb2.DESCRIPTOR,dqanalytics__pb2.DESCRIPTOR,])

_BONDQUOTETYPE = _descriptor.EnumDescriptor(
  name='BondQuoteType',
  full_name='dqproto.BondQuoteType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='YIELD_TO_MATURITY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLEAN_PRICE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRTY_PRICE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAR_RATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1338,
  serialized_end=1424,
)
_sym_db.RegisterEnumDescriptor(_BONDQUOTETYPE)

BondQuoteType = enum_type_wrapper.EnumTypeWrapper(_BONDQUOTETYPE)
_BONDPRICINGMETHOD = _descriptor.EnumDescriptor(
  name='BondPricingMethod',
  full_name='dqproto.BondPricingMethod',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STD_BOND_PRICING_METHOD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CSI_BOND_PRICING_METHOD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CCDC_BOND_PRICING_METHOD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CFETS_BOND_PRICING_METHOD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1427,
  serialized_end=1565,
)
_sym_db.RegisterEnumDescriptor(_BONDPRICINGMETHOD)

BondPricingMethod = enum_type_wrapper.EnumTypeWrapper(_BONDPRICINGMETHOD)
_BONDSPECIFICPRICINGREQUEST = _descriptor.EnumDescriptor(
  name='BondSpecificPricingRequest',
  full_name='dqproto.BondSpecificPricingRequest',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='YIELD_TO_MATUIRTY_REQUEST', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRTY_PRICE_REQUEST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLEAN_PRICE_REQUEST', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCRUED_INTEREST_REQUEST', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_DURATION_REQUEST', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODIFIED_DURATION_REQUEST', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MACAULAY_DURATION_REQUEST', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVEXITY_REQUEST', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BASIS_POINT_VALUE_REQUEST', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1568,
  serialized_end=1852,
)
_sym_db.RegisterEnumDescriptor(_BONDSPECIFICPRICINGREQUEST)

BondSpecificPricingRequest = enum_type_wrapper.EnumTypeWrapper(_BONDSPECIFICPRICINGREQUEST)
YIELD_TO_MATURITY = 0
CLEAN_PRICE = 1
DIRTY_PRICE = 2
PAR_RATE = 3
STD_BOND_PRICING_METHOD = 0
CSI_BOND_PRICING_METHOD = 1
CCDC_BOND_PRICING_METHOD = 2
CFETS_BOND_PRICING_METHOD = 3
YIELD_TO_MATUIRTY_REQUEST = 0
DIRTY_PRICE_REQUEST = 1
CLEAN_PRICE_REQUEST = 2
ACCRUED_INTEREST_REQUEST = 3
SIMPLE_DURATION_REQUEST = 4
MODIFIED_DURATION_REQUEST = 5
MACAULAY_DURATION_REQUEST = 6
CONVEXITY_REQUEST = 7
BASIS_POINT_VALUE_REQUEST = 8



_BONDYIELDCURVEBUILDSETTINGS = _descriptor.Descriptor(
  name='BondYieldCurveBuildSettings',
  full_name='dqproto.BondYieldCurveBuildSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='curve_name', full_name='dqproto.BondYieldCurveBuildSettings.curve_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curve_type', full_name='dqproto.BondYieldCurveBuildSettings.curve_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interp_method', full_name='dqproto.BondYieldCurveBuildSettings.interp_method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extrap_method', full_name='dqproto.BondYieldCurveBuildSettings.extrap_method', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=88,
  serialized_end=276,
)


_BONDPARCURVE_PILLAR = _descriptor.Descriptor(
  name='Pillar',
  full_name='dqproto.BondParCurve.Pillar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument_name', full_name='dqproto.BondParCurve.Pillar.instrument_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote', full_name='dqproto.BondParCurve.Pillar.quote', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=457,
  serialized_end=505,
)

_BONDPARCURVE = _descriptor.Descriptor(
  name='BondParCurve',
  full_name='dqproto.BondParCurve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_date', full_name='dqproto.BondParCurve.reference_date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='dqproto.BondParCurve.currency', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pillars', full_name='dqproto.BondParCurve.pillars', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote_type', full_name='dqproto.BondParCurve.quote_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='dqproto.BondParCurve.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BONDPARCURVE_PILLAR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=505,
)


_BONDYIELDCURVEBUILDSETTINGSCONTAINER = _descriptor.Descriptor(
  name='BondYieldCurveBuildSettingsContainer',
  full_name='dqproto.BondYieldCurveBuildSettingsContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_curve_name', full_name='dqproto.BondYieldCurveBuildSettingsContainer.target_curve_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bond_yield_curve_build_settings', full_name='dqproto.BondYieldCurveBuildSettingsContainer.bond_yield_curve_build_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='par_curve', full_name='dqproto.BondYieldCurveBuildSettingsContainer.par_curve', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day_count_convention', full_name='dqproto.BondYieldCurveBuildSettingsContainer.day_count_convention', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compounding_type', full_name='dqproto.BondYieldCurveBuildSettingsContainer.compounding_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='dqproto.BondYieldCurveBuildSettingsContainer.frequency', index=5,
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
  serialized_start=508,
  serialized_end=844,
)


_FIMKTDATASET = _descriptor.Descriptor(
  name='FiMktDataSet',
  full_name='dqproto.FiMktDataSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='as_of_date', full_name='dqproto.FiMktDataSet.as_of_date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discount_curve', full_name='dqproto.FiMktDataSet.discount_curve', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spread_curve', full_name='dqproto.FiMktDataSet.spread_curve', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='forward_curve', full_name='dqproto.FiMktDataSet.forward_curve', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='underlying_discount_curve', full_name='dqproto.FiMktDataSet.underlying_discount_curve', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='underlying_income_curve', full_name='dqproto.FiMktDataSet.underlying_income_curve', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=847,
  serialized_end=1147,
)


_FIRISKSETTINGS = _descriptor.Descriptor(
  name='FiRiskSettings',
  full_name='dqproto.FiRiskSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ir_curve_settings', full_name='dqproto.FiRiskSettings.ir_curve_settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cs_curve_settings', full_name='dqproto.FiRiskSettings.cs_curve_settings', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='theta_settings', full_name='dqproto.FiRiskSettings.theta_settings', index=2,
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
  serialized_start=1150,
  serialized_end=1336,
)

_BONDYIELDCURVEBUILDSETTINGS.fields_by_name['curve_type'].enum_type = dqanalytics__pb2._IRYIELDCURVETYPE
_BONDYIELDCURVEBUILDSETTINGS.fields_by_name['interp_method'].enum_type = dqnumerics__pb2._INTERPMETHOD
_BONDYIELDCURVEBUILDSETTINGS.fields_by_name['extrap_method'].enum_type = dqnumerics__pb2._EXTRAPMETHOD
_BONDPARCURVE_PILLAR.containing_type = _BONDPARCURVE
_BONDPARCURVE.fields_by_name['reference_date'].message_type = dqdatetime__pb2._DATE
_BONDPARCURVE.fields_by_name['pillars'].message_type = _BONDPARCURVE_PILLAR
_BONDPARCURVE.fields_by_name['quote_type'].enum_type = _BONDQUOTETYPE
_BONDYIELDCURVEBUILDSETTINGSCONTAINER.fields_by_name['bond_yield_curve_build_settings'].message_type = _BONDYIELDCURVEBUILDSETTINGS
_BONDYIELDCURVEBUILDSETTINGSCONTAINER.fields_by_name['par_curve'].message_type = _BONDPARCURVE
_BONDYIELDCURVEBUILDSETTINGSCONTAINER.fields_by_name['day_count_convention'].enum_type = dqdatetime__pb2._DAYCOUNTCONVENTION
_BONDYIELDCURVEBUILDSETTINGSCONTAINER.fields_by_name['compounding_type'].enum_type = dqanalytics__pb2._COMPOUNDINGTYPE
_BONDYIELDCURVEBUILDSETTINGSCONTAINER.fields_by_name['frequency'].enum_type = dqdatetime__pb2._FREQUENCY
_FIMKTDATASET.fields_by_name['as_of_date'].message_type = dqdatetime__pb2._DATE
_FIMKTDATASET.fields_by_name['discount_curve'].message_type = dqanalytics__pb2._IRYIELDCURVE
_FIMKTDATASET.fields_by_name['spread_curve'].message_type = dqanalytics__pb2._CREDITCURVE
_FIMKTDATASET.fields_by_name['forward_curve'].message_type = dqanalytics__pb2._IRYIELDCURVE
_FIMKTDATASET.fields_by_name['underlying_discount_curve'].message_type = dqanalytics__pb2._IRYIELDCURVE
_FIMKTDATASET.fields_by_name['underlying_income_curve'].message_type = dqanalytics__pb2._IRYIELDCURVE
_FIRISKSETTINGS.fields_by_name['ir_curve_settings'].message_type = dqanalytics__pb2._IRCURVERISKSETTINGS
_FIRISKSETTINGS.fields_by_name['cs_curve_settings'].message_type = dqanalytics__pb2._CREDITCURVERISKSETTINGS
_FIRISKSETTINGS.fields_by_name['theta_settings'].message_type = dqanalytics__pb2._THETARISKSETTINGS
DESCRIPTOR.message_types_by_name['BondYieldCurveBuildSettings'] = _BONDYIELDCURVEBUILDSETTINGS
DESCRIPTOR.message_types_by_name['BondParCurve'] = _BONDPARCURVE
DESCRIPTOR.message_types_by_name['BondYieldCurveBuildSettingsContainer'] = _BONDYIELDCURVEBUILDSETTINGSCONTAINER
DESCRIPTOR.message_types_by_name['FiMktDataSet'] = _FIMKTDATASET
DESCRIPTOR.message_types_by_name['FiRiskSettings'] = _FIRISKSETTINGS
DESCRIPTOR.enum_types_by_name['BondQuoteType'] = _BONDQUOTETYPE
DESCRIPTOR.enum_types_by_name['BondPricingMethod'] = _BONDPRICINGMETHOD
DESCRIPTOR.enum_types_by_name['BondSpecificPricingRequest'] = _BONDSPECIFICPRICINGREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BondYieldCurveBuildSettings = _reflection.GeneratedProtocolMessageType('BondYieldCurveBuildSettings', (_message.Message,), {
  'DESCRIPTOR' : _BONDYIELDCURVEBUILDSETTINGS,
  '__module__' : 'dqfianalytics_pb2'
  # @@protoc_insertion_point(class_scope:dqproto.BondYieldCurveBuildSettings)
  })
_sym_db.RegisterMessage(BondYieldCurveBuildSettings)

BondParCurve = _reflection.GeneratedProtocolMessageType('BondParCurve', (_message.Message,), {

  'Pillar' : _reflection.GeneratedProtocolMessageType('Pillar', (_message.Message,), {
    'DESCRIPTOR' : _BONDPARCURVE_PILLAR,
    '__module__' : 'dqfianalytics_pb2'
    # @@protoc_insertion_point(class_scope:dqproto.BondParCurve.Pillar)
    })
  ,
  'DESCRIPTOR' : _BONDPARCURVE,
  '__module__' : 'dqfianalytics_pb2'
  # @@protoc_insertion_point(class_scope:dqproto.BondParCurve)
  })
_sym_db.RegisterMessage(BondParCurve)
_sym_db.RegisterMessage(BondParCurve.Pillar)

BondYieldCurveBuildSettingsContainer = _reflection.GeneratedProtocolMessageType('BondYieldCurveBuildSettingsContainer', (_message.Message,), {
  'DESCRIPTOR' : _BONDYIELDCURVEBUILDSETTINGSCONTAINER,
  '__module__' : 'dqfianalytics_pb2'
  # @@protoc_insertion_point(class_scope:dqproto.BondYieldCurveBuildSettingsContainer)
  })
_sym_db.RegisterMessage(BondYieldCurveBuildSettingsContainer)

FiMktDataSet = _reflection.GeneratedProtocolMessageType('FiMktDataSet', (_message.Message,), {
  'DESCRIPTOR' : _FIMKTDATASET,
  '__module__' : 'dqfianalytics_pb2'
  # @@protoc_insertion_point(class_scope:dqproto.FiMktDataSet)
  })
_sym_db.RegisterMessage(FiMktDataSet)

FiRiskSettings = _reflection.GeneratedProtocolMessageType('FiRiskSettings', (_message.Message,), {
  'DESCRIPTOR' : _FIRISKSETTINGS,
  '__module__' : 'dqfianalytics_pb2'
  # @@protoc_insertion_point(class_scope:dqproto.FiRiskSettings)
  })
_sym_db.RegisterMessage(FiRiskSettings)


# @@protoc_insertion_point(module_scope)
