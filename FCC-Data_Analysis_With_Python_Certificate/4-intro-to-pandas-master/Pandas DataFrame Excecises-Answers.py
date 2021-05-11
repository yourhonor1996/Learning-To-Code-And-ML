#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
%matplotlib inline
# %%
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]
# %%
df = pd.DataFrame(marvel_data)
# %%
df
# %%
df.columns?
# %%
df.columns = ['name', 'sex', 'firs_appearance']
df
# %%
df.index = df['name']
# %%
df
# %%
df.drop('name', axis=1, inplace= True)
df
# %%
df.drop(['Namor', 'Hank Pym'], axis= 0, inplace= True)
df
# %%
df.iloc[:5, 0]
# %%
# df.iloc[:5]['sex']
df.iloc[:5]['sex'].to_frame()

# %%
df.iloc[1:-1]
# %%
df.iloc[1:-1]['firs_appearance'].to_frame()

# %%
df.iloc[[0, -1]]
# %%
df.loc['Vision', 'firs_appearance'] = 1964
# %%
df['years_since'] = 2020 - df['firs_appearance']
df
# %%
df.loc['sex'] = 'female'
# %%
df.drop('sex', axis= 0, inplace= True)
df
# %%
df['sex'] == 'female'
# %%
df[df['sex'] == 'female']
# %%
df[df['firs_appearance'] > 1970]
# %%
df[(df['sex'] == 'female') & (df['firs_appearance'] > 1970)]
# %%
df.describe()
# %%
df.info()
# %%
df.reset_index(inplace= True)
df
# %%
df.plot?
# %%
df['firs_appearance'].plot()
# %%
