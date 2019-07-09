#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship

Base = declarative_base()

# ##################### 多对多示例 #########################

class Server2Depart(Base):
    __tablename__ = 'server2depart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    depart_id = Column(Integer, ForeignKey('depart.id'))

    __table_args__ = (
        # 联合唯一索引
        UniqueConstraint('server_id', 'depart_id', name='uix_depart_server'),
    )

class Depart(Base):
    __tablename__ = 'depart'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

    # 与生成表结构无关，仅用于查询方便
    servers = relationship('Server', secondary='server2depart', backref='departs')

class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)


if __name__ == '__main__':
    engine = create_engine(
        "mysql+pymysql://root:apNXgF6RDitFtDQx@192.168.11.38:3306/m2day03db?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)