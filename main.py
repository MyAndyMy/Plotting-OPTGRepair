import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
# ⽀持中⽂以及负数
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False
# 读文件数据
def loadData(fileName):
    inFile = open(fileName, 'r')#以只读方式打开某filename文件
    #定义2个空的list，用来存放文件中的数据
    x = []
    y = []
    for line in inFile:
        trainingSet = line.split(',')#对于每一行，按','把数据分开，这里是分成两部分
        x.append(float(trainingSet[0]))#第一部分，即文件中的第一列数据逐一添加到list x中
        y.append(float(trainingSet[1]))#第二部分，即文件中的第二列数据逐一添加到list y中

    return (x, y)
# 绘图
def plotData(x, y):
    #length = len(y)
    #plt.figure(1)
    plt.plot(x,y,'-o',color='blue')  # 'ko'表示点的类型为黑色实心圆点
    plt.xlabel('Horizontal axis title')
    plt.ylabel('Vertical axis title')
    plt.savefig("/Users/andy/Documents/GitHub/Plotting-OPTGRepair/test.png", dpi=600)
    plt.show()  # 让绘制的图像在屏幕上显示出来
    # 定义渐变⾊范围
    #color1 = '#00FF00'
    #color2 = '#FF0000'
    #color3 = '#D3D3D3'
    #color4 = '#DBDB70'
    #color5 = '#23238E'
    #color6 = '#FF1CAE'
    #cmap = matplotlib.colors.LinearSegmentedColormap.from_list('b2w', [color1, color2, color3, color4, color5, color6])
    #cm.register_cmap(cmap=cmap)
    # 模拟实验数据，实际使⽤换成⾃⼰的
    #x = np.linspace(0, 1, 10)
    #exp_group = {'对照组': list(x), '实验组1': list(x ** 2), '实验组2': list(x ** 3), '实验组3': list(x ** 0.5),
                 #'实验组4': list(x ** 2 + x), '实验组5': list(x ** 3 - x ** 2)}
    #print(exp_group)
    # 利⽤pandas的接⼝绘图更加⽅便，底层仍旧是matplotlib
    #df = pd.DataFrame(exp_group)
    #df.plot(colormap='b2w', style=['-^', '-v', '-<', '->', '-|', '-o'])  # 线型不够⽤还有虚线等可以去官⽹查找
    # 常规的绘图轴、标题设置
    #plt.xlabel('x label')
    #plt.ylabel('y label')
    #plt.title("Black White Plot")

    #plt.show()

    #length = len(y)
    #pylab.figure(1)
    #pylab.plot(x, y, 'ko')#'ko'表示点的类型为黑色实心圆点
(x, y) = loadData('/Users/andy/Documents/GitHub/Plotting-OPTGRepair/123.txt')
print(x, y)
plotData(x, y)