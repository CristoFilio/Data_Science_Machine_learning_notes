import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
array = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

# panda series grabs data on the first argument and the labels on the second one.
print(my_data, "This is a list")
print(labels, 'This is a list \n')
print(pd.Series(my_data, labels), '\nThis is a series using the two lists'
                                  '\npd.Series takes 2 arguments, data and labels\n')

print(array, 'This is an array made from the data list \n')
print(pd.Series(array, labels), '\nThis is a series made from a data array and a labels list\n')

print(d, 'This is a dictionary\n')
print(pd.Series(d), '\nThis is a Series made from the dictionary \n')

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
print(ser1, '\n Series 1\n')
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser2, '\n Series 2\n')

print(ser1['USA'], '\nThis is indexing the value of USA\n')

print(ser1+ser2, '\nSeries can be added if the labels match, and return nan if they dont\n')
