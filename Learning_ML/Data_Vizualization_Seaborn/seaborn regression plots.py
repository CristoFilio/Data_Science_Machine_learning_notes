import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

#sns.set_style(style='darkgrid')

sns.lmplot('total_bill','tip',tips,hue='sex', palette='magma')

#plt.figure(figsize=(12,4))
#sns.countplot(data=tips,x='sex')

plt.show()