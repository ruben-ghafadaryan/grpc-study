from sqlalchemy.orm import Session

from models.organizations import OrganizationModel

class OrganizationController:
    def __init__(self, session: Session):
        self._session = session

    def get_all_organizations(self) -> list[object]:
        return self._session.query(OrganizationModel).all()

    def get_organization_by_id(self, org_id: int) -> object:
        return self._session.query(OrganizationModel).get(org_id)

    def update_organization(self, org_id: int, org_data: dict) -> object:
        org = self.get_organization_by_id(org_id)
        for key, value in org_data.items():
            setattr(org, key, value)
        self._session.commit()
        return org

    def delete_organization(self, org_id: int) -> None:
        org = self.get_organization_by_id(org_id)
        self._session.delete(org)
        self._session.commit()
        return None

    def find_organizations(self, filters: dict) -> list[object]:
        return []

    def create_organization(self, org_data: dict) -> object:
        org = OrganizationModel(**org_data)
        self._session.add(org)
        self._session.commit()
        return org
