import random,os,time,sys
from matplotlib import pyplot as plt # import pyplot

# 折线图：详细显示1-12月份平均气温，保存图片,并设置图片大小

def main():
    x = range(1, 13, 1)  # 从2，4，...24
    y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]


    # flg = plt.figure(figsize=(20,8),dpi=80) # set pyplot global figure config

    # len(x) == len(y)
    plt.plot(x, y)  # 传入x和y

    plt.yticks(range(min(y), max(y)+1, 1))
    plt.xticks(x, ('Jan', 'Feb', 'Mar', 'APR', 'MAY', 'JUN',\
                   'JUL','AUG','SEP', 'OCT', 'NOV', 'DEC'),rotation=45)

    plt.show()  # show image
    # plt.savefig("temp.svg")

if __name__ == "__main__":
    main()
    pass
