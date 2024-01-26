from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from models import *
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("postgresql://postgres:postgres@localhost/4DESA")
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    u = Users(username="chien", password="masterkey", email="sddfsdf")
    session.add(u)

    for class_instance in session.query(Users).all():
        print(vars(class_instance))

    session.close()
    print(database_exists(engine.url))