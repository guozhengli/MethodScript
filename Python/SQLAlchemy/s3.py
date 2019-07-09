
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from s2 import Users

engine = create_engine("mysql+pymysql://root:duduadmin@10.168.101.21:3308/reapal_cmdb?charset=utf8", max_overflow=0, pool_size=5)
SessionClass = sessionmaker(bind=engine)
# 每次执行数据库操作时，都需要创建一个session
session = SessionClass()

# ############# 添加 #############
# obj = Users(name="alex")
# session.add(obj)
# 提交事务
# session.commit()
# ############# 查询 #############
# result = session.query(Users).all()
# for row in result:
#     print(row.id,row.name)

# result = session.query(Users).filter(Users.id > 1)
# for row in result:
#     print(row.id,row.name)
# ############# 删除 #############
# session.query(Users).filter(Users.id > 1).delete()
# session.commit()
# ############# 修改 #############
# session.query(Users).filter(Users.id > 0).update({'name':'型谱'})
# session.commit()


# 关闭session
session.close()