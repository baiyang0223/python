from collections import Iterable,Iterator
import time,os,random,sys

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0


    def add(self,name):
        self.names.append(name)

    def __str__(self):
        return str(self.names)

    def __iter__(self):
        return self  # 自己就是迭代器，返回自己的对象即可，然后next可获取到自己的数据
    
    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
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
print("真实运行迭代结束1")
for temp in p:
    print(temp)
    time.sleep(1)
print("真实运行迭代结束2")
