#%%
import numpy as np
import pandas as pd
# %%
pd.isnull(pd.DataFrame({
    'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
}))
# %%
pd.Series([1, 2, np.nan]).count()
# %%
pd.Series([1, 2, np.nan]).sum()
# %%
df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})

# %%
df

# %%
df.isnull()

# %%
df.loc[df.isnull()]
# %%
df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()})
# %%
s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
# %%
s.isnull().values
# %%
