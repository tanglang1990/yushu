from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))  # 如果上面的属性user是user1那么这里应该写成 user1.id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book') # 由于我们的book是一张空表，故这里只记录上面的isbn号即可
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def recent(cls):
        # 链式调用
        # 主体 Query
        # 子函数
        # first() all()
        recent_gift = cls.query.filter_by(
            launched=False).group_by(
            cls.isbn).order_by(
            desc(cls.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
