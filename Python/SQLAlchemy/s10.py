"""
连接相关
"""
import threading
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session


engine = create_engine("mysql+pymysql://root:apNXgF6RDitFtDQx@192.168.11.38:3306/m2day03db?charset=utf8",
                       max_overflow=0, pool_size=5)
SessionClass = sessionmaker(bind=engine)
# 原来的session = SessionClass()
# from sqlalchemy.orm.session import Session
# old_session = SessionClass()
# print(type(old_session))

# 新的session = scoped_session对象
"""
session = {
    session_factory=老session类,
    registry=ThreadLocalRegistry()={
        createfunc=老session类,
        registry = threading.local()
    }
}
"""
session = scoped_session(SessionClass)

#session.query()
"""
class scoped_session(object):
    def query(self, *args, **kwargs):
        # self.registry() -> ThreadLocalRegistry.__call__ -> 为一个线程创建一个老session对象
        # getattr(老session对象, 'query') -> 获取原来的query方法
        # 原来的query方法(*args, **kwargs)
        return getattr(self.registry(), 'query')(*args, **kwargs)

    def merge(self, *args, **kwargs):
        return getattr(self.registry(), 'merge')(*args, **kwargs)

    def refresh(self, *args, **kwargs):
        return getattr(self.registry(), 'refresh')(*args, **kwargs)

    def rollback(self, *args, **kwargs):
        return getattr(self.registry(), 'rollback')(*args, **kwargs)  

"""



