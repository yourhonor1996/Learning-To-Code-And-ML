#%%
import numpy as np
from numpy import random
print(np.__version__)
# %%
a = np.zeros((10,))
a
# %%
a = np.zeros(10)
a
# %%
b = np.arange(10, 50)
b
# %%
a = np.zeros((2,2), dtype= np.int)
a
# %%
a = np.ones((3, 2), dtype= np.float)
a
# %%
x = np.arange(4, dtype=np.int)

# %%
a = np.ones_like(x)
a
# %%
a = np.zeros_like(x)
x
# %%
a = np.ones((4, 4), dtype= np.int) * 5
a
# %%
a = np.identity(3)
# %%
a = np.random.randint(1,10, (3,3))
a
# %%
a = np.random.random((3,3,3))
a
# %%
a = np.random.randn(3,3,3)
a
# %%
np.arange(9).reshape((3,3))
# %%
Z = np.zeros((10,10))
print(f'{Z.size * Z.itemsize} bytes')
# %%
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

#X[1:-1][1:-1] wrong!
X[1:-1, 1:-1]
# %%
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
X.any()

# %%
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X.sum(axis=1) # 
# %%
X.mean(axis= 0)
# %%
