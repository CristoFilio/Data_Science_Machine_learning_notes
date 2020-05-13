import numpy as np

#indexing and slicing of arrays works the same as it does in a list
array_one = np.arange(0,11)

print(array_one[8])
print(array_one[1:5])
print(array_one[0:7])
print(array_one[5:])
print(array_one[::-1])
print(array_one[::2])
print(array_one[::-2])

#"broadcasting" to a variable made from slices of an array, changes the values on the orignal array.
print('\n Broadcasting" to a variable made from slices of an array, changes the values on the orignal array. \n')
print(array_one, '\n Original array \n')
slice_of_array_one = array_one[3:9]
print(slice_of_array_one, '\n Variable made from [3:9] of array one \n')
slice_of_array_one[::] = 100
print(slice_of_array_one, '\n Slice of array one variable values changed to 100 \n')
print(array_one, '\n Original array after changing the variable made from the slice \n')
print('\n Numpy does this to prevent memory errors due to the size of arrays. A variable made from a slice of an array'
      'is not a copy of the slice, but it is more like a view of the slice\n')

array_slice_copy = array_one[3:9].copy()
print(array_slice_copy, '\n This is a copy of the slice of array one [3:9]\n')
array_slice_copy[::] = 15
print(array_slice_copy, '\t Changed the values of the copy of the slice to 15')
print(array_one, '\t No changes were made to the original array \n')

#indexing a 2D array

array_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print('\n Indexing in a matrix or 2D array\n')
print(array_2d, '\n This is the matrix\n')
print(array_2d[0][1], '\n This is in row 0 position 1 can be done with double brackets [0][1] or single [0,1]\n')

print(array_2d[:2,:2], '\n To grab a section of the array u do from row to but not inc , from col to but not inc'
                       ' [:2,:2]\n')

print('Indexing can also be done from conditions\n')
print(array_2d[array_2d > 15], '\Print values in the array that are greater than 15')