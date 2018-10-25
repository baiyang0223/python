#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
     python3 基础语法
"""

print("\n\n############################## 字符串操作函数 ###################################")
#打印函数，print默认会在后边加入换行符
print("hello world")

#字符串操作函数 ->大小写转换、合并字符串、数字与字符串之间转换、字符串排序、比较,删除空白
name = "bAi yaNg"
print(name)
print(name.title()) #每个单词首字母大写,其余都为小写
print(name.upper()) #字母全部大写
print(name.lower()) #字母全部大写

firstStr = "Hello,This is"
secondStr="bai Yang"
comballStr=firstStr + " " + secondStr  #字符串合并
print(comballStr)
print("This is a Introduction " + comballStr + "!")

#删除空白
blank=" testblank "
print(blank.rstrip())#删除末尾多余的空白符号
print(blank.lstrip())#删除开头多余的空白符号
print(blank.rstrip().lstrip())#删除两端的空白符号1
print(blank.strip())#删除两端的空白符号2

#注：字符串使用单引号或者双引号都可以，但避免和字符串中数据的单引号和双引号匹配
message='Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(message)


#特殊符号
print("Computer Language:\n\tpython\n\tC primer plus")








print("\n\n########################## 数字操作函数 #######################################")

#数字操作函数：数字运算，格式化输出，格式化输入，数字与字符串转换，数字与多进制间转换
#python数字运算
print(3+2)
print(3 / 2.0) #python2的 3/2 代表取整，为了兼容，所以将3或者2改为浮点数
print(3-2)
print(3*2)

print("My name is baiyang, I'm " + str(30))  #字符串和数字不能混合打印，必须转换为字符串类型
age="18"
age = int(age) #将字符串转换为数字




print("\n\n######################### 列表 ##########################################")
#列表由一系列按特定顺序排列的元素组成，也就是C里边的元素数组 ：数组遍历、修改/添加/删除某个元素、元素排序
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#列表的基本使用
print(bicycles) #打印列表中所有元素
print(bicycles[1]) #打印列表中指定元素，数组下标也是从0开始，最后一个元素也可以是-1，进行倒序
print("My first bicycle is " + bicycles[2] + " !")

#列表中修改、追加、添加某个元素
bicycles[1] = "feige"   #修改某个元素
print("change arr 1 is feige: " + bicycles[1] + "!")

bicycles.append("jiante") #后边追加元素
print("append arr  is jiante: " + bicycles[4] + "!")

bicycles.insert(0,"28jiazhong") #中间添加某个元素
print(bicycles)

#now bicpyle is ['28jiazhong', 'trek', 'feige', 'redline', 'specialized', 'jiante']
#删除元素包括：根据位置删除、pop末尾弹栈、根据值删除
del bicycles[0]       #根据位置删除，删除第一个元素 ['trek', 'feige', 'redline', 'specialized', 'jiante']
print(bicycles)       
last = bicycles.pop() #会删除最后一个元素并返回最后一个元素 ['trek', 'feige', 'redline', 'specialized']
print(bicycles)
last = bicycles.pop(3) #会删索引为3的元素并返回这个元素 ['trek', 'feige', 'redline']
print(bicycles)         
bicycles.remove('feige')#根据数值删除元素 会删元素"feige"
print(bicycles)   

print("\n\n######################### 列表排序 ##########################################")
#列表排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #列表倒序
print(cars)
print(sorted(cars)) #临时排序
cars.sort(reverse=False) #永久性排序 正序
print(cars)
cars.sort(reverse=True) #永久性排序  逆序
print(cars)
print("arr len is " + str(len(cars))) #len获取列表


print("\n\n######################### 列表遍历 ##########################################")
for car in cars:
    print(car)  #注：循环后必须要至少有一条语句
print("end list car")

for rangeNum in range(1,5):
    print(rangeNum)  #range(a,b)则会自动生成[a,b-1]的列表 range(a,b,c)最后一个参数代表步进个数，缺省为1

numArrs = list(range(1,6))   #函数list()将range()的结果直接转换为列表
for numArr in numArrs:
    print(numArr)

print("numArrs max， min，sum is：")
print(min(numArrs))
print(max(numArrs))
print(sum(numArrs))



"""
4-3 数到 20：使用一个 for 循环打印数字 1~20（含）。
4-5 计算 1~100 的总和：创建一个列表，其中包含数字 1~1 000 000，再使用
min()和 max()核实该列表确实是从 1 开始，到 1 000 000 结束的。另外，对这个列表调
用函数 sum()，看看 Python 将一百万个数字相加需要多长时间。
4-6 奇数：通过给函数 range()指定第三个参数来创建一个列表，其中包含 1~20 的
奇数；再使用一个 for 循环将这些数字都打印出来。
4-8 立方：将同一个数字乘三次称为立方。例如，在 Python 中， 2 的立方用 2**3
表示。请创建一个列表，其中包含前 10 个整数（即 1~10）的立方，再使用一个 for 循
环将这些立方数都打印出来。
4-9 立方解析：使用列表解析生成一个列表，其中包含前 10 个整数的立方。
"""
"""
print("test lianxi 4-3:")
for num4_3 in range(1,21):
    print(num4_3)
