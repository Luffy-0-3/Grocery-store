from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import setting

# database_url ="postgresql://postgres:shadow_19@localhost:5432/project" 
database_url = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
engine = create_engine(database_url)
local_session = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()