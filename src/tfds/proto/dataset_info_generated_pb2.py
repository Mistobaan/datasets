# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataset_info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow_metadata.proto.v0 import (
    statistics_pb2 as tensorflow__metadata_dot_proto_dot_v0_dot_statistics__pb2,
)
from tensorflow_metadata.proto.v0 import (
    schema_pb2 as tensorflow__metadata_dot_proto_dot_v0_dot_schema__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="dataset_info.proto",
    package="tfds",
    syntax="proto3",
    serialized_options=b"\370\001\001",
    serialized_pb=b'\n\x12\x64\x61taset_info.proto\x12\x04tfds\x1a-tensorflow_metadata/proto/v0/statistics.proto\x1a)tensorflow_metadata/proto/v0/schema.proto"\x1f\n\x0f\x44\x61tasetLocation\x12\x0c\n\x04urls\x18\x01 \x03(\t"\x9d\x01\n\tSplitInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nnum_shards\x18\x02 \x01(\x03\x12\x15\n\rshard_lengths\x18\x04 \x03(\x03\x12\x11\n\tnum_bytes\x18\x05 \x01(\x03\x12\x44\n\nstatistics\x18\x03 \x01(\x0b\x32\x30.tensorflow.metadata.v0.DatasetFeatureStatistics"/\n\x0eSupervisedKeys\x12\r\n\x05input\x18\x01 \x01(\t\x12\x0e\n\x06output\x18\x02 \x01(\t"%\n\x12RedistributionInfo\x12\x0f\n\x07license\x18\x01 \x01(\t"\xe9\x03\n\x0b\x44\x61tasetInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\t \x01(\t\x12\x10\n\x08\x63itation\x18\x03 \x01(\t\x12\x19\n\rsize_in_bytes\x18\x04 \x01(\x03\x42\x02\x18\x01\x12\x15\n\rdownload_size\x18\x0c \x01(\x03\x12\'\n\x08location\x18\x05 \x01(\x0b\x32\x15.tfds.DatasetLocation\x12H\n\x12\x64ownload_checksums\x18\n \x03(\x0b\x32(.tfds.DatasetInfo.DownloadChecksumsEntryB\x02\x18\x01\x12.\n\x06schema\x18\x06 \x01(\x0b\x32\x1e.tensorflow.metadata.v0.Schema\x12\x1f\n\x06splits\x18\x07 \x03(\x0b\x32\x0f.tfds.SplitInfo\x12-\n\x0fsupervised_keys\x18\x08 \x01(\x0b\x32\x14.tfds.SupervisedKeys\x12\x35\n\x13redistribution_info\x18\x0b \x01(\x0b\x32\x18.tfds.RedistributionInfo\x1a\x38\n\x16\x44ownloadChecksumsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x03\xf8\x01\x01\x62\x06proto3',
    dependencies=[
        tensorflow__metadata_dot_proto_dot_v0_dot_statistics__pb2.DESCRIPTOR,
        tensorflow__metadata_dot_proto_dot_v0_dot_schema__pb2.DESCRIPTOR,
    ],
)


_DATASETLOCATION = _descriptor.Descriptor(
    name="DatasetLocation",
    full_name="tfds.DatasetLocation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="urls",
            full_name="tfds.DatasetLocation.urls",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=118,
    serialized_end=149,
)


_SPLITINFO = _descriptor.Descriptor(
    name="SplitInfo",
    full_name="tfds.SplitInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="tfds.SplitInfo.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="num_shards",
            full_name="tfds.SplitInfo.num_shards",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="shard_lengths",
            full_name="tfds.SplitInfo.shard_lengths",
            index=2,
            number=4,
            type=3,
            cpp_type=2,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="num_bytes",
            full_name="tfds.SplitInfo.num_bytes",
            index=3,
            number=5,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="statistics",
            full_name="tfds.SplitInfo.statistics",
            index=4,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=152,
    serialized_end=309,
)


_SUPERVISEDKEYS = _descriptor.Descriptor(
    name="SupervisedKeys",
    full_name="tfds.SupervisedKeys",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="tfds.SupervisedKeys.input",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="output",
            full_name="tfds.SupervisedKeys.output",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=311,
    serialized_end=358,
)


_REDISTRIBUTIONINFO = _descriptor.Descriptor(
    name="RedistributionInfo",
    full_name="tfds.RedistributionInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="license",
            full_name="tfds.RedistributionInfo.license",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=360,
    serialized_end=397,
)


_DATASETINFO_DOWNLOADCHECKSUMSENTRY = _descriptor.Descriptor(
    name="DownloadChecksumsEntry",
    full_name="tfds.DatasetInfo.DownloadChecksumsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="tfds.DatasetInfo.DownloadChecksumsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tfds.DatasetInfo.DownloadChecksumsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=833,
    serialized_end=889,
)

