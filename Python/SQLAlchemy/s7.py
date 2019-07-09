from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from s6 import Depart, Server, Server2Depart

engine = create_engine("mysql+pymysql://root:apNXgF6RDitFtDQx@192.168.11.38:3306/m2day03db?charset=utf8",
                       max_overflow=0, pool_size=5)
SessionClass = sessionmaker(bind=engine)
# 每次执行数据库操作时，都需要创建一个session
session = SessionClass()

# ############# 添加 #############
# session.add_all([
#     Depart(name='IT'),
#     Depart(name='测试'),
#     Depart(name='运维'),
#     Server(hostname='c1.com'),
#     Server(hostname='c2.com'),
#     Server(hostname='c3.com'),
#     Server(hostname='c4.com'),
#     Server(hostname='c5.com'),
#
# ])

# session.add_all([
#     Server2Depart(server_id=1,depart_id=1),
#     Server2Depart(server_id=1,depart_id=2),
#     Server2Depart(server_id=1,depart_id=3),
#     Server2Depart(server_id=2,depart_id=1),
#     Server2Depart(server_id=2,depart_id=2),
# ])

# 问题：创建一个部门，为补充新增3个主机
# d1 = Depart(name='运营')
# d1.servers = [Server(hostname='c6.com'),Server(hostname='c7.com'),Server(hostname='c8.com'),]
# session.add(d1)
#
# session.commit()

# ############# 查询 #############
# 运营部都有哪些机器？

# result = session.query(Server2Depart.id, Depart.name, Server.hostname).join(Depart, Server2Depart.depart_id == Depart.id,
#                                                                          isouter=True).join(Server,
#                                                                                             Server2Depart.server_id == Server.id,
#                                                                                             isouter=True).filter(Depart.name=='运营').all()
# for item in result:
#     print(item)


# obj = session.query(Depart).filter(Depart.name=='运营').first()
# for s in obj.servers:
#     print(s.id,s.hostname)

# c1.com 都给哪些部门使用了？
# obj = session.query(Server).filter(Server.hostname=='c1.com').first()
# for d in obj.departs:
#     print(d.id,d.name)

# 关闭session
session.close()