num4_5 = list(range(1,101))
print("1+...+100 is " + str(sum(num4_5)))

for num4_6 in range(1,21,2):
    print(num4_6)

num4_8 = []
for num4_8tmp in range(1,10):
    num4_8.append(num4_8tmp ** 3)
print(num4_8)

squares = [value**3 for value in range(1,11)] # 列表解析
print(squares)
"""


print("\n\n######################### 列表切片 ##########################################")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3]) #players[a:b] 返回的是一个新的列表
print(players[3:])   #第3个以后
print(players[:2])   #前边两个
print(players[-3:])  #最后三个
players2=players[:]  #这样就 复制 了一个列表
players2.append("cace")
print(players)
print(players2) #则会发现players和players2不是同一个列表
#问题：如何遍历切片？ 因为name[a:b]返回的就是新的列表，则 for num in name[a:b]:进行遍历
players3=players
players3.append("coffe")
print(players)
print(players3) #则会发现players和players3是同一个列表 ,players3就像是指针一样



print("\n\n######################### 列表与字符串的互相转换 ##########################################")
str1 = "hi hello world"
print(str1.split(" "))
"""
输出：
['hi', 'hello', 'world']
"""
l = ["hi","hello","world"]
print(" ".join(l))
"""
输出：
hi hello world
"""

print("\n\n######################### 元组 ##########################################")
#元组：创建一系列不可修改的元素， 元组可以满足这种需求; 也就是不可修改的列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 #ERROR
dimensions = (400, 100) #给元组变量赋值是正确的
print(dimensions)



print("\n\n######################### if分支 ##########################################")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == "subaru":
        print(car.lower())
    else:
        print(car.title())
#比较条件
#字符串比较  "xxx" == "xxx"   "xxx" != "xxx"
#数字比较    a == b;  a != b;  a > b ; a >= b  a < b; a <= b
#多条件     （条件1） and （条件2）；（条件1） or （条件2）
#True/False 布尔
#检查值是否属于某个列表/元组     in /not in
banned_users = ['andrew', 'carolina', 'david']
#user = 'marie'
user = 'david'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
elif user in banned_users:
    print(user.title() + ",you are now in.")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


emptyArr=[]
if emptyArr:
    print("empytArr is not Empty")
else:
    print("empytArr is  Empty")

print("\n\n######################### 字典 ##########################################")
#字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。
#与键相关联的值可以是数字、字符串、列表乃至字典。
#事实上，可将任何Python对象用作字典中的值。

#字典中添加、删除、遍历、修改获取等属性
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#访问字典中值
print(alien_0['color'])
alien_0['color']="yellow"  #赋值和添加键值对一样
color = alien_0['color']
print(color)
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = "medium"
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position'])+ " " + str(x_increment))   

#删除键值对，和列表一样使用del
del alien_0['points']
print(alien_0)



print("\n\n######################### 字典遍历 ##########################################")
persion={}
persion["first_name"]="bai"
persion["last_name"]="yang"
persion["age"]=29
persion["city"]="beijing"
print(persion)
for key,value in persion.items():#items()，它返回一个键—值对列表 dict_items([('first_name', 'bai'), ('last_name', 'yang'), ('age', 29), ('city', 'beijing')])
    print("\nKey: " + key)
    print("Value: " + str(value)) #字符串使用str后值不变,为了避免age的数字冲突
print("\n")
#注：即便遍历字典时，键—值对的返回顺序也与存储顺序不同。 Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系

favorite_languages = {
    'BaiYang':"C",
    "LuYang":"C++"
}
for name in favorite_languages.keys():#遍历字典时，会默认遍历所有的键,所以keys() 《===》favorite_languages
    print(name.title())
#方法keys()和items()和values()都返回的是列表，所以可以用for来遍历列表
print(persion.items())  #dict_items([('first_name', 'bai'), ('last_name', 'yang'), ('age', 29), ('city', 'beijing')])
print(persion.keys())   #dict_keys(['first_name', 'last_name', 'age', 'city'])
print(persion.values()) #dict_values(['bai', 'yang', 29, 'beijing'])

#因为字典顺序不确定，所以遍历前可使用sorted()对连表进行排序,因为是临时列表，所以好像用不了永久排序sort()方法
for key,value in sorted(persion.items()):
    print("\nKey: " + key)
    print("Value: " + str(value)) 
print("\n")

#set()方法对列表字段去重,
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for value in set(favorite_languages.values()):
    print("Value: " + str(value)) 
print("\n")

print("\n\n######################### 字典嵌套:字典列表 ##########################################")
#将字典存储在列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]#列表中元素都是字典
for alien in aliens:
    print(alien)
print("Total number of aliens: " + str(len(aliens)))

aliens[1]["color"]="blue"   #访问时 aliens[1] 就可以看作alien_0 来使用
aliens[1]["x_posion"]=3
for alien in aliens:
    print(alien)
print("Total number of aliens: " + str(len(aliens)))
  

print("\n\n######################### 字典嵌套:列表字典 ##########################################")
#将列表存储在字典中  在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
pizza['toppings'].append("lajiang")#给数组追加值
print(pizza['crust'])
for topping in pizza['toppings']:
    print("\t" + topping)


#为了简化就不把配料全写出来了
gruel={
    '八宝粥':['大米','桂圆','红枣','芡实','莲子','薏仁','黑豆','核桃仁'],
    '瘦肉粥':['大米','瘦肉']
    }
for key,value in gruel.items():
    print('\n' + key, end=':')
    for batching in value:
        print(batching, end=' ')  #去掉结尾的换行符

print("\n\n######################### 字典嵌套:字典字典 ##########################################")
#在字典中嵌套字典，但这样做时，代码可能很快复杂起来。
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
users["aeinstein"]["age"]="30"
users["aeinstein"]["first"]="bai"
for username,userinfo in users.items():#注：这里因为要遍历里层键值，所以必须要获取users.value()，然后根据键值继续嵌套取值即可
    print("\n"+username +" current userinfo:")
    for userinfok,userinfoval in userinfo.items():
        print("\t"+ userinfok + ": " + userinfoval)

      
grade={
    '赵丽颖':{
        '国籍':'中国',
        '民族':'汉',
        '出生日期':'1987年10月16日',
        '身高':'165cm',        
        },
    '杨幂':{
        '国籍':'中国',
        '民族':'汉',
        '出生日期':'1986年9月12日',
        '身高':'166.5cm',  
        }
    }
for name,info in grade.items():
    print("\n" + name)
    for key,value in info.items():
        print(key+':'+value)



print("\n\n######################### input:用户输入 ##########################################")
#函数input()接受一个参数：即要向用户显示的提示或说明，让用户知道该如何做

"""
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
age = input("How old are you? ")#input输入为字符串
print("I'm " + age)
age = int(age) #将字符串转换为数字
"""

print("\n\n######################### while:循环 ##########################################")
#for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。（因为for与列表顺序无关）
#要在遍历列表的同时对其进行修改，可使用while循环。通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。

#while目前找到三种常用用法：1.用户输入填充链表  2.寻找列表中相关字段，修改或者删除  3.将一个列表迁移到另一个  

#while condition:
#   loop
"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
#while来寻找列表中相关字段
while 'cat' in pets:
    pets.remove('cat')
print(pets)



print("\n\n######################### 函数参数 ##########################################")
#函数是带名字的代码块，用于完 成具体的工作
def greet_user1():
    """显示简单函数用于"""
    print("hello")
greet_user1()    

#位置实参 -就像C语言的函数调用一样，与顺序有关
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("dog", "xiaobai")
describe_pet("cat", "mimi")

#关键字实参 - 与顺序无关，但不能冲突
#describe_pet(pet_name="gaga","birds") #ERROR
describe_pet("birds",pet_name="gaga")  #OK  
describe_pet(pet_name="孙悟空", animal_type="monkey")

#缺省参数
#编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时， Python将使用 指定的实参值；否则，将使用形参的默认值。
#注：和C++一样，缺省参数只能在行参表靠右，否则位置无法对应
#def default_param(animal_type="Dog",pet_name): #ERROR
def default_param(pet_name,animal_type="Dog"):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
default_param("xiaohei")


#传递列表
def greet_user1(names): #类似于指针传递，
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        print("hello ,welcome  " + name.title())
    names.append("xiaohei")

tmp_user=["baiyang","bailiuqiao"]
greet_user1(tmp_user)#列表的传递是指针传递，所针对的修改都是永久的，如果需要值传递，可传递副本greet_user1(tmp_user[:])，但创建副本导致效率降低
print(tmp_user)

"""
#传递列表
def greet_user3(names[:]):      #error???列表不能传切片或者复制体
    for name in names:
        print("hello ,welcome  " + name.title())
    names.append("xiaohei")