_DATASETINFO = _descriptor.Descriptor(
    name="DatasetInfo",
    full_name="tfds.DatasetInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="tfds.DatasetInfo.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="tfds.DatasetInfo.description",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="tfds.DatasetInfo.version",
            index=2,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="citation",
            full_name="tfds.DatasetInfo.citation",
            index=3,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="size_in_bytes",
            full_name="tfds.DatasetInfo.size_in_bytes",
            index=4,
            number=4,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="download_size",
            full_name="tfds.DatasetInfo.download_size",
            index=5,
            number=12,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="tfds.DatasetInfo.location",
            index=6,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="download_checksums",
            full_name="tfds.DatasetInfo.download_checksums",
            index=7,
            number=10,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="schema",
            full_name="tfds.DatasetInfo.schema",
            index=8,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="splits",
            full_name="tfds.DatasetInfo.splits",
            index=9,
            number=7,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="supervised_keys",
            full_name="tfds.DatasetInfo.supervised_keys",
            index=10,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="redistribution_info",
            full_name="tfds.DatasetInfo.redistribution_info",
            index=11,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_DATASETINFO_DOWNLOADCHECKSUMSENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=400,
    serialized_end=889,
)

_SPLITINFO.fields_by_name[
    "statistics"
].message_type = (
    tensorflow__metadata_dot_proto_dot_v0_dot_statistics__pb2._DATASETFEATURESTATISTICS
)
_DATASETINFO_DOWNLOADCHECKSUMSENTRY.containing_type = _DATASETINFO
_DATASETINFO.fields_by_name["location"].message_type = _DATASETLOCATION
_DATASETINFO.fields_by_name[
    "download_checksums"
].message_type = _DATASETINFO_DOWNLOADCHECKSUMSENTRY
_DATASETINFO.fields_by_name[
    "schema"
].message_type = tensorflow__metadata_dot_proto_dot_v0_dot_schema__pb2._SCHEMA
_DATASETINFO.fields_by_name["splits"].message_type = _SPLITINFO
_DATASETINFO.fields_by_name["supervised_keys"].message_type = _SUPERVISEDKEYS
_DATASETINFO.fields_by_name["redistribution_info"].message_type = _REDISTRIBUTIONINFO
DESCRIPTOR.message_types_by_name["DatasetLocation"] = _DATASETLOCATION
DESCRIPTOR.message_types_by_name["SplitInfo"] = _SPLITINFO
DESCRIPTOR.message_types_by_name["SupervisedKeys"] = _SUPERVISEDKEYS
DESCRIPTOR.message_types_by_name["RedistributionInfo"] = _REDISTRIBUTIONINFO
DESCRIPTOR.message_types_by_name["DatasetInfo"] = _DATASETINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DatasetLocation = _reflection.GeneratedProtocolMessageType(
    "DatasetLocation",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATASETLOCATION,
        "__module__": "dataset_info_pb2"
        # @@protoc_insertion_point(class_scope:tfds.DatasetLocation)
    },
)
_sym_db.RegisterMessage(DatasetLocation)

SplitInfo = _reflection.GeneratedProtocolMessageType(
    "SplitInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPLITINFO,
        "__module__": "dataset_info_pb2"
        # @@protoc_insertion_point(class_scope:tfds.SplitInfo)
    },
)
_sym_db.RegisterMessage(SplitInfo)

SupervisedKeys = _reflection.GeneratedProtocolMessageType(
    "SupervisedKeys",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUPERVISEDKEYS,
        "__module__": "dataset_info_pb2"
        # @@protoc_insertion_point(class_scope:tfds.SupervisedKeys)
    },
)
_sym_db.RegisterMessage(SupervisedKeys)

RedistributionInfo = _reflection.GeneratedProtocolMessageType(
    "RedistributionInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _REDISTRIBUTIONINFO,
        "__module__": "dataset_info_pb2"
        # @@protoc_insertion_point(class_scope:tfds.RedistributionInfo)
    },
)
_sym_db.RegisterMessage(RedistributionInfo)

DatasetInfo = _reflection.GeneratedProtocolMessageType(
    "DatasetInfo",
    (_message.Message,),
    {
        "DownloadChecksumsEntry": _reflection.GeneratedProtocolMessageType(
            "DownloadChecksumsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _DATASETINFO_DOWNLOADCHECKSUMSENTRY,
                "__module__": "dataset_info_pb2"
                # @@protoc_insertion_point(class_scope:tfds.DatasetInfo.DownloadChecksumsEntry)
            },
        ),
        "DESCRIPTOR": _DATASETINFO,
        "__module__": "dataset_info_pb2"
        # @@protoc_insertion_point(class_scope:tfds.DatasetInfo)
    },
)
_sym_db.RegisterMessage(DatasetInfo)
_sym_db.RegisterMessage(DatasetInfo.DownloadChecksumsEntry)


DESCRIPTOR._options = None
_DATASETINFO_DOWNLOADCHECKSUMSENTRY._options = None
_DATASETINFO.fields_by_name["size_in_bytes"]._options = None
_DATASETINFO.fields_by_name["download_checksums"]._options = None
# @@protoc_insertion_point(module_scope)