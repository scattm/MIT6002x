from matplotlib import pyplot as plt
import random

s = []

for i in range(1000):
    s.append(random.gauss(50, 10) + random.gauss(70, 10))

plt.hist(s)
plt.show()
