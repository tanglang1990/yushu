from collections import namedtuple

from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))  # 如果上面的属性user是user1那么这里应该写成 user1.id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book') # 由于我们的book是一张空表，故这里只记录上面的isbn号即可
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        data = YuShuBook.search_by_isbn(self.isbn)
        book = BookViewModel.handle_book_data(data)
        return book

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

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        # 根据传入的一组isbn，到Wish表中计算出某个礼物
        # 的Wish心愿数量
        # 输入：['9787108006721', '9787544247252']
        # 输出：{'9787108006721':1, '9787544247252':2}]
        # 一个数量吗？
        # 一组数量
        # 条件表达式
        # mysql in
        # isbn wish的数量
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()
        # count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        count_dict = {w[1]: w[0] for w in count_list}
        return count_dict

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False
