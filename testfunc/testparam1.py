g_num1 = None
g_num2 = None

def test01(name,like,val=0):
    """测试位置实参和缺省参数"""
    print("test01:name = %s like = %s val = %d" %(name,str(like),val))


def test02(num1,num2,arr,dic):
    """测试传递局部变量、全局变量、列表、字典的区别"""
    global g_num2
    print("\ng_num1 = %d, g_num2 = %d,num1 = %d num2 = %d\narr=%s\ndic = %s" % 
        (g_num1,g_num2,num1,num2,str(arr), str(dic)))
    num1 = num2 = g_num2 = 0x5A5A5A5A
    arr.append("test02")
    dic["func"] = "test02"


def test03(arr,dic):
    """如何避免修改影响列表和字典？"""
    arr.append("test03")
    dic["func"] = "test03"


def test04(num, *args):
    """测试任意数量实参-会将所有实参组成元组"""
    print("test04:param num-%d,other- %s\n" % (num,str(args)))


def test05(first,last,**userinfo):
    """任意数量实参：**userinfo会接收所有的键值对组成dict"""
    print("test05:param:first %s last %s\nuserinfo %s\n" %(first,last,str(userinfo)))

if __name__ == "__main__":
    num = 1
    g_num1 = 1
    g_num2 =  1
    arr = ["start"]
    dic = {"func":"start"}

    """测试位置参数和缺省参数和关键字实参"""
    test01("baiy","python")
    test01("caowq",["java","c++"],3)
    test01(val =3 ,name = "min",like={"first":"c"})

    """测试传递局部变量、全局变量、列表、字典的区别"""
    """测试发现：传递局部变量、全局变量在函数中修改不会影响调用函数，传递列表和字典会修改调用函数，显示修改全局变量会发生全局修改"""
    test02(g_num1,num,arr,dic)
    print("\ng_num1 = %d, g_num2 = %d,num = %d\narr=%s\ndic = %s\n" % 
        (g_num1,g_num2,num,str(arr), str(dic)))

    """
    如何避免修改影响列表和字典？
    使用列表时：使用列表的切片副本
    使用字典时：暂时未知 TODO
    """
    test03(arr[:],dic)
    print("\narr=%s\ndic = %s\n" % (str(arr), str(dic)))

    """测试任意数量实参-函数中将多余参数组成元组"""
    test04(1,2,3,4,5,6)

    """任意数量实参-传递多个键值对在函数中组成字典"""
    test05("bai","yang", age = 18, like=["c","python"],othre = {"wife":"yan"})