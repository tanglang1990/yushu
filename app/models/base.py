from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
