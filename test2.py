import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y = x**2 + 3
z = x*3 + 1

plt.figure()
plt.plot(x,y)
plt.show()
