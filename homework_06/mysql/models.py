from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalCount(Base):
    __tablename__ = 'Total_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Total_count(" \
               f"id='{self.id}'," \
               f"count='{self.count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)


class CountByType(Base):
    __tablename__ = 'Count_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Count_by_type(" \
               f"id='{self.id}'," \
               f"type='{self.type}', " \
               f"count='{self.count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(10), nullable=False)
    count = Column(Integer, nullable=False)


class Top10_request_by_count(Base):
    __tablename__ = 'Top10requests_sorted_by_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Top10requests_sorted_by_count(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"count='{self.count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(200), nullable=False)
    count = Column(Integer, nullable=False)


class Top5_4XX_by_size(Base):
    __tablename__ = 'Top5_4XX_requests_sorted_by_size'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Top5_4XX_requests_sorted_by_size(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"rc='{self.rc}'" \
               f"size='{self.size}'" \
               f"ip='{self.ip}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(250), nullable=False)
    rc = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(15), nullable=False)


class Top5_users_5XX_by_count(Base):
    __tablename__ = 'Top5_users_5XX_by_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Top5_users_5XX_by_count(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}'" \
               f"count='{self.count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(200), nullable=False)
    count = Column(Integer, nullable=False)
