#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/02/25
# 功能: 命名空间的定义与说明
# 依赖包: python
# 运行方法: python 进程.py
########################################################################################################


print(" process使用 ".center(100, "#"))
"""
process说明

Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）

强调：
1. 需要使用关键字的方式来指定参数
2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号

参数介绍：
1 group参数未使用，值始终为None
2 target表示调用对象，即子进程要执行的任务
3 args表示调用对象的位置参数元组，args=(1,2,'egon',)
4 kwargs表示调用对象的字典,kwargs={'name':'egon','age':18}
5 name为子进程的名称
"""

# process
# ----- start -----

"""
方法介绍

1 p.start()：启动进程，并调用该子进程中的p.run() 
2 p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法  
3 p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，
    使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
4 p.is_alive():如果p仍然运行，返回True
5 p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。
    timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程 
    
属性介绍

1 p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
2 p.name:进程的名称
3 p.pid：进程的pid
4 p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)
5 p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。
    这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）

在windows中使用process模块的注意事项

在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，在创建子进程的时候会自动 import 启动它的这个文件，
而在 import 的时候又执行了整个文件。因此如果将process()直接写在文件中就会无限递归创建子进程报错。
所以必须把创建子进程的部分使用if __name__ ==‘__main__’ 判断保护起来，import 的时候  ，就不会递归运行了。
"""
# 运行的第一个子进程

import time
from multiprocessing import Process


def f(name):
    print("hello", name)
    print("我是子进程")


# if __name__ == '__main__':
#     p = Process(target=f, args=("bob",))
#     p.start()
#     time.sleep(1)
#     print("执行主进程的内容了")

print(" join使用 ".center(100, "#"))

#
# def f(name):
#     print("hello", name)
#     print("我是子进程")
#     time.sleep(10)
#
#
# if __name__ == '__main__':
#     p = Process(target=f, args=("bob",))
#     p.start()
#     p.join(timeout=2)
#     print("执行主进程的内容了")

print(" 查看主进程和子进程进程号 ".center(100, "#"))
# import os
# from multiprocessing import Process
#
#
# def f(x):
#     print("子进程：{}, 父进程: {}".format(os.getpid(), os.getppid()))
#     return x*x
#
#
# if __name__ == '__main__':
#     print('主进程id ：', os.getpid())
#     for i in range(5):
#         p = Process(target=f, args=(i,))
#         p.start()

# 进阶，多个进程同时运行（注意，子进程的执行顺序不是根据启动顺序决定的）

print(" 多个进程同时运行 ".center(100, "#"))
import time
# from multiprocessing import  Process
#
# def f(name):
#     print("我是子进程", name)
#     time.sleep(1)
#
# p_list = []
# for i in range(5):
#     p = Process(target=f, args=(i,))
#     p.start()
#     p_list.append(p)
# print(p_list)

print(" 多个进程同时运行 join方法 ".center(100, "#"))

import time
from multiprocessing import  Process


def f(name):
    print("我是子进程", name)
    time.sleep(1)

#
# p_list = []
# for i in range(5):
#     p = Process(target=f, args=(i,))
#     p.start()
#     p_list.append(p)
#     # p.join()
#     [p.join() for p in p_list]
# print("父进程执行")
# print(p_list)
# -----  end  -----

# 通过继承Process类开启进程
# ----- start -----
import os
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(os.getpid())
        print("%s 正在和女人聊天" %self.name)

# p1 = MyProcess("wupeiqi")
# p2 = MyProcess("jiangdan")
# p3 = MyProcess("xiaocilou")
#
# p1.start()
# p2.start()
# p3.start()
#
# p1.join()
# p2.join()
# p3.join()
#
# print("主进程")


print(" 进程之间的数据隔离问题 ".center(100, '#'))
#
# def work():
#     global n
#     print("子进程内:", n)
#     n = 0
#     print("子进程内:",n)
#
# if __name__ == '__main__':
#     n = 100
#     p = Process(target=work)
#     p.start()
#     print("主进程内:", n)


