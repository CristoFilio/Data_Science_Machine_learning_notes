import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

'''
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y,)
ax.set_ylabel('y label')
ax.set_xlabel('x label')
ax.set_title('Title')
plt.tight_layout()
plt.show()
'''
'''
fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y,)
ax.set_ylabel('y label')
ax.set_xlabel('x label')
ax.set_title('Big plot')
ax2 = fig.add_axes([0.2, 0.55, 0.25, 0.25])
ax2.plot(x, y,)
ax2.set_ylabel('y label')
ax2.set_xlabel('x label')
ax2.set_title('Small plot')

plt.show()
'''
'''
fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, z,)
ax.set_ylabel('z label')
ax.set_xlabel('x label')
ax.set_title('Big plot')
ax2 = fig.add_axes([0.2, 0.55, 0.25, 0.25])
ax2.plot(x, y,)
ax2.set_ylim(30,50)
ax2.set_xlim(20,22)
ax2.set_ylabel('y label')
ax2.set_xlabel('x label')
ax2.set_title('Small plot')

plt.show()
'''
#'''
fig, ax = plt.subplots(nrows=1,ncols=2, figsize=(12,4))

ax[0].plot(x,y,ls='--', color='blue', lw=3)
ax[0].set_title('Blue Dotted')
ax[0].set_ylabel('Y side')
ax[0].set_xlabel('Gogi')
ax[1].plot(x,z,lw=3, color='red')
ax[1].set_title('Red Thickness')
ax[1].set_ylabel('Y side')
ax[1].set_xlabel('Monster')
plt.tight_layout()
plt.savefig('Graphs.png')
plt.show()
#'''
