from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_app.social_generic.models import Models
from sqlalchemy.orm import sessionmaker
from flask_app.social_generic.database_access import DBA

if __name__ == '__main__':
    dba = DBA()
    session = dba.getSession()
    u = Models.users.value(username="chien", password="masterkey", email="sddfsdf")
    session.add(u)

    for class_instance in session.query(Models.users.value).all():
        print(vars(class_instance))

    session.close()