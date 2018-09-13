"""横轴：时间范围(0-1000,1000-2000,...,17000-18000)
   纵轴：个数(同一个进程按照不同的线程数来运行，相同的线程数下有多少个运行时间在这个时间范围内
   曲线：每一条曲线对应一个线程数(5,10,15,...100)"""
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('C:\\Users\lenovo\Documents\WeChat Files\wxid_n9iviot545tk22\Files\分类统计结果Demo.xlsx')
data['range'] = data['took_time'].apply(lambda t: int(t/1000))
data.drop(['return_size', 'took_time'], axis=1, inplace=True)
x = []
for i in range(18):
    x.append(str(i)+'-'+str(i+1)+'k')
g = dict(list(data.groupby(['thread_count'])))
colornames = ['black', 'gray', 'rosybrown', 'lightcoral', 'red', 'darkred', 'orange', 'gold', 'olive', 'peru',
              'greenyellow', 'green', 'c', 'deepskyblue', 'navy', 'slateblue', 'violet', 'blueviolet', 'fuchsia', 'hotpink']
for thc in g.keys():
    tmp = []
    for i in range(18):
        tmp.append(0)
    for j in g[thc]['range'].values:
        tmp[j] += 1
    plt.plot(x, tmp, color=colornames[int(thc/5)-1], label=str(thc))
plt.xlabel("timegap")
plt.ylabel("number")
plt.legend()
plt.show()