tmp_user3=["baiyang","bailiuqiao"]
greet_user3(tmp_user3)#列表的传递是指针传递，所针对的修改都是永久的，
print(tmp_user3)
"""

#传递字典
def greet_user2(names):
    """打印字典"""
    print(names)
    names["like"]="girl"

tmp_user1={"name":"baiyang", "age":30}
print(tmp_user1)
greet_user2(tmp_user1)
print(tmp_user1)    #发现函数中修改对字典 有效，则为指针传递

def test_str(str):
    str = str + "world"
str1="hello"
test_str(str1)  #注意：发现函数中修改对字符串无效，除了列表元组和字典，其余传递都是值复制，不影响本身
print(str1)

#传递任意数量实参
def make_pizza(*toppings):#形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
                          #Python将实参封装到一个元组中，即便函数只收到一个值也如此：问题？？只能是元组么，不能修改阿？？？  
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza2(size,*toppings):
    """打印顾客点的所有配料"""
    print("make size is " + str(size))
    print(toppings)
make_pizza2(16,'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

print(build_profile("bai","yang",age=18,high="178"))

print("\n\n######################### 函数返回值 ##########################################")
#并返回一个或一组值（多个值间用‘，’隔开），也可返回字典或者列表元祖等
def get_formatted_name(first_name,last_name,middle_name=''):
    "返回整洁的姓名"
    if middle_name:
        full_name=first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name=first_name + ' ' + last_name
    return full_name.title()
print(get_formatted_name("bai","yang"))
print(get_formatted_name("bai","qiao","liu"))
def mult_com(left,right):
    value = left + right
    return 0,value

ret,val=mult_com(3,5)
print(ret)
print(val)

#返回字典
def build_persion(first_name,last_name,middle_name=''):
    persion={}
    persion['first_name']=first_name
    persion['last_name']=last_name
    if middle_name:
        persion['middle_name']=middle_name
    return persion

print(build_persion("bai","yang"))

print("\n\n#########################导入函数模块 ##########################################")
#filename.py
#import filename    #导入整个py文件
#使用时 filename.func()#即可
#from filename import func1,func2,func3 #从某个文件导入某些函数 -- 导入特定函数
#from filename import * #导入所有函数
#使用时 func1()即可

#as可为函数制定别名，可来简化函数长度或者名字冲突
#from pizza import make_pizza as mp  #从pizza.py导入 make_pizza函数，别名为mp
#import pizza as p#导入整个py文件，别名为p
#使用时，直接p.func()即可

#细节：
#每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。
#给形参指定默认值时，等号两边不要有空格：
#代码行的长度不要超过79字符
#所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。





print("\n\n#########################测试类##########################################")
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        print("Car init : make: " + self.make + ",model: " + self.model + ",year: " + str(self.year))
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

#end class Car


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        #super().__init__(make, model, year)
        Car.__init__(self,make,model,year)
        self.battersize = 70
    
    def get_batter_size(self,size):
        return self.battersize
    
    def set_batter_size(self,size):
        self.battersize = size
    
    def get_descriptive_name(self):#覆盖父类方法
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + str(self.battersize)
        return long_name.title()



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.set_batter_size(100)
print(my_tesla.get_descriptive_name())
