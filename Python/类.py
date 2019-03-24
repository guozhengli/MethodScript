#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/03/22
# 功能: 命名空间的定义与说明
# 依赖包: python
# 运行方法: python 类.py
########################################################################################################

# isinstance(obj,cls)检查obj是否是类 cls 的对象
# ----- start -----
print(" isinstance ".center(100, '#'))


class A(object):
    print("Hi Ha")


obj = A()

print(isinstance(obj, A))   # return True or False
# -----  end  -----


# issubclass(sub, super)检查sub类是否是 super 类的派生类
# ----- start -----
print(" issubclass ".center(100, '#'))


class A(object):
    pass


class B(A):
    pass


print(issubclass(B, A))     # return True or False
# -----  end  -----


# 反射
# ----- start -----
print(" 反射 ".center(100, '#'))
print("""    反射的概念是由Smith在1982年首次提出的，主要是指程序可以访问、检测和修改它本身状态或行为的一种能力（自省）。
这一概念的提出很快引发了计算机科学领域关于应用反射性的研究。它首先被程序语言的设计领域所采用,并在Lisp和面向对象方面取得了成绩。
""")
print("下列方法适用于类和对象（一切皆对象，类本身也是一个对象）")
print(" hasattr ".center(100, '#'))


class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("{} say Hi".format(self.name))


obj = Foo("wangzhaojun", 20)

print(" hasattr检查是否含有某个属性 ".center(100, '#'))
print(hasattr(obj, "name"))  # return True or False

print(" getattr获取某个方法函数或属性 ".center(100, '#'))
print(getattr(obj, "name"))
sh = getattr(obj, "say_hi")
sh()
print(getattr(obj, "aaa", "不存在呀"))  # 如果获取某个属性不存在时，返回"不存在呀"

print(" setattr设置某个属性 ".center(100, '#'))
setattr(obj, "sex", "男")
print(obj.__dict__)     # {'name': 'wangzhaojun', 'age': 20, 'sex': '男'}
setattr(obj, 'show_name', lambda self: self.name+'sb')
print(obj.__dict__)
print(getattr(obj, "show_name")(obj))   # wangzhaojunsb
# 个人理解：obj等同于这个对象的所有属性即self.name 然后将这个属性传入进去 getattr是获取show_name这个属性 这个属性就是一个变量 然后print
# 打印了这个变量 然后就显示出来了

print(" delattr删除某个属性 ".center(100, '#'))
delattr(obj, "show_name")   # 如果不存在 则报错
print(obj.__dict__)

print(" __str__,__repr__,__format__使用 ".center(100, '#'))
format_dict = {
    'nat': '{obj.name}-{obj.addr}-{obj.type}',   # 学校名-学校地址-学校类型
    'tna': '{obj.type}:{obj.name}:{obj.addr}',   # 学校类型:学校名:学校地址
    'tan': '{obj.type}/{obj.addr}/{obj.name}',   # 学校类型/学校地址/学校名
}


class School:
    def __init__(self,name, addr, type):
        self.name = name
        self.addr = addr
        self.type = type

    def __repr__(self):
        return 'School(%s,%s)' %(self.name,self.addr)

    def __str__(self):
        return '(%s,%s)' %(self.name,self.addr)

    def __format__(self, format_spec):
        # if format_spec
        if not format_spec or format_spec not in format_dict:
            format_spec = 'nat'
        fmt=format_dict[format_spec]
        return fmt.format(obj=self)


s1 = School("ligz", "北京", "陈真")
print(str(s1))
print(repr(s1))
print(s1)
# 调用关系：
#   str函数或者print函数--->obj.__str__()
#   repr或者交互式解释器--->obj.__repr__()
#   如果__str__没有被定义,那么就会使用__repr__来代替输出
#   注意:这俩方法的返回值必须是字符串,否则抛出异常
print(format(s1, 'nat'))
print(format(s1, 'tna'))
print(format(s1, 'tan'))
print(format(s1, 'asfdasdffd'))

# 简易调用方式


class B:

    def __str__(self):
        return 'str : class B'

    def __repr__(self):
        return 'repr : class B'


b = B()
print('%s' % b)
print('%r' % b)

print(" __del__使用 ".center(100, '#'))
# 析构方法，当对象在内存中被释放时，自动触发执行。
# 注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。


class Foo(object):
    def __del__(self):
        print("执行我")


aa = Foo()

del aa  # 如果没有del进行删除的话 会将这个都执行完成后才会触发del
print("执行后".center(20, "#"))


print(" __new__ ".center(100, "#"))


class A:
    def __init__(self):
        self.x = 1
        print('in init function')

    def __new__(cls, *args, **kwargs):  # 真正意义上的构造器，class 执行时 先执行了new方法 然后才是init方法
        print('in new function')
        return object.__new__(A, *args, **kwargs)


a = A()
print(a.x)

# 单例模式


class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance


one = Singleton()
two = Singleton()

two.a = 3
print(one.a)
# 3
# one和two完全相同,可以用id(), ==, is检测
print(id(one))
# 29097904
print(id(two))
# 29097904
print(one == two)
# True
print(one is two)


print(" __call__对象后面添加括号来触发该方法 ".center(100, "#"))


class Foo(object):
    def __init__(self):
        print("实例化执行")

    def __call__(self, *args, **kwargs):
        print("实例化后加括号来触发")


cc = Foo()  # init 来触发
cc()    # call 来触发


print(" __len__ ".center(100, "#"))


class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __len__(self):
        return len(self.__dict__)


a = A()
print(len(a))

print(" __hash__ ".center(100, "#"))


class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __hash__(self):
        return hash(str(self.a) + str(self.b))


a = A()
print(hash(a))  # 默认按照id来进行hash


print(" __eq__ ".center(100, "#"))


class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __eq__(self, obj):
        if self.a == obj.a and self.b == obj.b:
            return True


a = A()
b = A()
print(a == b)
# -----  end  -----



