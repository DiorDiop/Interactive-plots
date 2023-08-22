#!/usr/bin/env python
# coding: utf-8

# In[3]:


import plotly.express as px
import pandas as pd

# Load example dataset from Plotly
data = px.data.gapminder()

# Creating an interactive scatter plot using Plotly
fig = px.scatter(data_frame=data, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country',
                 log_x=True, size_max=60)
fig.update_layout(
    title='Interactive Scatter Plot with Plotly',
    xaxis_title='GDP per Capita',
    yaxis_title='Life Expectancy'
)
fig.show()

# Creating an interactive bar plot using Plotly
bar_data = data.groupby(['continent', 'year'])['pop'].sum().reset_index()
bar_fig = px.bar(bar_data, x='year', y='pop', color='continent', barmode='group')
bar_fig.update_layout(
    title='Interactive Grouped Bar Plot with Plotly',
    xaxis_title='Year',
    yaxis_title='Population'
)
bar_fig.show()


# In[ ]:





# In[ ]:




