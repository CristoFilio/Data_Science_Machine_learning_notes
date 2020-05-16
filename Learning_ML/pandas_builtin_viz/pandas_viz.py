import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df3 = pd.read_csv('df3')
print(df3.info())
print(df3.head())

# df3.plot.scatter(x='a', y='b',figsize=(12,4),color='red')
plt.style.use('ggplot')
# df3['a'].plot.hist(bins=25,alpha=.8)
# df3[['a','b']].plot.box()
#df3['d'].plot.kde(lw=4,ls='--')

df3[0:30].plot.area(alpha=.7)
plt.legend(loc='center left',bbox_to_anchor=(.99,0.5))

plt.show()

