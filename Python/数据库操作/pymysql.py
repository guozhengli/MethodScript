import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.11.38', port=3306, user='root', passwd='apNXgF6RDitFtDQx', db='m2day03db')
# 创建游标
cursor = conn.cursor(pymysql.cursors.DictCursor)


# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from user")
result = cursor.fetchall()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

print(result)