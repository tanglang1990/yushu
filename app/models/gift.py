from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import db


class Gift(db.Model):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))  # 如果上面的属性user是user1那么这里应该写成 user1.id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book') # 由于我们的book是一张空表，故这里只记录上面的isbn号即可
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)
