from typing import List

from graphql_api.schema import *

import strawberry
from graphql_api.controller import Mutations, Queries


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
