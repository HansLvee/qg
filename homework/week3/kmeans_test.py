import numpy as np
import matplotlib.pyplot as plt

"""数据"""
X = np.array([
    [1, 2], [1.5, 1.8],
    [5, 8], [8, 8],
    [1, 0.6], [9, 11]
])

"""二分类"""
k = 2
max_iter = 100

"""随机中心"""
np.random.seed(42)
centers = X[np.random.choice(len(X), k, replace=False)]

"""K means 迭代"""
for _ in range(max_iter):
    labels = np.argmin(((X - centers[:, np.newaxis])**2).sum(axis=2), axis=0)
    new_centers = np.array([X[labels == i].mean(axis=0) for i in range(k)])

    if np.all(centers == new_centers):
        break
    centers = new_centers

plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis')
plt.scatter(centers[:,0], centers[:,1], marker='o', s=300, c='red')
plt.show()