print(" 守护进程 ".center(100, "#"))

# 1、守护进程 是随主进程的代码结束而结束
# 2、守护进程中不可在开启子进程
# 3、守护进程要在start之前
import time
from multiprocessing import Process

# 这种情况下， 当主进程都退出了 但子进程还在继续执行

# def c_time():
#     while True:
#         time.sleep(1)
#         print("我停留了1秒钟")
#
#
# if __name__ == '__main__':
#     p = Process(target=c_time)
#     p.start()
#
#     for i in range(100):
#         time.sleep(0.1)
#         print("*"*i)

# 开启守护进程后，当主进程代码都结束了 子进程也会退出


# def c_time():
#     while True:
#         time.sleep(1)
#         print("我停留了1秒")
#
#
# if __name__ == '__main__':
#     p = Process(target=c_time)
#     p.daemon = True     # 开启守护进程
#     p.start()
#
#     for i in range(100):
#         time.sleep(0.1)
#         print("*"*i)


# 开启守护进程后，只随着主进程的代码结束而结束，不涉及其他子进程


# def fun():
#     print("子进程")
#     time.sleep(15)
#     print("结束")
#
#
# def c_time():
#     while True:
#         time.sleep(1)
#         print("我停留了1秒")
#
#
# if __name__ == '__main__':
#     p = Process(target=c_time)
#     p.daemon = True     # 开启守护进程
#     p.start()
#
#     p2 = Process(target=fun)
#     p2.start()
#
#     for i in range(100):
#         time.sleep(0.1)
#         print("*"*i)


print(" 回调函数 ".center(100, "#"))


def callback_fun(cont):
    print("我是回调函数哈哈", cont)


def fun(c):
    print("处理问题楼")
    return c*100

#
# from multiprocessing import Pool
#
# p = Pool(5)
# p.apply_async(fun, (10,), callback=callback_fun)
# time.sleep(2)


print(" Lock ".center(100, '#'))

from multiprocessing import Process, Lock
import json
# 为了数据安全，需要一个锁来控制，虽然减少了处理性能

# 做一个锁的抢票功能

import time, random
def napiao(i):
    with open("tick.txt") as f:
        tick = json.load(f)['count']
    print("{} 拿到{}票了".format(i, tick))


def yongpiao(i):
    with open("tick.txt") as f:
        old_tick = json.load(f)['count']

    time.sleep(random.random())

    if old_tick > 0:
        with open("tick.txt", 'w') as f:
            json.dump({"count": old_tick - 1}, f)
        print("买到了")
    else:
        print("没买到")

def run(i, lock):
    napiao(i)
    lock.acquire()
    yongpiao(i)
    lock.release()

#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(20):
#         p = Process(target=run, args=(i,lock))
#         p.start()



print(" 信号量 ".center(100, "#"))
# 信号量可以粗略的理解为 Lock只有一把 信号量有多把
from multiprocessing import Semaphore

# 做一个信号量的 迷你唱吧的排队唱歌功能
import time, random

def func(i, sem):
    sem.acquire()
    print("{} 进来唱歌了".format(i))
    time.sleep(random.randint(1,3))
    sem.release()
    print("{} 唱完了".format(i))


# if __name__ == '__main__':
#     sem = Semaphore(10)
#     for i in range(100):
#         p = Process(target=func, args=(i, sem))
#         p.start()


print(" 生产者消费者 ".center(100, "#"))
# 生产者消费者模型 这里利用多进程+queue方法实现 但queue功能只是队列 在消费者都消费完后还得计算结束之类的 所以这里用JoinableQueue代替
# JoinableQueue 拥有task_none功能 就是消费后通知已消费完
import time, random
from multiprocessing import JoinableQueue, Process

def shengchanzhe(q, food):
    for i in range(5):
        q.put("{}-{}".format(food, i))
        print("生产了 {}".format(food))
        time.sleep(random.randint(1,5))
    q.join()


