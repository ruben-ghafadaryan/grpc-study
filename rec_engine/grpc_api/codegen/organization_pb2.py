# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: organization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12organization.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xa8\x01\n\x14OrganizationResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x04 \x01(\t\x12\x10\n\x08industry\x18\x05 \x01(\t\x12\x0f\n\x07website\x18\x06 \x01(\t\x12\x14\n\x0c\x66ounded_year\x18\x07 \x01(\x05\x12\x17\n\x0f\x65mployees_count\x18\x08 \x01(\x05\"H\n\x18OrganizationResponseList\x12,\n\rorganizations\x18\x01 \x03(\x0b\x32\x15.OrganizationResponse\"(\n\x1aGetOrganizationByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\'\n\x19\x44\x65leteOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\xa1\x01\n\x19\x43reateOrganizationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x10\n\x08industry\x18\x04 \x01(\t\x12\x0f\n\x07website\x18\x05 \x01(\t\x12\x14\n\x0c\x66ounded_year\x18\x06 \x01(\x05\x12\x17\n\x0f\x65mployees_count\x18\x07 \x01(\x05\"\xb3\x02\n\x19UpdateOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07\x63ountry\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08industry\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07website\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x19\n\x0c\x66ounded_year\x18\x07 \x01(\x05H\x05\x88\x01\x01\x12\x1c\n\x0f\x65mployees_count\x18\x08 \x01(\x05H\x06\x88\x01\x01\x42\x07\n\x05_nameB\x0e\n\x0c_descriptionB\n\n\x08_countryB\x0b\n\t_industryB\n\n\x08_websiteB\x0f\n\r_founded_yearB\x12\n\x10_employees_count\"\xc7\x01\n\x17\x46indOrganizationRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07\x63ountry\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08industry\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07website\x18\x05 \x01(\tH\x04\x88\x01\x01\x42\x07\n\x05_nameB\x0e\n\x0c_descriptionB\n\n\x08_countryB\x0b\n\t_industryB\n\n\x08_website2\xf4\x04\n\x13OrganizationService\x12K\n\x16GetOrganizationsAsList\x12\x16.google.protobuf.Empty\x1a\x19.OrganizationResponseList\x12K\n\x18GetOrganizationsAsStream\x12\x16.google.protobuf.Empty\x1a\x15.OrganizationResponse0\x01\x12I\n\x13GetOrganizationById\x12\x1b.GetOrganizationByIdRequest\x1a\x15.OrganizationResponse\x12G\n\x12\x43reateOrganization\x12\x1a.CreateOrganizationRequest\x1a\x15.OrganizationResponse\x12G\n\x12UpdateOrganization\x12\x1a.UpdateOrganizationRequest\x1a\x15.OrganizationResponse\x12H\n\x12\x44\x65leteOrganization\x12\x1a.DeleteOrganizationRequest\x1a\x16.google.protobuf.Empty\x12M\n\x18\x46indOrganizationAsStream\x12\x18.FindOrganizationRequest\x1a\x15.OrganizationResponse0\x01\x12M\n\x16\x46indOrganizationAsList\x12\x18.FindOrganizationRequest\x1a\x19.OrganizationResponseListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'organization_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ORGANIZATIONRESPONSE']._serialized_start=52
  _globals['_ORGANIZATIONRESPONSE']._serialized_end=220
  _globals['_ORGANIZATIONRESPONSELIST']._serialized_start=222
  _globals['_ORGANIZATIONRESPONSELIST']._serialized_end=294
  _globals['_GETORGANIZATIONBYIDREQUEST']._serialized_start=296
  _globals['_GETORGANIZATIONBYIDREQUEST']._serialized_end=336
  _globals['_DELETEORGANIZATIONREQUEST']._serialized_start=338
  _globals['_DELETEORGANIZATIONREQUEST']._serialized_end=377
  _globals['_CREATEORGANIZATIONREQUEST']._serialized_start=380
  _globals['_CREATEORGANIZATIONREQUEST']._serialized_end=541
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_start=544
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_end=851
  _globals['_FINDORGANIZATIONREQUEST']._serialized_start=854
  _globals['_FINDORGANIZATIONREQUEST']._serialized_end=1053
  _globals['_ORGANIZATIONSERVICE']._serialized_start=1056
  _globals['_ORGANIZATIONSERVICE']._serialized_end=1684
# @@protoc_insertion_point(module_scope)
