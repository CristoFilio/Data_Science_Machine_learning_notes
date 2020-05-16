import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head)

print(iris['species'].unique())

#g = sns.PairGrid(iris)
#g.map_diag(sns.distplot)
#g.map_upper(plt.scatter)
#g.map_lower(sns.kdeplot)

tips = sns.load_dataset('tips')
print(tips.head())

g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.distplot,'total_bill')

plt.show()