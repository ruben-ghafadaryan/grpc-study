from typing import List
from pydantic import parse_obj_as

from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from database.sqlite import get_session
from rest.schemas.organizations import (
    OrganizationCreateSchema,
    OrganizationUpdateSchema,
    OrganizationFilterSchema,
    OrganizationResponseSchema
)
from rest.schemas.general import GeneralErrorResponseSchema
from controllers.organizations import OrganizationController

router = APIRouter(prefix="/organizations", tags=["organizations"])

@router.get('/', responses={
    200: {"model": List[OrganizationResponseSchema]},
    500: {"model": GeneralErrorResponseSchema}
})
def get_all_organizations(response: Response, session: Session = Depends(get_session)):
    try:
        org_ctl = OrganizationController(session)
        orgs = org_ctl.get_all_organizations()
        return parse_obj_as(List[OrganizationResponseSchema], orgs)
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))

@router.get('/{org_id}/', responses={
    200: {"model": OrganizationResponseSchema},
    404: {"model": GeneralErrorResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
def get_organization_by_id(org_id: int,
                           response: Response, session: Session = Depends(get_session)):
    try:
        org_ctl = OrganizationController(session)
        org = org_ctl.get_organization_by_id(org_id)
        if org is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Organization {org_id} not found")
        return OrganizationResponseSchema.from_orm(org)
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))


@router.patch('/{org_id}/', responses={
    200: {"model": OrganizationResponseSchema},
    404: {"model": GeneralErrorResponseSchema},
    422: {"model": GeneralErrorResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
def update_organization(org_id: int, org_data: OrganizationUpdateSchema,
                        response: Response, session: Session = Depends(get_session)):
    try:
        pass
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))

@router.post('/{org_id}/', responses={
    204: None,
    500: {"model": GeneralErrorResponseSchema}
})
def delete_organization(org_id: int, response: Response, session: Session = Depends(get_session)):
    try:
        org_ctl = OrganizationController(session)
        org_ctl.delete_organization(org_id)
        response.status_code = status.HTTP_204_NO_CONTENT
        return None
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))


@router.post('/', responses={
    201: {"model": OrganizationResponseSchema},
    422: {"model": GeneralErrorResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
def create_organization(org_data: OrganizationCreateSchema,
                        response: Response, session: Session = Depends(get_session)):
    try:
        create_dat
        org_ctl = OrganizationController(session)
        org = org_ctl.create_organization(org_data)
        response.status_code = status.HTTP_201_CREATED
        return OrganizationResponseSchema.from_orm(org)
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))

@router.post('/find/', responses={
    200: {"model": List[OrganizationResponseSchema]},
    422: {"model": GeneralErrorResponseSchema},
    500: {"model": GeneralErrorResponseSchema}
})
def find_organizations(org_data: OrganizationFilterSchema,
                       response: Response, session: Session = Depends(get_session)):
    try:
        pass
    except Exception as x:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GeneralErrorResponseSchema(message=str(x))




