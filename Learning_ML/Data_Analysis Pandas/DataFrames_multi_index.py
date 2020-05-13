import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# Index Levels

outside = ('G1 G1 G1 G2 G2 G2'.split())
print(outside, '\nOuside list\n')
inside = [1, 2, 3, 1, 2, 3]
print(inside, '\nInside List\n')
hier_index = list(zip(outside, inside))
print(hier_index, '\nList of tuples using the zip method and the two lists\n')
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index, '\ncreates a multi level index  from the list of tuples\n')

# Create Dataframe

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
# data frame ( data = random numbers in 6 rows 2 columns, index labels = hier_index, column labels = A B)

print(df)
print('\nIndexes can be labeled using the index.name method (name, name)')
df.index.names = ['Groups','Num']
print(df)
print('\nTo select individual values in the dataframe you need to specify the outer index first\n'
      'then the inside index, and then the column example: df.loc["G1"].loc[2]["B"]\n\n', df.loc['G1'].loc[2]['B'])

print('\nAnother way of selecting values is using the xs method.\n'
      'You specify the index position inside the level to get the row in the index\n'
      'example: df.xs(1, level="Num")\n\n', df.xs(1, level='Num'))
