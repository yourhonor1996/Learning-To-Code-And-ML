
#%%
import pandas as pd
import numpy as np 

#%%
df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})
df

# %%
df = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})
# %%
df.duplicated()
# %%
df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})
# %%
df['Data'].str.split('_' , expand= True)
# %%
s = pd.Series(["a", None, "b"], dtype= 'string')
# %%
s
# %%
pd.Series?
# %%
a = r'\n the \f'
a
# %%
a[0]
# %%
a[1]
# %%
a.replace?

# %%
