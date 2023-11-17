#!/bin/bash

# Generate python code from proto files
python -m grpc_tools.protoc -I./grpc_api/proto --python_out=./grpc_api/codegen --grpc_python_out=./grpc_api/codegen ./grpc_api/proto/*.proto

