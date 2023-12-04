from typing import List

from graphql_api.schema import *

import strawberry
from graphql_api.controller import Mutations, Queries

from database.sqlite import get_session

import asyncio
from typing import AsyncGenerator

from graphql_api.schema import *
from strawberry.types import Info
from controllers.organizations import OrganizationController
from database.sqlite import get_session
from graphql_api.schema import OrganziationCountType


@strawberry.type
class Query:
    all_organizations: List[OrganizationType] = strawberry.field(resolver=Queries.get_all_organizations)
    filtered_organizations: List[OrganizationType] = strawberry.field(resolver=Queries.get_filtered_organizations)
    organization: OrganizationType = strawberry.field(resolver=Queries.get_organization)


@strawberry.type
class Mutation:
    create_organization: OrganizationType = strawberry.field(resolver=Mutations.create_organization)
    update_organization: OrganizationType = strawberry.field(resolver=Mutations.update_organization)
    delete_organization = strawberry.field(resolver=Mutations.delete_organization)


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def organization_created(self) -> OrganziationCountType:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            count = org_ctl.get_organizations_count()
            while True:
                await asyncio.sleep(1)
                new_count = org_ctl.get_organizations_count()
                if new_count > count:
                    count = new_count
                    yield OrganziationCountType(count=count)
