#!/usr/bin/env python
# coding: utf-8

# ***Insurance claims data fraud detection***

# In[2]:


#Libraries for basic operations 
import joypy
import pandas as pd
import numpy as np
#libraries for visualizations
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import plotting
from pandas.plotting import parallel_coordinates 
#for interactive visualizations 
import plotly
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
from plotly import tools
init_notebook_mode(connected=True)
import plotly.figure_factory as ff
#for animated visualizations
from bubbly.bubbly import bubbleplot
import plotly_express as px
#for providing path
import os
print(os.listdir("../input"))
#for modelling
import sklearn
import imblearn
#for model explanation
import shap
import eli5


# In[ ]:


data=pd.read_csv('insurance_claims.csv')
pd.set_option('display.max_columns', None)
data.head()


# In[ ]:


#shape of the dataset
data.shape


# In[ ]:


#information about the data
data.info()


# In[ ]:


data.describe()


# In[33]:


#checking for correlation
data.corr()


# In[ ]:


#checking for covariance 
data.cov()


# **Cleaning the data**

# In[ ]:


#checking whether there are missing values
data.isnull().any()


# **Data Visualizations**

# In[ ]:


#scatter plot
fig= px.scatter(data, x='total_claim_amount', y='policy_annual_premium', color='insured_sex', marginal_x='rug', marginal_y='histogram')
fig.show()


# In[3]:


fig=px.scatter_matrix(data, dimensions=["injury_claim", "property_claim", "vehicle_claim"], color="insured_sex")
fig.show()


# In[ ]:




