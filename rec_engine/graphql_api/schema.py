from typing import List, Optional

import strawberry


@strawberry.type
class OrganizationType:
    id: int
    name: str
    description: str
    country: str
    industry: str
    website: Optional[str] = None
    founded_year: Optional[int] = None
    employees_count: Optional[int] = None


@strawberry.input
class OrganizationCreateInput:
    name: str
    description: str
    country: str
    industry: str
    website: Optional[str] = None
    founded_year: Optional[int] = None
    employees_count: Optional[int] = None


@strawberry.input
class OrganizationFilterInput:
    name: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None


@strawberry.input
class OrganizationUpdateInput(OrganizationFilterInput):
    id: int
    founded_year: Optional[int] = None
    employees_count: Optional[int] = None


@strawberry.input
class OrganizationDeleteInput:
    id: int
