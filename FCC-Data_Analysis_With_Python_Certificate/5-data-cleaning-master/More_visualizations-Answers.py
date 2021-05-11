# %%
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
# %%
x = np.arange(-10, 11)

# %%
plt.figure(figsize= (12,6))
plt.title('My Nice Plot')
plt.plot(x, x**2)
plt.plot(x, -1 * (x **2))
# %%
plt.figure(figsize= (12, 6))
plt.title('My Nice Plot')

plt.subplot(1, 2, 1)
plt.plot(x, x**2)
plt.plot([0,0], [-10, 100])
plt.legend(['X^2', 'Vertical Line'])
plt.xlabel('X')
plt.ylabel('X Squared')

plt.subplot(1, 2, 2)
plt.plot(x, -1 * (x ** 2))
plt.plot([-10, 10], [-50, -50])
plt.legend(['X^2', 'Horizontal Line'])

plt.xlabel('X')
plt.ylabel('X Squared')

# %%
fig, axes = plt.subplots(figsize= (12, 6))
# %%
axes.plot(x, (x**2),'--r' ,color= 'red', linewidth= 3, marker= 'o', markersize= 8, label= 'X^2')

axes.plot(x, -1 * (x**2), 'b--', label= 'X^2')
# axes.plot(x, -(x **2), 'b--', label= '-X^2')

axes.set_xlabel('X')
axes.set_ylabel('X Squared')
axes.set_title('My Nice Plot')
axes.legend()
# %%
fig
# %%
print(f'Markers: {[m for m in plt.Line2D.markers]}')
# %%
plt.Line2D?
# %%
plot_objects = plt.subplots()

fig, ax = plot_objects

ax.plot([1,2,3], [1,2,3])

plot_objects
# %%
plot_objects = plt.subplots()

fig, ax = plot_objects

ax.plot([1,2,3], [1,2,6])

plot_objects
# %%
x = np.arange(-10, 11)
y = np.array([max(0, n**3) for n in x])
fig, axes = plt.subplots(figsize= (14,6))
axes.plot(x, y, 'b-')
# %%
fig, axes = plt.subplots(2, 2, figsize= (30,6))
((ax1, ax2), (ax3, ax4)) = axes
# %%
ax4.plot(np.random.randn(50), c= 'yellow')
# %%
fig
# %%
ax4.clear()

# %%
fig
#%%
plt.Line2D?
# %%
for item in axes:
    item[0].clear()
    item[1].clear()
ax4.plot(np.random.randn(50), c= 'yellow')
ax3.plot(np.random.randn(50), c= 'red', marker= 'o', animated= True)
ax2.plot(np.random.randn(50), c= 'black', animated= False)
ax1.plot(np.random.randn(50), c= 'yellow')

# %%
fig
# %%
plt.figure?
# %%
plt.figure(figsize=(14, 6))

ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
# %%
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (20 * np.random.rand(N)) ** 2
# %%
fig = plt.figure(figsize= (14, 6))
plt.scatter(x, y, s= area, c= colors, alpha= 0.5, cmap= 'Spectral')
plt.colorbar()
fig

#%%
# plt.scatter?
plt.colormaps()
# %%
fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1,2,1)
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel1')
plt.colorbar()

ax2 = fig.add_subplot(1,2,2)
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel2')
plt.colorbar()
# %%
fig
# %%
