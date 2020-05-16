import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.columns)
print(titanic.info())


#sns.jointplot(y='age',x='fare',data=titanic,kind='scatter')
#sns.boxplot(x='pclass',y='age',data=titanic)
#sns.barplot(x='fare',y='survived',data=titanic)
#sns.swarmplot(x='pclass',y='age',data=titanic)
#sns.countplot(x='sex',data=titanic)

tcr = titanic.corr()
sns.set_style('darkgrid')
sns.set_palette('pink')
sns.heatmap(tcr,cmap='coolwarm')
plt.title('TITANIC TITLE')
plt.ylabel('Y LABEL')
#sns.jointplot(x='age',y='sex', kind='countplot')

plt.show()