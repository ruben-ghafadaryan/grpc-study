from graphql_api.schema import *
from controllers.organizations import OrganizationController
from database.sqlite import get_session


class Mutations:
    def create_organization(self, data: OrganizationCreateInput) -> OrganizationType:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            org = org_ctl.create_organization(
                name=data.name,
                description=data.description,
                industry=data.industry,
                country=data.country,
                website=data.website,
                founded_year=data.founded_year,
                employees_count=data.employees_count
            )
            return OrganizationType(**org._asdict())

    def update_organization(self, data: OrganizationUpdateInput) -> OrganizationType:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            update_data = {}
            for key in ("name", "description", "country", "industry", "website", "founded_year", "employees_count"):
                value = getattr(data, key)
                if value is not None:
                    update_data[key] = value

            org = org_ctl.update_organization(data.id, **update_data)

            return OrganizationType(**org._asdict())

    def delete_organization(self, data: OrganizationDeleteInput) -> None:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            org_ctl.delete_organization(data.id)
            return None


class Queries:
    def get_organization_count(self) -> OrganziationCountType:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            count = org_ctl.get_organizations_count()
            return OrganziationCountType(count=count)

    def get_all_organizations(self) -> List[OrganizationType]:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            orgs = org_ctl.get_all_organizations()
            return [OrganizationType(**org._asdict()) for org in orgs]

    def get_organization(self, id: int) -> OrganizationType:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            org = org_ctl.get_organization_by_id(id)
            return OrganizationType(**org._asdict())

    def get_filtered_organizations(self, data: OrganizationFilterInput) -> List[OrganizationType]:
        session = next(get_session())
        with session:
            org_ctl = OrganizationController(session)
            filter_data = {}
            for key in ("name", "description", "country", "industry", "website"):
                value = getattr(data, key)
                if value is not None:
                    filter_data[key] = value
            orgs = org_ctl.find_organizations(**data.asdict())
            return [OrganizationType(**org._asdict()) for org in orgs]
