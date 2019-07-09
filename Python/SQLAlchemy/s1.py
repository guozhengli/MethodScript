import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

engine = create_engine(
    "mysql+pymysql://root:duduadmin@10.168.101.21:3308/reapal_cmdb?charset=utf8",   # reapal_cmdb 数据库名  duduadmin  密码  root 用户
    max_overflow=5,  # 超过连接池大小外最多创建的连接
    pool_size=1,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

def task(arg):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    # cursor.execute("select * from user",[])
    cursor.execute("select * from asset_host",[])   # sql 查询语句
    # cursor.execute("select sleep(3)")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(result)

for i in range(20):
    t = threading.Thread(target=task, args=(i,))
    t.start()

# 基于Session执行原生SQL （*******）
"""
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:duduadmin@10.168.101.21:3308/reapal_cmdb?charset=utf8", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)
session = Session()

# 查询
cursor = session.execute('select * from asset_host')
result = cursor.fetchall()
print(result)

# 添加
# cursor = session.execute('insert into users(name) values(:value)',params={"value":'wupeiqi'})
# session.commit()
# print(cursor.lastrowid)

session.close()
"""