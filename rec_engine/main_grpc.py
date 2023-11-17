import grpc

from concurrent import futures
from grpc_api.codegen import organization_pb2_grpc
from grpc_api.codegen.organization_pb2_grpc import OrganizationServiceServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    organization_pb2_grpc.add_OrganizationServiceServicer_to_server(OrganizationServiceServicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
