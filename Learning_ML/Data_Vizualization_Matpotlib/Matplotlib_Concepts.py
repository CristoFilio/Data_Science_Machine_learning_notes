import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

plt.plot(x, y, 'r-')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')

# this is Object oriented plotting, gives more control than the methods above
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.48, 0.15, 0.4, 0.3])
axes1.plot(x, y)
axes2.plot(y, x)
axes2.set_xlabel('X Label')
axes2.set_ylabel('Y Label')
axes2.set_title('Smaller plot')

plt.show()
