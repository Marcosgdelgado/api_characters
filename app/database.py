import databases
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# URL  for the database connection.
DATABASE_URL = "sqlite:///characters.db"
database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
Base = declarative_base()
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db_and_tables():
    """Create the database and tables if they don't exist"""
    Base.metadata.create_all(bind=engine)


def get_session():
    """get connection to database

    Yields:
        Session: connection to the characters.db
    """
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


def close_session():
    """close current session"""
    with Session(get_session()) as session:
        session.close()
