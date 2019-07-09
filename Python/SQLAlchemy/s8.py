"""
连接相关
"""
import threading
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:apNXgF6RDitFtDQx@192.168.11.38:3306/m2day03db?charset=utf8",
                       max_overflow=0, pool_size=5)
SessionClass = sessionmaker(bind=engine)
# 每次执行数据库操作时，都需要创建一个session

def task():
    # 从数据库连接池获取一个连接。
    session = SessionClass()
    # 查询
    cursor = session.execute('select sleep(3)')
    result = cursor.fetchall()
    session.close()
    print(result)


for i in range(20):
    t = threading.Thread(target=task)
    t.start()