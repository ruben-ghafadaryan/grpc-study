from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_file = Path(__file__).parent / "data" / "rec_engine.db"

print(db_file)
SQL_DATA_FILE = f"sqlite:///{db_file}"
print(SQL_DATA_FILE)

engine = create_engine(SQL_DATA_FILE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


Base = declarative_base()
