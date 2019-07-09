
class Foo(object):
    pass

setattr(Foo,'func',lambda self,x:x)

obj = Foo()
print(obj.func(1))