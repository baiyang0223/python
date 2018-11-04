'''
@Author: Baiy
@Date: 2018-11-04 16:19:59
@LastEditors: Baiy
@LastEditTime: 2018-11-04 16:52:20
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: file content
'''


def fibor(count=0):
    num1 = 0
    num2 = 1
    cursor = 0
    while cursor < count:
        print("firbor cursot =" , cursor)
        val = yield num1
        print("fibor val = ",  val)
        num1, num2 = num2, num1+num2
        cursor += 1
    else:
       return "---Finish---"


def main():
    """测试生成器"""
    f1 = fibor(10)
    
    print(">>>main:val is ",next(f1))
    print(">>>main:val is ",f1.send("hahah"))
    print(">>>main:val is ",f1.send("heiheihei"))
    print(">>>main:val is ",f1.send(None))

if __name__ == "__main__":
    main()

