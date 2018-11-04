def test_yield():
    print("----1----")
    yield 1
    print("----2----")
    yield 2
    print("----3----")
    yield 3
    print("----4----")


def fibona_create(max_num):
    print("-----first----")
    a, b = 0, 1
    cursor = 0
    
    while cursor < max_num:
        print("-----second----")
        #print(a)  # 这里如果想保存数据，则占用大量空间
        yield a  # 只要有yield，则 fibona_create 就不是函数了 
        print("-----third----")
        cursor += 1
        a, b = b, a+b
        print("-----forth----")


if __name__ == "__main__":
    """测试生成器"""
    #如果调用的函数中有yield语句，那么就不是函数调用，而是创建一个生成器对象
    obj = fibona_create(10)

    print("start loop")
    """
    for num in obj:
        print(num)
    """
    try:
        while True:
            ret = next(obj)
            print(ret)
    except Exception:
        pass

    print("\n\n" + "=="*20)
    y = test_yield()
    for test in y:
        print("test_yield: ", test)
    