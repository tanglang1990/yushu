# SQLAlchemy
* ORM 全称 Object Relational Mapping, 翻译过来叫对象关系映射。简单的说， ORM 将数据库中的表与面向对象语言中的类建立了一种对应关系。这样，我们要操作数据库， 数据库中的表或者表中的一条记录就可以直接通过操作类或者类实例来完成。

* SQLAlchemy 是Python 社区最知名的 ORM 工具之一，为高效和高性能的数据库访问设计， 实现了完整的企业级持久模型。 支持几乎所有主流数据库MySQL, SQLite, PostgreSQ， Microsoft SQL Server, Oracle 等等。此外还有Django ORM但是被限制在Django框架中使用。

### SQLAlchemy 官方文档

* 官网: [http://www.sqlalchemy.org/](http://www.sqlalchemy.org/)
* github: [https://github.com/zzzeek/sqlalchemy](https://github.com/zzzeek/sqlalchemy)
* 官方文档: [http://www.sqlalchemy.org/docs/](http://www.sqlalchemy.org/docs/)

### 在Flask中的应用 flask-sqlalchemy
* 基于SQLAlchemy开发
* github: https://github.com/mitsuhiko/flask-sqlalchemy
* 官方文档: http://flask-sqlalchemy.pocoo.org/
* 中文文档: http://www.pythondoc.com/flask-sqlalchemy/

### 安装
```
$ pip install SQLAlchemy
```


###  创建连接

创建Engine实例，它提供数据库的核心接口

#### 语法:
```python
dialect+driver://username:password@host:port/database
```

#### 连接实例
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///mysqlit.db', echo=True) # 连接sqlite，会产生db文件
engine = create_engine('sqlite:///:memory:', echo=True) # 直接在内存中
engine = create_engine("mysql://scott:tiger@hostname/dbname?charset=utf8", encoding='latin1', echo=True) #留意?charset=utf8
```

#### 注意
* 创建Engine并未真正连接数据库，调用Engine.execute()或Engine.connect()时，Engine才真正访问数据库。
* 连接mysql的时候特别留意加上"?charset=utf8"，可以防止出现乱码

#### 更多实列： http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls


### 模型

#### 定义模型 Declare a Mapping

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base() # 创建基类

class User(Base):
    __tablename__ = 'user' # 必须的对应数据库表

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

```
* 主键用 primary_key=True 标记。可以把多个键标记为主键，此时它们作为复合主键。

* 列的类型是 Column 的第一个参数。您可以直接提供它们或进一步规定（比如提供一个长度）。
下面的类型是最常用的(不要求100%记住):
### 
列类型 | 描述
-----| -----
Integer|	一个整数
String (size)|	有长度限制的字符串
Text|	一些较长的 unicode 文本
DateTime|	表示为 Python datetime 对象的 时间和日期
Float|	存储浮点值
Boolean	|存储布尔值
PickleType|	存储为一个持久化的 Python 对象
LargeBinary	|存储一个任意大的二进制数据


#### 一对多(one-to-many)关系
```python
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    addresses = relationship("Address", backref="user", order_by="Address.id") # 一对一只需要加上 uselist=False

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    email_address = Column(String)
```
* 关系使用 relationship() 函数表示
* 此处用户地址为1对多关系
* 如果您想要一对一关系，您可以把 uselist=False
* relationship中的"Address"使用字符串是因为在此时还没有定义
* 那么backref意味着什么？backref 是一个在 Address 类上声明新属性的简单方法。您也可以使用 address.user 来获取使用该地址(address)的用户(user)。

#### 定义多对多关联关系
```python
from sqlalchemy import Table

tags = Table('tags',
    Column('tag_id', Integer, ForeignKey('tag.id')),
    Column('page_id', Integer, ForeignKey('page.id'))
)

class Page(Base):
    id = Column(db.Integer, primary_key=True)
    tags = relationship('Tag', secondary=tags,
        backref=backref('pages', lazy='dynamic'))

class Tag(Base):
    id = Column(Integer, primary_key=True)
```
* 如果您想要用多对多关系，您需要定义一个用于关系的辅助表。
* 每个 tag 的页面列表（ Tag.pages）是一个动态的反向引用。 正如上面提到的，这意味着您会得到一个可以发起 select 的查询对象。


#### 同步数据库
```python
Base.metadata.create_all(engine)
```

### 增删改查（CURD）

CURD代表创建（Create）、更新（Update）、读取（Retrieve）和删除（Delete）操作。

#### 会话 Session

当我们开始我们的应用程序，需要在创建Engine的同一级别定义Session工厂类

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)   # 创建Session工厂类

# 如果没有engine可以先这样创建
# Session = sessionmaker()
# 等到有engine了再绑定
# Session.configure(bind=engine)

session = Session() # 从连接池获取会话，可理解成加强版的事务
dn_user = User(name='ten', fullname='ten tyrion', password='edspassword')
session.add(ed_user)
session.commit() # 事务提交
```

#### 插入记录

##### 添加一个用户
```python
dn_user = User(name='ten', fullname='ten tyrion', password='edspassword')
session.add(ed_user)
session.commit()
```

##### 添加多个用户
```python
session.add_all([
     User(name='wendy', fullname='Wendy Williams', password='foobar'),
     User(name='mary', fullname='Mary Contrary', password='xxg527'),
     User(name='fred', fullname='Fred Flinstone', password='blah')])
session.commit()
```

#### 回滚
```python
session.rollback()
```

#### 查询
查询是重中之重

参考文档 http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#querying


#### 删除
```python
jack = session.query(User).\
                        options(joinedload(User.addresses)).\
                        filter_by(name='jack').one()
session.delete(jack)
```

#### 修改
```python
jack = session.query(User).\
                        options(joinedload(User.addresses)).\
                        filter_by(name='jack').one()
jack.name = 'ten'
```




### 经典映射（效果同上,暂时不讲）
```python
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('user', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(User, user)

address = Table('address', metadata,
            Column('id', Integer, primary_key=True),
            Column('user_id', Integer, ForeignKey('user.id')),
            Column('email_address', String(50))
            )

mapper(User, user, properties={
    'addresses' : relationship(Address, backref='user', order_by=address.c.id)
})

mapper(Address, address)

```



