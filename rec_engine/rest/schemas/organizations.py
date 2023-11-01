from typing import Optional
from pydantic import BaseModel


class OrganizationBaseSchema(BaseModel):
    name: str
    description: str
    country: str
    industry: str
    website: Optional[str] = None
    founded_year: Optional[int] = None
    employees_count: Optional[int] = None

    class Config:
        orm_mode = True


class OrganizationResponseSchema(OrganizationBaseSchema):
    id: int


class OrganizationCreateSchema(OrganizationBaseSchema):
    pass


class OrganizationFilterSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    country: Optional[str]
    industry: Optional[str]
    website: Optional[str]


class OrganizationUpdateSchema(OrganizationFilterSchema):
    founded_year: Optional[int]
    employees_count: Optional[int]

