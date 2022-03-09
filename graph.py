import matplotlib
import matplotlib.pyplot as plt
matplotlib.use ('Agg')


x = [255, 127, 64, 32, 5, 2, 0]
y = [3.248, 1.6, 0.810, 0.498, 0.487, 0.485, 0.485]
plt.scatter (x, y)
plt.plot (x, y)
plt.grid()
plt.savefig("graph.png")