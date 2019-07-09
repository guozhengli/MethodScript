import pymysql
import threading
from DBUtils.PooledDB import PooledDB, SharedDBConnection
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=20,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    #maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='192.168.11.38',
    port=3306,
    user='root',
    passwd='apNXgF6RDitFtDQx',
    db='m2day03db',
    charset='utf8'
)


def connect():
    # 创建连接
    # conn = pymysql.connect(host='192.168.11.38', port=3306, user='root', passwd='apNXgF6RDitFtDQx', db='m2day03db')
    conn = POOL.connection()
    # 创建游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    return conn,cursor

def close(conn,cursor):
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def fetch_one(sql,args):
    conn,cursor = connect()
    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute(sql,args)
    result = cursor.fetchone()
    close(conn,cursor)

    return result

def fetch_all(sql,args):
    conn, cursor = connect()

    # 执行SQL，并返回收影响行数
    cursor.execute(sql,args)
    result = cursor.fetchall()

    close(conn, cursor)
    return result

def insert(sql,args):
    """
    创建数据
    :param sql: 含有占位符的SQL
    :return:
    """
    conn, cursor = connect()

    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute(sql,args)
    conn.commit()

    close(conn, cursor)

def delete(sql,args):
    """
    创建数据
    :param sql: 含有占位符的SQL
    :return:
    """
    conn, cursor = connect()

    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute(sql,args)

    conn.commit()

    close(conn, cursor)

    return effect_row

def update(sql,args):
    conn, cursor = connect()

    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute(sql, args)

    conn.commit()

    close(conn, cursor)

    return effect_row