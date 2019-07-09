
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from s4 import Person,PersonType

engine = create_engine("mysql+pymysql://root:apNXgF6RDitFtDQx@192.168.11.38:3306/m2day03db?charset=utf8", max_overflow=0, pool_size=5)
SessionClass = sessionmaker(bind=engine)
# 每次执行数据库操作时，都需要创建一个session
session = SessionClass()

# ############# 添加 #############
"""
session.add_all([
    PersonType(caption="普通用户"),
    PersonType(caption="超级用户"),
    PersonType(caption="SVIP用户"),
])
"""

"""
session.add_all([
    Person(name="李杰",type_id=1),
    Person(name="征集文",type_id=1),
    Person(name="兴普",type_id=2),
])
"""

"""
obj = session.query(PersonType).filter(PersonType.id==2).first()
session.add_all([
    Person(name="李杰1",ptype=obj),
    Person(name="征集文1",ptype=obj),
    Person(name="兴普1",ptype=obj),
])
"""

"""
obj = Person(name='宏伟',ptype=PersonType(caption="VVIP"))
session.add(obj)
"""

# session.commit()

# ############# 查询 #############
# 查询所有用户，并打印姓名
# obj_list = session.query(Person).all()
# for obj in obj_list:
#     print(obj.name)

# 查询所有用户，并打印姓名+用户类型名称
# obj_list = session.query(Person).all()
# for obj in obj_list:
#     print(obj.name,obj.type_id,obj.ptype.caption)

# 查询所有用户，并打印姓名+用户类型名称
# result = session.query(Person.nid,Person.name.label('nnn'),PersonType.caption).join(PersonType,Person.type_id==PersonType.id,isouter=True).all()
# for row in result:
#     print(row.nnn,row.caption)


# 找到属于某个用户类型的所有人。
# obj = session.query(PersonType).filter(PersonType.id == 2).first()
# print(obj.id)
# print(obj.caption)
# print(obj.pers)

# result = session.query(Person).filter(Person.type_id == 2).all()
# print(result)


# 关闭session
session.close()