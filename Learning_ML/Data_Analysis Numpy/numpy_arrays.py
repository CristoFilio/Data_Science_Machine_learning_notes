import numpy as np  # imported numpy represented by np

my_list = [1, 2, 3]

arr = np.array(my_list)  # np.array turns list objects into one dimensional array

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # this is a list of lists

two_d_array = np.array(my_mat)  # np.array turns a list of lists into a 2D array

arr_range = np.arange(0, 11, 2)  # np.arange creates a array using start,stop,step

zeros_arr = np.zeros((2, 3))  # np.zeros creates a 2D array using a tuple row,columns

ones_arr = np.ones((4, 3))  # np.ones creates a 2D array using a tuple row,columns

equal_spacing_arr = np.linspace(0, 5, 10)
# np.linspace creates an array of equally separated numbers start, stop, separations

eye = np.eye(4)  # identity matrix

random_matrix_zto = np.random.rand(5, 1)  # np.random.rand generates a random matrix from 0 to 1 using rows and columns

random_m_num = np.random.randn(4, 4,)  # generates a random matrix from random numbers by rows 4 columns 4

random_int_lth = np.random.randint(1, 100, 15)  # generates an array of 15 random numbers low 1 high 99 size 15

print(my_list, '\n', 'My list \n')
print(arr, '\n', 'This is My list transformed to a one dimensional array using np.array \n')
print(my_mat, '\n', 'This is a list of lists \n')
print(two_d_array, '\n', '2D array made from a list of lists using np.array \n')
print(arr_range, '\n', 'Generated array using np.arange(start 0, stop 11, step 2 \n')
print(zeros_arr, '\n', 'Generated 2D array of zeros using a tuple row 2 column 3 \n')
print(ones_arr, '\n', 'Generated 2D array of ones using a tuple row 4 column 3 \n')
print(equal_spacing_arr, '\n', 'Generated equal spacing numbers using start 0 end 5 separations 10 \n')
print(eye, '\n', 'Generated identity matrix used in linear algebra by number of rows 4 \n')
print(random_matrix_zto, '\n Generated random matrix from rows 5 col 1 \n')
print(random_m_num, '\n Generated random matrix from random numbers rows 4 col 4 \n')
print(random_int_lth, '\n Generated random array of 15 numbers from low 1 high 100 \n')

array_one = np.arange(25) #generated array range to 25
print(array_one, '\n Array range to 25 \n')

rand_arr = np.random.randint(0, 100, 10) #generated array of 10 numbers from 1 to 99
print(rand_arr, ' \n Random array of 10 numbers from 0 to 99 \n')

reshape_array_one = array_one.reshape(5, 5) #reshape array one to a 5 by 5 matrix
print(reshape_array_one, '\n Reshaped array one to a 2D matrix of 5 by 5 note: needs enough values to reshape \n')

print(rand_arr.max(), 'is the max value of array one, located at {} postion\n'.format(rand_arr.argmax()))
print(' {} is the min value in the random array located at position {}\n'.format(rand_arr.min(),rand_arr.argmin()))
print('The shape of the reshaped array one is {}'.format(reshape_array_one.shape))
