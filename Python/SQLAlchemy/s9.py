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
# 创建的scoped_session Session对象
# 当线程去调用
#       session.query()
#       session.add
#       session.add_all
# scoped_session内部会为每个线程创建一个新的Session对象，让他来使用。
session = scoped_session(SessionClass)


def task():
    # 查询
    cursor = session.execute('select sleep(3)')
    result = cursor.fetchall()
    session.remove()
    print(result)


for i in range(20):
    t = threading.Thread(target=task)
    t.start()