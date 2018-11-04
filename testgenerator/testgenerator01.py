'''
@Author: Baiy
@Date: 2018-11-04 15:57:00
@LastEditors: Baiy
@LastEditTime: 2018-11-04 16:15:27
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: 测试生成器
'''



def fibor(count=0):
    num1 = 0
    num2 = 1
    cursor = 0
    while cursor < count:
        #print(num1)
        yield num1
        num1, num2 = num2, num1+num2
        cursor += 1
    #else:
    #    raise StopIteration


def main():
    """测试生成器"""
    f = fibor(10)
    for temp in f:
        print(temp)


if __name__ == "__main__":
    main()