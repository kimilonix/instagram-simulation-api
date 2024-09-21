from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker 

engine = creat_engine("sqlite:///Instagram.db", connect_args={'check_same_thread':False})
Base = declarative_base()

sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    session = sessionlocal()
    try:
        yield session
    finally:
        session.close()