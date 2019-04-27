import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
data = pd.read_csv('bands/bands_red.dat',names=['K points', 'energy(ev)','a','b'],header=None,skiprows=1)
k=data['a'].count()
xticks_k = data['a'][:k].values
xticks_v = data['b'][:k].values
n=(21*k)//2
data.drop(['a', 'b'], axis=1, inplace=True)
data.index = data['K points']
data.drop(['K points'], axis=1, inplace=True)
s = data.iloc[0:n].index
rows = data.shape[0]
lines = rows // n
for i in range(lines):
    plt.plot(s, data.iloc[i * n:(i + 1) * n].values)
plt.ylabel('energy')
plt.xlabel('K points')
plt.xticks(xticks_v, xticks_k)
plt.show()