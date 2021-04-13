import ibis
import sqlalchemy as db
from {{cookiecutter.repo_name}} import settings
from {{cookiecutter.repo_name}}.models.example_model import ExampleModel
from sqlalchemy.orm import sessionmaker

engine = {"mysql": db.create_engine(settings.SQLALCHEMY_MYSQL_URI)}


# Create sqlalchemy connection
class Connection:
    def __init__(self, db):
        self.db = db

    def create_session(self):
        Session = sessionmaker(bind=engine[self.db])
        session = Session()
        return session


# Create impala connection
class ImpalaQuery(object):
    def __init__(self):
        self.__db_conn = ibis.impala.connect(**settings.IMPALA_CONNECTION)

    def __columns_to_lower(self, df):
        df.columns = map(str.lower, df.columns)
        return df

    def execute(self, query=None, limit=None):
        return self.__columns_to_lower(self.__db_conn.sql(query).execute(limit=limit))


# Create tables
ExampleModel.__table__.create(bind=engine["mysql"], checkfirst=True)

__all__ = ["Connection", "ExampleModel", "ImpalaQuery"]
