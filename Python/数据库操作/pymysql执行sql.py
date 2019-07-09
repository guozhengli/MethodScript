import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.11.38', port=3306, user='root', passwd='apNXgF6RDitFtDQx', db='m2day03db')
# 创建游标
cursor = conn.cursor(pymysql.cursors.DictCursor)


# 执行SQL，并返回收影响行数
# sql = "insert into user(name,email,pwd) values(%s,%s,%s)"
# effect_row = cursor.execute(sql,['jiliang','jl@live.com','123'])

sql = "insert into user(name,email,pwd) values(%(n)s,%(m)s,%(p)s)"
effect_row = cursor.execute(sql,{'n':'jiwen','m':'jiwen@live.com','p':'123'})


# 增加、删除、修改
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

