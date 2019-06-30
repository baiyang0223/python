#!/usr/bin/env python
#coding:utf-8

import random,os,time,sys
import matplotlib
from matplotlib import pyplot as plt    # import pyplot
from matplotlib import font_manager     # import font


# 折线图： 显示多条线条，并标明每条线条信息

def main():
    x = range(21,41,1)
    a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
    b = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
    y = range(1,max(a+b)+1,1)

    myfont = font_manager.FontProperties(fname='/usr/share/fonts/MyFonts/simhei.ttf')
    my_blod_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

    # plt.plot(x,a,label="小明")
    # plt.plot(x,b,label="小白")

    # https://www.sioe.cn/yingyong/yanse-rgb-16/
    plt.plot(x,a,label="小明",color="blue",linewidth=1,linestyle="--")
    plt.plot(x,b,label="小白",color=	"#8B008B",linewidth=1,linestyle="-.")

    plt.xlabel("岁数(岁)", fontproperties=myfont)
    plt.ylabel("交友数量(个)", fontproperties=myfont)
    plt.title("约炮统计", fontproperties=my_blod_font)

    plt.xticks(list(x))
    plt.yticks(list(y))

    plt.legend(prop=myfont,loc=1)   # show legend
    plt.show()


if __name__ == "__main__":
    main()
    pass
