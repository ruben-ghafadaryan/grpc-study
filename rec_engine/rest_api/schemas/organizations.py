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
    name: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None


class OrganizationUpdateSchema(OrganizationFilterSchema):
    founded_year: Optional[int] = None
    employees_count: Optional[int] = None
