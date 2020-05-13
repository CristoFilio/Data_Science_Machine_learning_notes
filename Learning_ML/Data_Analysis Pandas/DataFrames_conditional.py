import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df > 0, '\n Data frames con be selected or filetered with conditional statements.\n'
              'df > 0 returns boolean results\n')

print(df[df > 0], '\ndf[df > 0] returns the data frame values for the True boolean and NaN for False\n'
                  'This is not commonly used. It is better to filter using rows and columns\n')

print(df[df['W'] > 0], '\nBy using df[df[\'W\']>0] we can show only the rows which values in column W are > 0\n'
                       'The value in row C column W is < 0 and the row has been filtered out\n')

print(df[df['W'] > 0][['X', 'Z']], '\nYou can also filter a row by a condition on column values, and then display\n'
                                   'only the columns needed. df[df["W"] > 0][["X","Z"]]\n'
                                   'This filters out row C because its value in column W is less than 0 and then\n'
                                   'displays the list of columns X and Z\n')

print('To perform multiple conditions on a data frame, each condition must be inside a () and the operators\n'
      'for "and" and "or" will be "&" "|" respectively\n'
      'The following df[(df["W"] > 0) & (df["Y"] > 1) Will return only the rows that are > 0 in column W\n'
      'and that are > in column Y:\n\n', df[(df["W"] > 0) & (df["Y"] > 1)])

print('\nThe method .reset_index() adds a column index. Remember that to make permanent changes\n'
      'inplace=True must be used\n', df.reset_index())

newind = ('US MX CA KO JA'.split())
print('\nWe created a new list to use for index\n', newind)
print('\nWe then add the list as a column to the data frame by using df["Countries"] = newind\n')
df["Countries"] = newind
print('You can also replace the current index by using a column, in this case the Countries column\n'
      'using the set index method df.set_index("Countries")\n')
print(df.set_index("Countries"))