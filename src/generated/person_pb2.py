# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import generated.date_pb2 as date__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='person',
  syntax='proto3',
  serialized_options=b'\n\021com.ev.fap.personP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cperson.proto\x12\x06person\x1a\ndate.proto\"\xbc\x02\n\x06Person\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x13\n\x0bis_verified\x18\x05 \x01(\x08\x12\x0e\n\x06height\x18\x06 \x01(\x02\x12\x15\n\rphone_numbers\x18\x07 \x03(\t\x12\x1e\n\x06gender\x18\x08 \x01(\x0e\x32\x0e.person.Gender\x12\x18\n\x03\x64ob\x18\t \x01(\x0b\x32\x0b.utils.Date\x12)\n\taddresses\x18\n \x03(\x0b\x32\x16.person.Person.Address\x1aj\n\x07\x41\x64\x64ress\x12\x16\n\x0e\x61\x64\x64ress_line_1\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x64\x64ress_line_2\x18\x02 \x01(\t\x12\x10\n\x08zip_code\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t*+\n\x06Gender\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x42\x15\n\x11\x63om.ev.fap.personP\x01\x62\x06proto3'
  ,
  dependencies=[date__pb2.DESCRIPTOR,])

_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='person.Gender',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=355,
  serialized_end=398,
)
_sym_db.RegisterEnumDescriptor(_GENDER)

Gender = enum_type_wrapper.EnumTypeWrapper(_GENDER)
UNKNOWN = 0
MALE = 1
FEMALE = 2



_PERSON_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='person.Person.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_line_1', full_name='person.Person.Address.address_line_1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_line_2', full_name='person.Person.Address.address_line_2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zip_code', full_name='person.Person.Address.zip_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='person.Person.Address.city', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='person.Person.Address.country', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=247,
  serialized_end=353,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='person.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='person.Person.first_name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='person.Person.last_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_verified', full_name='person.Person.is_verified', index=2,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='person.Person.height', index=3,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_numbers', full_name='person.Person.phone_numbers', index=4,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='person.Person.gender', index=5,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dob', full_name='person.Person.dob', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='person.Person.addresses', index=7,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_ADDRESS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=353,
)

_PERSON_ADDRESS.containing_type = _PERSON
_PERSON.fields_by_name['gender'].enum_type = _GENDER
_PERSON.fields_by_name['dob'].message_type = date__pb2._DATE
_PERSON.fields_by_name['addresses'].message_type = _PERSON_ADDRESS
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.enum_types_by_name['Gender'] = _GENDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {

  'Address' : _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_ADDRESS,
    '__module__' : 'person_pb2'
    # @@protoc_insertion_point(class_scope:person.Person.Address)
    })
  ,
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:person.Person)
  })
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.Address)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