def xiaofeizhe(q, name):
    while True:
        food = q.get()
        if food == None: break
        print("{} 吃了 {}".format(name, food))

        q.task_done()


# if __name__ == '__main__':
#     jq = JoinableQueue()
#     p1 = Process(target=shengchanzhe, args=(jq, "泔水"))   # 生产者
#     p1.start()
#     p2 = Process(target=shengchanzhe, args=(jq, "骨头"))   # 生产者
#     p2.start()
#
#     c1 = Process(target=xiaofeizhe, args=(jq, "alex"))     # 消费者
#     c1.daemon = True
#     c1.start()
#     c2 = Process(target=xiaofeizhe, args=(jq, "sb"))     # 消费者
#     c2.daemon = True
#     c2.start()
#     c3 = Process(target=xiaofeizhe, args=(jq, "quebi"))     # 消费者
#     c3.daemon = True
#     c3.start()
#
#     p1.join()
#     p2.join()

print(" Pipe管道 ".center(100, '#'))
# 其实 队列就等同于 管道+锁
# 管道  双向通信 数据不安全 偏底层一些
# 关系可以理解为：
    # Pipe
    # Queue 封装了Pipe+Lock
    # JoinableQueue 封装了Queue
    # 从上往下继承

from multiprocessing import Pipe, Process

def func(foo,son):
    foo.close()     # 因为foo用不到所以将其关闭掉
    print(son.recv())


# if __name__ == '__main__':
#     foo, son = Pipe()
#     p = Process(target=func, args=(foo, son))
#     p.start()
#     son.close()     # 因为son用不到所以将其关闭掉
#     foo.send('cccccc')
#     p.join()

print(" Message ".center(100, '#'))
from multiprocessing import Manager, Process
# 进程间数据共享

def func(dc, lock):
    # print(dc)
    lock.acquire()
    dc['count'] -= 1
    lock.release()

    # dc['count'] = dc['count'] -1

# if __name__ == '__main__':
#     lock = Lock()   # 加上锁 确保 数据安全
#     m = Manager()
#     dic = m.dict({"count":10})
#     # dic = {"count":10}
#     j = []
#     for i in range(10):
#         p = Process(target=func, args=(dic,lock))
#         p.start()
#         # p.join()    # 如果在这里添加了join就相当于同步了 没有意义 可以改成这样
#         j.append(p)
#
#     [i.join() for i in j]
#     print(dic)  # 可以通过结果看出来count值并非都是0 因为Manage为数据不安全的 所以需要加个锁 或者直接上队列就可以了

print(" Event ".center(100, '#'))

from multiprocessing import Event
from multiprocessing import Process

# 模拟红绿灯

def signal_lamp(e):
    while True:
        if e.is_set():
            time.sleep(3)
            print("红灯停")
            e.clear()
        else:
            time.sleep(3)
            print("路灯行")
            e.set()

def car(i,e):
    e.wait()
    print("{}车 通过".format(i))


# if __name__ == '__main__':
#     e = Event()
#     tra = Process(target=signal_lamp, args=(e,))
#     tra.start()
#     for i in range(10):
#         if i%6 == 0:
#             time.sleep(random.randint(1,3))
#         car_pro = Process(target=car, args=(i,e))
#         car_pro.start()
#
#     tra.join()

print(' 线程池 '.center(100, '#'))
from concurrent import futures
# futures.ThreadPoolExecutor  # 线程池
import time
import random
thread_tool = futures.ThreadPoolExecutor(5)

f_lst = []

# def funcname(i):
#     print(i)
#     time.sleep(random.random())
#     return i*'*'
#
# def call(i):
#     print(i.result(),'ddddddd')
#
# for i in range(10):
#     f = thread_tool.submit(funcname, i)
#     f_lst.append(f)
#     f.result()

# [print(i.result()) for i in f_lst]
# thread_tool.map(funcname, range(10))    # 实现了 submit result 方法 但是不能获取 return 值

# thread_tool.submit(funcname, 1).add_done_callback(call)   # 回调函数




# -----  end  -----


