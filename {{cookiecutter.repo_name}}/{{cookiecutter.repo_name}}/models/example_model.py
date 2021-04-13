from datetime import datetime

import pytz
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
tz = pytz.timezone("America/Buenos_Aires")


class ExampleModel(Base):
    __tablename__ = "example_table_name"

    example_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    content_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    execution_date = db.Column(db.DateTime, nullable=False, default=datetime.now(tz))
