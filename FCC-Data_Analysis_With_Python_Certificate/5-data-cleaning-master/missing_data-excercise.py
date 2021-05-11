#%%
import numpy as np 
import pandas as pd
# %%
falsy_values = (0, False, None, '', [], {})
# %%
any(falsy_values)
# %%
np.nan
# %%
3 + np.nan
# %%
a = np.array([1, 2, 3, np.nan, np.nan, 4])
# %%
a.sum()
# %%
a.sum?
# %%
np.sum?
# %%
3 + None
# %%
a = np.array([1, 2, 3, np.nan, None, 4], dtype='float')
# %%
a
# %%
np.inf / np.inf
# %%
np.inf?
# %%
np.inf
# %%
b = np.array([1, 2, 3, np.inf, np.nan, 4], dtype=np.float)
# %%
b.sum()
# %%
