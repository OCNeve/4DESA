from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from .models import Base
from sqlalchemy.orm import sessionmaker

class DBA:
    def __init__(self):
        self.engine = create_engine("postgresql://postgres:postgres@localhost/4DESA")

        if self.create_database(): # If database did not previously exist
            Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def getSession(self):
        return self.session

    def create_database(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            return True
        return False

    def close_seesion(self):
        self.session.close()
    