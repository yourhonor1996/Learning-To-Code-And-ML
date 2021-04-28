#%%
import numpy as np
from numpy.core.fromnumeric import sort
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
# %%
sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])
# %%
sales.head()
# %%
sales.describe()
# %%
sales.columns
# %%
customer_data = sales['Customer_Age']
# %%
customer_data.plot(kind= 'kde')
# %%
sales['Country'].value_counts().plot(kind= 'bar', figsize= (14,6))
# %%
sales['Product_Category'].value_counts()
# %%
sales['Product'].value_counts()

# %%
sales['Product'].unique()

# %%
sales['Product'].value_counts(sort= True).head(10).plot(kind= 'bar', xlabel= 'things')
# %%
sales.plot(kind= 'scatter', x= 'Unit_Cost', y= 'Unit_Price', figsize= (6,6))
# %%
sales.plot(kind= 'scatter', x= 'Order_Quantity', y= 'Profit', figsize= (8,8));
# %%
sales[['Profit', 'Country']].boxplot (by='Country', figsize= (10,6))
# %%
sales[['Customer_Age', 'Country']].boxplot(by= 'Country', figsize= (12,8), )
# %%
sales.boxplot(column= 'Customer_Age', by= 'Country', figsize= (10,10))
# %%
