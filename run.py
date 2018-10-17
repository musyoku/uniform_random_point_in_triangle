import numpy as np
import matplotlib.pyplot as plt

va = np.array([1, 1], dtype=np.float32)[None, :]
vb = np.array([2, 1], dtype=np.float32)[None, :]
vc = np.array([2, 2], dtype=np.float32)[None, :]

u = np.random.uniform(size=(1000, 1))
v = np.random.uniform(size=(1000, 1))
w = np.random.uniform(size=(1000, 1))
sum = u + v + w
u /= sum
v /= sum
w /= sum

sampled_point = va * u + vb * v + vc * w

plt.scatter(sampled_point[:, 0], sampled_point[:, 1])
plt.show()

u = np.random.uniform(size=(1000, 1))
v = np.random.uniform(size=(1000, 1))

sampled_point = va * (1 - np.sqrt(u)) + vb * (np.sqrt(u) * (1 - v)) + vc * (v * np.sqrt(u))

plt.scatter(sampled_point[:, 0], sampled_point[:, 1])
plt.show()