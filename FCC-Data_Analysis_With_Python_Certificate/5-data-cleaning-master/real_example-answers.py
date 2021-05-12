#%%
# from numpy.testing._private.utils import decorate_methods
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline
figSize = (14, 6)
# %%
df = pd.read_csv(
    'data/btc-eth-prices-outliers.csv',
    index_col= 0,
    parse_dates= True
)
# %%
df.plot?
# %%
df.plot(subplots= False, figsize= (14,10), sharex= False)
# %%
df.loc['2017-12':'2017-12-15'].plot(grid= True, figsize= (16,9))
# %%
df_na = df.loc['2017-12' : '2017-12-15']
# %%
df_na
# %%
df_na['Ether'].isna().values.any()
# %%
df_na.loc[df_na['Ether'].isna()]
# %%
df.loc['2017-12-6':'2017-12-12']
# %%
df.loc['2017-12-6':'2017-12-12'].fillna(method= 'bfill', inplace= True)

# %%
df.isna()
# %%
df.loc[df['Ether'].isna()]
# %%
df.loc[df['Ether'].isna() | df['Bitcoin'].isna()]
# %%
df.columns
# %%
df.loc['2017-12-6':'2017-12-12']
# %%
df.plot(figsize= figSize)
# %%
df['2017-12-25':'2018-01-01'].plot()
# %%
df['2018-03-01': '2018-03-09'].plot()
# %%
# %%
df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))
# %%
df_cleaned.plot(figsize= figSize)
# %%
df_cleaned.loc['2017-12-26':'2017-12-30'].plot(figsize= figSize)
# %%
df.plot(figsize= figSize)
# %%
# %%
df.mean()
# %%
df_cleaned.mean()
# %%
df.median()
# %%
df_cleaned.median()

# %%
df_cleaned.plot(kind= 'hist', y= 'Ether', bins= 150)
# %%
df_cleaned.plot(kind= 'hist', y= 'Bitcoin', bins= 150)

# %%
fig, ax = plt.subplots(figsize= figSize)
sns.distplot(df_cleaned['Ether'], rug= True, ax= ax)
#%%
df_cleaned.plot(y= 'Ether')
# %%
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
# %%
df[df['Bitcoin'] < upper_limit].plot(figsize=(16, 7))
# %%
df.drop(df[df['Bitcoin'] > upper_limit].index).plot(figsize=(16, 7))
# %%
df[df['Bitcoin'] > upper_limit]
# %%