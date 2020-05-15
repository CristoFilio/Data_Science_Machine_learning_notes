import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

fig,axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, color='green', linewidth=5, alpha=0.5, marker='o')
axes[0].set_title('First Plot')
axes[1].plot(y, x, color='blue', linewidth=0.5, linestyle='--')
axes[1].set_title('Second Plot')
plt.show()


