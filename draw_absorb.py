import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
data=pd.read_excel('[muchong.com]标准太阳能光谱数据.xls',header=1, #选择excel子表
                   sheet_name=['Spectra'], usecols=[0,2], names=['nm','y'])
df=data['Spectra']  #选择对应子表的数据
df['energy']=df['nm'].apply(lambda x: 1240/x)  #光的波长转光子能量
#读取计算出来的虚部文件，注意是空格分隔
d1 = pd.read_csv('IMAG_black.in',delimiter='\s+',
    header=1,usecols=[0,1,2,3],names=['energy','xx','yy','zz'])
d2 = pd.read_csv('IMAG_blue.in',delimiter='\s+',
    header=1,usecols=[0,1,2,3],names=['energy','xx','yy','zz'])
d3 = pd.read_csv('IMAG_red.in',delimiter='\s+',
    header=1,usecols=[0,1,2,3],names=['energy','xx','yy','zz'])
x,y=df['energy'].values, df['y'].values
x1 = d1['energy']
x2 = d2['energy']
x3 = d3['energy']
d1.drop(['energy'], axis=1, inplace=True)
d2.drop(['energy'], axis=1, inplace=True)
d3.drop(['energy'], axis=1, inplace=True)
y1=d1.mean(1)       #求行平均
y2=d2.mean(1)
y3=d3.mean(1)
plt.plot(x1, y1, color='black',label='black')
plt.plot(x2, y2, color='blue',label='blue')
plt.plot(x3, y3, color='red',label='red')
plt.xlabel('energy(ev)')
plt.ylabel('absorb(ε^2)')
plt.xlim(0,5)
plt.xticks([1,1.77,2,3,3.1,4], rotation=60)
#plt.axvline(x=3.1,color='yellow',linewidth=1,alpha=0.4)
plt.legend(loc='upper left')
ax=plt.gca()
ax2=ax.twinx()
ax2.set_ylabel('Global tilt(W*m-2*nm-1)')
plt.plot(x,y,color='green',linewidth=1.2,alpha=0.8,label='sun')
#显示可见光波段
plt.fill_between(x,y,where=(1.77<x)&(x<3.1),facecolor='yellow',alpha=0.3)
for label in ax.get_xticklabels():
    label.set_fontsize(9)
plt.legend(loc='upper right')
plt.show()



