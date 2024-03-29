import pandas as pd
import numpy as np

ecom = pd.read_csv('Ecommerce Purchases')

print(ecom.head(10))
print(ecom.info())
print(ecom['Purchase Price'].mean())
print(ecom['Purchase Price'].min())
print(ecom['Purchase Price'].max())
print(ecom[ecom['Language'] == 'en']['Language'].count())
print(ecom[ecom['Job'] == 'Lawyer']['Job'].count())
print(ecom['AM or PM'].value_counts())
print(ecom['Job'].value_counts().head(5))
print(ecom[ecom['Lot']=='90 WT']['Purchase Price'])
print(ecom[ecom['Credit Card'] == '4926535242672853']["Email"])
print(ecom[ecom['CC Provider'] == 'American Express'][ecom['Purchase Price'] > 95].count())
print(ecom[ecom['CC Exp Date'].apply(lambda x: x[3:] == '25')].count())
