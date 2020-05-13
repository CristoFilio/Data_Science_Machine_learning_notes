import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df, '\nA Data Frame is a collection of series, and the columns label can be used to call the series\n')
print(df['W'], '\nThis is the column W or series W variable["W"]\n')
print(df[['W', 'X']], '\nThis is the column W and X series called by giving a list of the series ["W","X"]\n')

df['new'] = df['W'] + df['Y']
print(df, '\n You can define new columns into the dataframe using aritmetics df["W"] + df["Y"]\n')

print(df.drop('new', axis=1), '\n.drop takes out a column using its label and the axis 1\n This is not permanent yet')
print(df, '\nThe original data frame still has the column new\n')
df.drop('new', axis=1, inplace=True)
print(df, '\nIn order to drop the column permanently you have to use inplace=True')
print(df.drop('E', axis=0), '\n.drop takes out a row using its label and the axis 0\n This is not permanent yet')
print(df, '\nThe original data frame still has the row E\n')
df.drop('E', axis=0, inplace=True)
print(df, '\nIn order to drop the row permanently you have to use inplace=True')



