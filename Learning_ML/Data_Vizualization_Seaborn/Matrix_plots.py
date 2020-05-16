import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
print(tips.head())
print(flights.head())

tc = tips.corr()

#sns.heatmap(tc,annot=True,cmap='coolwarm')
flp = flights.pivot_table(index='month',columns='year',values='passengers')
print(flp)
sns.heatmap(flp)
plt.show()