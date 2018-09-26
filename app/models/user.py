from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash

from app.models.base import Base


class User(Base):
    # __tablename__ = 'yushu_user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    # password = Column(String(128), nullable=False)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)

    @property
    def password(self):
        return self._password

    # 可能大家能够理解却还是不会用property的getter与setter
    # 记住代码一定要尝试去写，这样才能写出地道的python代码
    # 通过这种方式我们还能对属性实现只读，在下述方法中抛出异常，而不设置值即可
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
