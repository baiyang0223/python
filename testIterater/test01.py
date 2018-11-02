from collections import Iterable,Iterator
import time,os,random,sys

class Classmate(object):
    def __init__(self):
        self.names = list()


    def add(self,name):
        self.names.append(name)


    def __str__(self):
        return str(self.names)


    def __iter__(self):
        return ClassIterator(self)  # 将Classmate的引用传下去，以便ClassIterator可访问到当前对象


class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        return
    
    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]  # 访问到Classmate的数据
            self.current_num += 1
            return ret
        else:
            self.current_num = 0
            raise StopIteration

p = Classmate()
p.add("老王")
p.add("小王")
p.add("王二小")

# 注：这里isinstance来Pan段类型是否为迭代器，必须为对象，不能为类，
print("判断Classmate()对象是否可被迭代？ ",isinstance(p,Iterable))
print("判断Classmate()对象是否为迭代器？ ",isinstance(p,Iterator))
if not isinstance(p,Iterable):
    print("对象不可被迭代")
    sys.exit(1)

o = iter(p)
print("判断iter返回对象是否可被迭代？ ",isinstance(o,Iterable))
print("判断iter返回对象是否为迭代器？ ",isinstance(o,Iterator))
if not isinstance(o,Iterator):
    print("返回对象不是迭代器，没有next方法")
    sys.exit(1)


while True:
    try:
        print(next(o))
    except StopIteration:
        break
    time.sleep(1)
print("模拟测试迭代结束")
for temp in p:
    print(temp)
    time.sleep(1)
print("真实运行迭代结束")