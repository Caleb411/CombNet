import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def to_percent(temp, position):
    return '%1.0f' % (temp) + '%'

# 添加数据标签 就是矩形上面的数值
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, height+0.0001*height, '%0.2f'%height+'%', ha='center',  va='bottom', fontsize=12, color='black')
        rect.set_edgecolor('white')

if __name__ == "__main__":
    y1 = [97.76]
    y2 = [97.27]
    y3 = [94.02]
    y4 = [98.09]
    y5 = [95.86]
    x = [1]
    bar_width = 0.1
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    add_labels(plt.bar(x=x,
            height=y1,
            # color='#63b2ee',
            edgecolor='white',
            label='Combw/oAR',
            width=bar_width))
    add_labels(plt.bar(x=[i + bar_width for i in x],
            height=y2,
            # color='#76da91',
            edgecolor='white',
            label='Combw/oCNN',
            width=bar_width))
    add_labels(plt.bar(x=[i + bar_width * 2 for i in x],
            height=y3,
            # color='#f8cb7f',
            edgecolor='white',
            label='Combw/oTA',
            width=bar_width))
    add_labels(plt.bar(x=[i + bar_width * 3 for i in x],
            height=y4,
            # color='#f89588',
            edgecolor='white',
            label='CombNet-GRU',
            width=bar_width))
    add_labels(plt.bar(x=[i + bar_width * 4 for i in x],
            height=y5,
            # color='#7cd6cf',
            edgecolor='white',
            label='CombNet',
            width=bar_width))
    plt.xticks([],[])
    font = {'size': 15}
    plt.ylabel('R2',fontdict=font)
    plt.ylim(86, 100)
    plt.legend(loc='lower left')
    plt.show()
