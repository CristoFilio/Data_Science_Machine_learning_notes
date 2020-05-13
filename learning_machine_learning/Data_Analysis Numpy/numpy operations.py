import numpy as np

array_one = np.arange(1,11)

print(array_one, 'Original Array\n')
print('Operators to itself\n')
print(array_one + array_one, '+\n')
print(array_one - array_one, '-\n')
print(array_one * array_one, '*\n')
print(array_one / array_one, '/\n')
print(array_one ** array_one, '**\n')
print('\nOperators to a number\n')
print(array_one + 100, '+100\n')
print(array_one - 100, '-100\n')
print(array_one * 100, '*100\n')
print(array_one / 100, '/100\n')
print(array_one ** 4, '**4\n')

