#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd


# In[81]:


df=pd.read_csv('IPL_Ball_by_Ball_2008_2022.csv')


# In[82]:


df.info()


# In[83]:


df.head()


# In[84]:


import numpy as np


# In[85]:


df['extra_type'].replace(np.NaN,0, inplace=True)
df['player_out'].replace(np.NaN,0, inplace=True)
df['kind'].replace(np.NaN,0, inplace=True)
df['fielders_involved'].replace(np.NaN,0, inplace=True)


# In[86]:


df.head()


# In[87]:


df.shape


# In[88]:


df.isnull().sum()


# In[89]:


df.describe()


# In[91]:


import plotly.express as px
# df_products = df.groupby('bowler').sum().head(10).sort_values(by='extras_run', ascending=False)
df_data = df.groupby("bowler", as_index=False).sum().sort_values("extras_run", ascending=False).head(10)
fig = px.bar(df_data, x='bowler', y='extras_run', title="Extra run given by bowlers")
fig.show()


# In[92]:


df_run = df.groupby("batter", as_index=False).sum().sort_values("batsman_run", ascending=False).head(10)
fig = px.bar(df_run, x='batter', y='batsman_run', title="Run made by Batsman")
fig.show()


# In[93]:


df_run = df.groupby("bowler", as_index=False).sum().sort_values("total_run", ascending=False).head(10)
fig = px.bar(df_run, x='bowler', y='total_run', title='Total run Given by bowlers')
fig.show()


# In[94]:


df_run = df.groupby("bowler", as_index=False).sum().sort_values("isWicketDelivery", ascending=False).head(10)
fig = px.bar(df_run, x='bowler', y='isWicketDelivery', title="Wicket taken by bowlers")
fig.show()


# In[ ]:


df_wicket = df.groupby("batter", as_index=False).sum().sort_values("kind", ascending=False).head(10)
fig = px.bar(df_wicket, x='batter', y='kind')
fig.show()

