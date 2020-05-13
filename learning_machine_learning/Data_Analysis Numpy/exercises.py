import numpy as np

print(np.zeros(10), '\n')
print(np.ones(10),'\n')
print(np.ones(10)*5,'\n')
print(np.arange(5,51),'\n')
print(np.arange(10,51,2),'\n')
print(np.arange(9).reshape(3,3),'\n')
print(np.eye(3),'\n')
print(np.random.rand(1),'\n')
print(np.random.randn(25),'\n')
print(np.linspace(0.01,1,100).reshape(10,10),'\n')
print(np.linspace(0, 1, 20),'\n')

array = np.arange(1,26).reshape(5,5)

print(array)
print(array[2:,1:])
print(array[3,4])
print(array[0:3,1:2])
print(array[4,::])
print(array[3:,:])

print(array.sum())
print(array.sum(array[::,:1]))