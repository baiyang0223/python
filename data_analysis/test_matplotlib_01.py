import random,os,time,sys
from matplotlib import pyplot as plt # import pyplot
# 折线图：简略显示1-12月份平均气温，保存图片

def main():
    x = range(2, 26, 2)  # 从2，4，...24
    y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
    # x和y的len必须一致
    plt.plot(x, y)  # 传入x和y
    plt.show()  # show image


if __name__ == "__main__":
    main()
    pass
