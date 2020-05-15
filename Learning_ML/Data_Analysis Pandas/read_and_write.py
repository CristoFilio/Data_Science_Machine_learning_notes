import pandas as pd

sal = pd.read_csv('Salaries.csv')
print(sal)
print(sal.head())

print(sal.info())
print(sal['EmployeeName'])
print(sal['BasePay'].mean())

print(sal['OvertimePay'].max())

print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])
# DF[column = column max][
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'])
# salDF[ salDF total payment column value is = to the minimum ] [ employee name]
print(sal.groupby('Year').mean()['BasePay'])
# salary dataframe grouby the column year and give the mean and look for the base pay
print(sal['JobTitle'].nunique())
print(sal['JobTitle'].value_counts().head(10))
print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1))
