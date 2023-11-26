from typing import List

import grpc
from pydantic import parse_obj_as

from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from database.sqlite import get_session
from rest_api.schemas.organizations import (
    OrganizationCreateSchema,
    OrganizationUpdateSchema,
    OrganizationFilterSchema,
    OrganizationResponseSchema
)
from rest_api.schemas.general import GeneralErrorResponseSchema
from controllers.organizations import OrganizationController
from grpc_api.codegen.organization_pb2_grpc import OrganizationServiceStub
from grpc_client.organization import GRPCOrganziationClient

router = APIRouter(prefix="/organizations_g", tags=["organizations_g"])


@router.get('/', responses={
    200: {"model": List[OrganizationResponseSchema]},
    500: {"model": GeneralErrorResponseSchema}
})
async def get_all_organizations(response: Response, session: Session = Depends(get_session)):
    try:
        stub = GRPCOrganziationClient()
        res = stub.get_organizations_as_list()
        response.status_code = status.HTTP_200_OK
        return parse_obj_as(List[OrganizationResponseSchema], res)
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))


@router.get('/{org_id}/', responses={
    200: {"model": OrganizationResponseSchema},
    404: {"model": GeneralErrorResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
async def get_organization_by_id(org_id: int,
                                 response: Response, session: Session = Depends(get_session)):
    try:
        stub = GRPCOrganziationClient()
        res = stub.get_organization_by_id(org_id)
        response.status_code = status.HTTP_200_OK
        return parse_obj_as(OrganizationResponseSchema, res)
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))


@router.patch('/{org_id}/', responses={
    200: {"model": OrganizationResponseSchema},
    404: {"model": GeneralErrorResponseSchema},
    422: {"model": GeneralErrorResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
async def update_organization(org_id: int, org_data: OrganizationUpdateSchema,
                              response: Response, session: Session = Depends(get_session)):
    try:
        stub = GRPCOrganziationClient()
        response = stub.get_organization_by_id(org_id)
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))


@router.delete('/{org_id}/', responses={
    500: {"model": GeneralErrorResponseSchema}
})
async def delete_organization(org_id: int, response: Response, session: Session = Depends(get_session)):
    try:
        stub = GRPCOrganziationClient()
        stub.delete_organization(org_id)
        response.status_code = status.HTTP_204_NO_CONTENT
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))


@router.post('/', responses={
    201: {"model": OrganizationResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
async def create_organization(org_data: OrganizationCreateSchema,
                              response: Response, session: Session = Depends(get_session)):
    try:
        stub = GRPCOrganziationClient()
        res = stub.create_organization(org_data)
        response.status_code = status.HTTP_201_CREATED
        return parse_obj_as(OrganizationResponseSchema, res)
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))


@router.post('/find/', responses={
    200: {"model": List[OrganizationResponseSchema]},
    422: {"model": GeneralErrorResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
async def find_organizations(org_data: OrganizationFilterSchema,
                             response: Response, session: Session = Depends(get_session)):
    try:
        pass
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))
