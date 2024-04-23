import databases
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "sqlite:///characters.db"
database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
Base = declarative_base()


def create_db_and_tables():
    engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)


def get_session():
    engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


def close_session():
    with Session(get_session()) as session:
        session.close()


def initialize_db():
    create_db_and_tables()
