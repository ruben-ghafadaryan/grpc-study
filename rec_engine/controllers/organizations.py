from sqlalchemy.orm import Session

from models.organizations import OrganizationModel


class OrganizationController:
    def __init__(self, session: Session):
        self._session = session

    def get_organizations_count(self) -> int:
        return self._session.query(OrganizationModel).count()

    def get_all_organizations(self) -> list[object]:
        return self._session.query(OrganizationModel).all()

    def get_organization_by_id(self, org_id: int) -> object:
        return self._session.query(OrganizationModel).get(org_id)

    def update_organization(self, org_id: int, **org_data) -> object:
        org = self.get_organization_by_id(org_id)
        for key, value in org_data.items():
            setattr(org, key, value)
        self._session.commit()
        return org

    def delete_organization(self, org_id: int) -> None:
        org = self.get_organization_by_id(org_id)
        if org:
            self._session.delete(org)
            self._session.commit()
        return None

    def find_organizations(self, **filter_data) -> list[object]:
        filters = []
        for key, value in filter_data.items():
            if value is not None:
                filters.append(getattr(OrganizationModel, key).ilike(f"%{value}%"))
        return self._session.query(OrganizationModel).filter(*filters).all()

    def create_organization(self, **org_data) -> object:
        org = OrganizationModel(**org_data)
        self._session.add(org)
        self._session.commit()
        self._session.refresh(org)
        return org
