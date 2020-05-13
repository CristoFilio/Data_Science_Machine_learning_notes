import numpy as np
import pandas as pd

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)
print(df, '\nThe method groupby is very similar to SQL and its helpful in grouping values'
          '\nand displaying helpful operations on the values\n\n')

company_group = df.groupby('Company')
print(df.groupby('Company').mean(), '\nMean of each Company\n')
print(df.groupby('Company').count(), '\nCount of instances per Company\n')
print(df.groupby('Company').min(), '\nMin of Company values\n')
print(df.groupby('Company').describe().transpose(), '\nDescribe shows all the possible operations\n')
print(df.groupby('Company').describe().loc['FB'], '\nDescribe for FB only\n')

