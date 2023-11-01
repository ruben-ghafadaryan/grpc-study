from sqlalchemy import Column, Integer, String

from database.sqlite import Base


class OrganizationModel(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    country = Column(String, nullable=False, index=True)
    industry = Column(String, nullable=False, index=True)
    website = Column(String, nullable=True)
    description = Column(String, nullable=True)
    founded_year = Column(Integer, nullable=True)
    employees_count = Column(Integer, nullable=True)
