class Test():
    def __init__(self,val=3):
        self.val = 3
        return
    
    def __str__(self):
        return str(self.val)


def test01():
    """返回一个变量"""
    val = 3
    return val

def test02():
    """返回一个元组"""
    tup = (1,2,3,"test02")
    return tup

def test03():
    """返回一个列表"""
    arr = [1,2,3,"test03"]
    return arr


def test04():
    """返回一个字符串"""
    return "this is test04"


def test05():
    """返回一个对象"""
    a = Test(2)
    return a

def test06():
    """返回一个字典"""
    return {"name":"baiyang", "age":18}


def main():
    a = test01()
    print("test01 a = %d" % a)

    b = test02()
    print("test02 b = %s" % (str(b)))

    c = test03()
    print("test03 c = %s" % (str(c)))
    c.append("append")
    print("test03 c = %s" % (str(c)))

    d = test04()
    print("test04 d = %s" % (str(d)))

    e = test05()
    print("test05 e = %s" % (str(e)))

    f = test06()
    print("test06 f=%s" % (str(f)))
    f["like"]="c"
    print("test06 f=%s" % (str(f)))


if __name__ == "__main__":
    main()