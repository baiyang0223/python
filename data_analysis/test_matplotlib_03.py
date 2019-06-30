#!/usr/bin/env python
#coding:utf-8

import random,os,time,sys
import matplotlib
from matplotlib import pyplot as plt    # import pyplot
from matplotlib import font_manager     # import font

# 折线图：显示10-12点温度,调整x和y轴的刻度,支持中文,支持x/y轴线说明

def main():
    temp = [random.randint(20,35) for i in range(120)]  # set per temp
    tm = range(0,120,1)
    print(temp)
    print(tm)

    myfont = font_manager.FontProperties(fname='/usr/share/fonts/MyFonts/simhei.ttf')
    my_blod_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

    plt.figure(figsize=(20,80))

    plt.plot(tm,temp)

    x_label = ["10点{}分".format(i) for i in range(60)]
    x_label += ["11点{}分".format(i) for i in range(60)]

    y_labels = [i / 2 for i in range(40,72,1)] # show 20-35 degrees

    """ set font """
    matplotlib.rc('lines', lw=2, c='r')

    tmp = ["haha{}".format(i) for i in range(1,len(list(tm)[::3])+1, 1)  ]
    plt.xticks(list(tm)[::3], x_label[::3],rotation=45,fontproperties=myfont)
    plt.yticks(list(y_labels))

    plt.xlabel("时间",fontproperties=myfont)
    plt.ylabel("温度 单位(℃)",fontproperties=myfont, rotation=90)
    plt.title("显示8-10点温度信息",fontproperties=my_blod_font)

    # 显示网格
    plt.grid(alpha=0)

    plt.show()


if __name__ == "__main__":
    main()
    pass
