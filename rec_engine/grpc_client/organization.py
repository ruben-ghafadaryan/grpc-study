import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from grpc_api.codegen.organization_pb2_grpc import OrganizationServiceStub
import grpc_api.codegen.organization_pb2 as organization__pb2


class GRPCOrganziationClient:
    def __init__(self, host="localhost", port=50051):
        self._channel = grpc.insecure_channel(f"{host}:{port}")
        self._stub = OrganizationServiceStub(self._channel)

    def get_organizations_as_list(self):
        response = self._stub.GetOrganizationsAsList(google_dot_protobuf_dot_empty__pb2.Empty())
        ret = [self._convert_msg_to_dict(org) for org in response.organizations]
        return ret

    def get_organization_by_id(self, org_id):
        response = self._stub.GetOrganizationById(organization__pb2.GetOrganizationByIdRequest(id=org_id))
        return self._convert_msg_to_dict(response)

    def create_organization(self, org_data):
        response = self._stub.CreateOrganization(organization__pb2.CreateOrganizationRequest(**org_data))
        return self._convert_msg_to_dict(response)

    def update_organization(self, org_id, org_data):
        response = self._stub.UpdateOrganization(organization__pb2.UpdateOrganizationRequest(id=org_id, **org_data))
        return self._convert_msg_to_dict(response)

    def delete_organization(self, org_id):
        self._stub.DeleteOrganization(organization__pb2.DeleteOrganizationRequest(id=org_id))
        return None

    def find_organizations_as_list(self, org_data):
        response = self._stub.FindOrganizationsAsList(organization__pb2.FindOrganizationsAsListRequest(**org_data))
        ret = [self._convert_msg_to_dict(org) for org in response.organizations]
        return ret

    def _convert_msg_to_dict(self, msg):
        return {k.name: v for k, v in msg.ListFields()}
