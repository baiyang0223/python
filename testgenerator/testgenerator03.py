'''
@Author: Baiy
@Date: 2018-11-04 16:19:59
@LastEditors: Baiy
@LastEditTime: 2018-11-04 16:28:54
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: file content
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
    else:
       return "---Finish---"


def main():
    """测试生成器"""
    f1 = fibor(10)
    f2 = fibor(10)
    
    
    while True:
        try:
            val1 = next(f1)
            print(val1)
            val2 = next(f2)
            print(val2)
        except Exception as e:
            print(e.value)
            break


if __name__ == "__main__":
    main()

