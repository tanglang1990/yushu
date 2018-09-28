from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        data = YuShuBook.search_by_isbn(self.isbn)
        book = BookViewModel.handle_book_data(data)
        return book

    @classmethod
    def get_user_wishes(cls, uid):
        gifts = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return gifts

    @classmethod
    def get_gift_counts(cls, isbn_list):
        # 输入：['9787108006721', '9787544247252']
        # 输出：{'9787108006721':1, '9787544247252':2}]
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        count_dict = {w[1]: w[0] for w in count_list}
        return count_dict


from app.models.gift import Gift
