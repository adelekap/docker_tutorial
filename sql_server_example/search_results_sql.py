import sqlalchemy as sqla
import sqlalchemy_utils as sqla_utils
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = 'mssql+pyodbc://sa:reallyStrongPwd123@127.0.0.1:1433/DemoDB?driver=ODBC+Driver+13+for+SQL+Server'
ENGINE = sqla.create_engine(CONNECTION_STRING)
BASE = declarative_base()


class SearchResults(BASE):
    __tablename__ = 'SearchResults'
    id = sqla.Column(sqla.Integer, primary_key=True)
    query = sqla.Column(sqla.String)
    result = sqla.Column(sqla.String)


def create_session():
    BASE.metadata.create_all(bind=ENGINE)
    Session = sessionmaker()
    Session.configure(bind=ENGINE)
    session = Session()

    return session


def create_database():
    if not sqla_utils.database_exists(CONNECTION_STRING):
        sqla_utils.create_database(CONNECTION_STRING)


def insert_data(query, result):
    create_database()
    session = create_session()

    row = SearchResults(query=query, result=result)

    session.add(row)
    session.commit()
    session.close()
