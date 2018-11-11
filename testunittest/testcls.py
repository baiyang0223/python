'''
@Author: Baiy
@Date: 2018-11-11 21:35:41
@LastEditors: Baiy
@LastEditTime: 2018-11-11 22:06:57
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: python中cls方法和self方法
'''


class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print('hello', name)
      
    def foo2(self, name):
        print('hello', name)
    @classmethod
    def foo3(cls, name):
        print('hello', name)


class B(object):
    b = 'b'
    @staticmethod
    def foo1(name):
        print('hello-1', name)
      
    def foo2(self, name):
        print('hello-2', name)

    @classmethod
    def foo3(cls, name):
        print(cls)
        print('hello-3', name)
        print(cls.b)  # 可通过cls来直接访问内部参数，甚至不需要定义对象
        cls().foo2(name)  # 可通过cls()方法直接来访问类内部方法


b = B()
B.foo3("nihao")
print(B.foo3)
print("=========" * 10)
print(b)
b.foo3("nibuhao")
print(b.foo3)