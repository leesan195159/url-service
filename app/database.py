from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "mysql+pymysql://ls:1234@localhost/url_service"

engine = create_engine(database_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
