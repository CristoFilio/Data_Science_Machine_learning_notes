import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
print(d, '\nDictionary to be passed as Data Frame\n')

df = pd.DataFrame(d)
print(df, '\nData Frame with missing values filled in by NaN\n')

print('Using the .dropna method allows for columns or rows to be dropped if they have missing values\n'
      'This method has arguments to choose the axis and the threshold of missing values\n'
      'example: df.dropna(axis=0,thresh=2) This drops any rows that have 2 or more NaN\n\n',
      df.dropna(thresh=2))

print('\nIf we want to fill in the missing values we can use the .fillna(value="")\n'
      'The value can be filled in using the mean value of the row or column\n\n')

print(df['A'].fillna(value=df['A'].mean()))
print('\nTo fill in the missing value in column A using the mean of that columns '
      '\nwe use df["A"].fillna(value=df["A"].mean())')
