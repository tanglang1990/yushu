from sqlalchemy import Column, Integer, Boolean

from app.models.base import db


class Gift(db.Model):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
