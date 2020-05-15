import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#print(tips.head())

#sns.distplot(tips['total_bill'], kde=False, bins=35)
#sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')#kind = reg, hex, kde
#sns.pairplot(tips, hue='sex', palette='coolwarm')
sns.rugplot(tips['total_bill'])
plt.show()

